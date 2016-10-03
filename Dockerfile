FROM python:3.5.2
MAINTAINER Harshada "harshada.bhide@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["home.py"]
