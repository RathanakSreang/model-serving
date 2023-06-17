FROM python:3.8-slim

ENV FLASK_APP=src.app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

WORKDIR /model_serving

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . /model_serving

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]