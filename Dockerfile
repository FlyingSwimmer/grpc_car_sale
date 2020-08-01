from python:3

RUN apt update && apt install postgresql-server-dev-all -y

RUN mkdir code

ADD . code/

WORKDIR code

RUN pip install -r requirements.txt

CMD ["python", "server.py"]