FROM python:3.7

COPY requirements.txt /app/requirements.txt
COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
#CMD ["app_version.py"]
#CMD ["app_version_blueprint.py"]
