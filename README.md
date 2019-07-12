# FlaskMicroService
Simple Flask Micro-Service

## To build the flask app:
```bash
$ cd app
$ docker build -t flask-micro-service:latest .
```

## To run the flask app:
```bash
$ docker run -d -p 5000:5000 flask-micro-service
90b5e91f873c5fe9acf014ca63cfc5235a5b5d66ecb534c83cc9963bba98c36f
```

## Visit running flask app within broswer via URL:
```bash
http://localhost:5000/
```

## Checkout the logs while running
```bash
$ docker logs 90b5e91f873c5fe9acf014ca63cfc5235a5b5d66ecb534c83cc9963bba98c36f
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 227-495-239
172.17.0.1 - - [12/Jul/2019 18:18:57] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [12/Jul/2019 18:19:01] "GET /get_versions HTTP/1.1" 200 -
```
