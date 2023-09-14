FROM python:3.8.18-bullseye

EXPOSE 9001

RUN mkdir -p /opt/app
RUN chmod -R 777 /opt/app
WORKDIR /opt/app


COPY web.py /opt/app/web.py
COPY requirements.txt /opt/app/requirements.txt

RUN pip install -r /opt/app/requirements.txt

CMD["python","-u","web.py"]
