import os
import time

from .models import File


def file_processing(path):
    time.sleep(5)
    file_name = path.split('/')[2]
    _, extension = os.path.splitext(file_name)
    processing_by_extension(extension)
    file = File.objects.filter(file=file_name).first()
    file.processed = True
    file.save()

def processing_by_extension(extension):
    # do something
    pass