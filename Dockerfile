FROM python:3.8

ENV PYTHONUNBUFFERED True

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

EXPOSE 5000

COPY . .

RUN python download_model.py

CMD ["flask", "run", "--host", "0.0.0.0"]