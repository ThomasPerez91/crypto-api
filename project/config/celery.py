from tasks.test import pouet
import os
from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery.conf.update(
    result_expires=3600,
    broker_connection_retry_on_startup=True
)

# Importez les tâches de tasks/pouet.py

if __name__ == "__main__":
    celery.start()
