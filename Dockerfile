FROM python:3.5.2
MAINTAINER Harshada "harshada.bhide@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install	configparser
RUN pip install	pymysql
RUN pip install	flask
RUN pip install	flask-sqlalchemy
RUN pip install	flask-wtf
RUN pip install	sqlalchemy
RUN pip install	Flask-Script
RUN pip install	Flask-Migrate
RUN pip install	simplejson
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000