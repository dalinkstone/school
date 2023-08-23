FROM library/python:3.10

WORKDIR /test

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./test /test/

CMD ["python", "tester.py"]