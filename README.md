# FlaskMicroService
Simple Flask Micro-Service

## To build the flask app:
```bash
$ cd app
$ docker build -t flask-micro-service:latest .
```

## To run the flask app:
```bash
$ docker run -d -p 5000:5000 flask-micro-service:latest
```

## Visit running flask app within broswer via URL:
```bash
http://localhost:5000/
```
