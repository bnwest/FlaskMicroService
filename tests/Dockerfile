FROM python:3.7

COPY requirements.txt /test/requirements.txt
COPY . /test/

WORKDIR /test/

RUN pip install -r requirements.txt

ENTRYPOINT ["sleep"]
CMD ["86400"]
