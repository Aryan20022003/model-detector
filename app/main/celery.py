from celery import Celery
import time
import requests

app = Celery(
    "main",
    broker="amqp://",
    backend="redis://",
    include=["main.tasks"],
)
