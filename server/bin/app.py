import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'mongodb://user:testpassword@cluster0-shard-00-00.octrg.mongodb.net:27017,cluster0-shard-00-01.octrg.mongodb.net:27017,cluster0-shard-00-02.octrg.mongodb.net:27017/test?ssl=true&replicaSet=atlas-10c7j0-shard-0&authSource=admin'
}


db = MongoEngine(app)


class Score(db.Document):
    imageid=db.StringField()
    url=db.StringField()
    count=db.IntField()
    def to_json(self):
        return {"imageid": self.imageid,
                "url":self.url,
                "count": self.count,
                }


@app.route('/', methods=['GET', 'POST'])
def query_records():
    if request.method == 'GET':
        score = Score.objects().all()
        if not score:
            return jsonify({'error': 'data not found'})
        else:
            return jsonify(score)
    elif request.method == 'POST':
        record = json.loads(request.data)
        print('*************')
        print(record)
        score=Score(imageid=str(record['imageid']),
                    url=str(record['url']),
                    count=str(record['count']))
        score.save()
        return jsonify(score)


@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    score = Score.objects(imageid=record['imageid'])
    if not score:
        return jsonify({'error': 'data not found'})
    else:
        score.update(count=record['count'])
    return jsonify(score.to_json())
            
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    score = Score.objects(imageid=record['imageid'])
    if not score:
        return jsonify({'error': 'data not found'})
    else:
        score.delete()
    return jsonify(score.to_json())



if __name__ == '__main__':
    app.run()