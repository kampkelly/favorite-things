FROM python:3-onbuild

WORKDIR /src

copy requirements.txt /src

RUN pip install -r requirements.txt

COPY api /src/api

EXPOSE 7000

CMD ["python", "server.py"]
