FROM python:3.9

RUN mkdir /work
WORKDIR /work

COPY requirements.txt /work
RUN pip install -r ./requirements.txt

COPY main.py /work
ENTRYPOINT python main.py
