import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS


#DEBUG = True

app = Flask(__name__)
CORS(app)
#CORS(app, resources=r'/*', allow_headers='Content-Type')


app.config['MONGODB_SETTINGS'] = {
    'db': 'score',
    'host': 'mongodb://user:testpassword@cluster0-shard-00-00.octrg.mongodb.net:27017,cluster0-shard-00-01.octrg.mongodb.net:27017,cluster0-shard-00-02.octrg.mongodb.net:27017/score?ssl=true&replicaSet=atlas-10c7j0-shard-0&authSource=admin'
}


db = MongoEngine(app)

class User(db.Document):
    score1 = db.StringField()
    score2 = db.StringField()
    score3 = db.StringField()
    score4 = db.StringField()
    def to_json(self):
        return {"score1": self.score1,
                "score2": self.score2,
                "score3": self.score3,
                "score4": self.score4
                }


@app.route('/', methods=['GET', 'POST'])
def query_records():
    if request.method == 'GET':
        user = User.objects().all()
        print(user[len(user)-1].to_json())
        if not user:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(user[len(user)-1].to_json())
    elif request.method == 'POST':
        record = json.loads(request.data)
        print('*************')
        print(record)
        print('*************')
        user = User(score1=str(record['score1']),
                    score2=str(record['score2']),
                    score3=str(record['score3']),
                    score4=str(record['score4']))
        user.save()
        return jsonify(user.to_json())



if __name__ == '__main__':
    app.run()