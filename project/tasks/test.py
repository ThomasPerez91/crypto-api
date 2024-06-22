from celery import Celery  # type: ignore

celery = Celery(__name__)


@celery.task(name="pouet")
def pouet(a: int, b: int):
    return a + b
