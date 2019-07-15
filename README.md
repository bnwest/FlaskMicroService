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

## Visit running flask app within broswer via URLs:
```bash
http://localhost:5000/
http://localhost:5000/get_versions
```
or via wget:
```bash
$ wget -O - http://localhost:5000/get_versions
--2019-07-13 19:33:25--  http://localhost:5000/get_versions
Resolving localhost (localhost)... 127.0.0.1, ::1
Connecting to localhost (localhost)|127.0.0.1|:5000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 230 [application/json]
Saving to: ‘STDOUT’

-                                    0%[                                                                 ]       0  --.-KB/s               {
  "flask": "0.12.4",
  "flask_restplus": "0.12.1",
  "marshmallow": "2.19.5",
  "python": "3.7.4 (default, Jul 12 2019, 01:10:03) \n[GCC 6.3.0 20170516]",
  "python-info": [
    3,
    7,
    4,
    "final",
    0
  ]
}
-                                  100%[================================================================>]     230  --.-KB/s    in 0s

2019-07-13 19:33:25 (7.26 MB/s) - written to stdout [230/230]
```
or via curl
```bash
$ curl -i -X GET http://localhost:5000/get_versions
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 230
Server: Werkzeug/0.15.4 Python/3.7.4
Date: Sat, 13 Jul 2019 19:32:16 GMT

{
  "flask": "0.12.4",
  "flask_restplus": "0.12.1",
  "marshmallow": "2.19.5",
  "python": "3.7.4 (default, Jul 12 2019, 01:10:03) \n[GCC 6.3.0 20170516]",
  "python-info": [
    3,
    7,
    4,
    "final",
    0
  ]
}
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

# FlaskMicroService - part 2
Less simple Flask Micro-Service.

## /echo endpoint

This is an example of an endpoint that echos backs it input JSON playload.  The python `marshmallow` package validates the incoming JSON payload.

### To exercise the /echo endpoint:
```bash
$ curl -i -X GET http://localhost:5000/echo --header "Content-Type: application/json" --data '{ "answer": 42 }'
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 19
Server: Werkzeug/0.15.4 Python/3.7.4
Date: Sat, 13 Jul 2019 19:09:07 GMT

{
  "answer": 42
}
```

## /echo_plus endpoint

This endpoint extends the previous endpoint by adding a `flask_restplus` model to create the request's response.  Date fields were added to the response.

### To exercise the /echo_plus endpoint:
```bash
$ curl -i -X GET http://localhost:5000/echo_plus --header "Content-Type: application/json" --data '{ "answer": 42 }'
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 107
Server: Werkzeug/0.15.4 Python/3.7.4
Date: Sat, 13 Jul 2019 19:08:57 GMT

{
    "answer": 42,
    "utc": "2019-07-13T19:08:57.303211",
    "utc_alt": "2019-07-13 19:08:57.303238"
}
```
