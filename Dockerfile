FROM library/python:3.10

WORKDIR /test

COPY ./test /test/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python tester.py