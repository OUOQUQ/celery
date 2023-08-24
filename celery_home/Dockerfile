FROM python:3.9.10-alpine3.15

WORKDIR /celery_work

COPY * .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--preload"]