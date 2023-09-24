from core.celery import app
from .service import file_processing


@app.task
def processing(file):
    file_processing(file)