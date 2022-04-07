FROM python:buster

RUN pip3 install web3
COPY ./src /app

ENTRYPOINT ["python","/app/app.py"]

