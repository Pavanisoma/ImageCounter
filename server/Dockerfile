FROM python:alpine3.7
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=bin/app.py
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]