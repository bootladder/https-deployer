FROM alpine

# install dependencies
RUN apk update 
RUN apk add  py-pip python-dev curl wget

WORKDIR /opt/install
COPY ./requirements.txt  .
RUN pip install -r requirements.txt

# run app
WORKDIR /opt/server
CMD ["python","-u","server.py"]

