FROM python:3.7

RUN useradd celery -m -s /bin/bash

COPY requirements.txt /app/requirements.txt
COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
