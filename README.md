## Асинхронный обработчик загруженных файлов

 Django REST API, который позволяет загружать файлы на сервер, 
 а затем асинхронно обрабатывать их с использованием Celery.

В проекте реализован эндпоинт POST http://127.0.0.1:80000/upload/, который принимает POST-запросы 
для загрузки файлов.

При загрузке файл сохраняется на сервер, после чего запускается асинхронная 
задача для обработки файла с использованием Celery, по окончании которой
статус загруженного файла - processed меняется на True. 

Также реализован эндпоинт http://127.0.0.1:80000/files/, который возвращает 
список всех загруженных файлов с их данными  

### Использованные инструменты:

* Python
* Django
* Django REST Framework
* Celery
* Redis

### Запуск и использование

Клонировать проект
```shell
git clone 
```

Из директории с проектом запустить команду сборки и запуска контейнеров 
```shell
docker-compose up -d --build
```
Отправить POST запрос на эндпоит http://127.0.0.1:80000/upload/, в теле 
которого передать файл и указать атрибут `enctype="multipart/form-data"`
В качестве демонстрации симулируется задержка выполнения обработки файла, однако
это не приводит к блокировке всего приложения. Это можно проверить отправив 
GET запрос на эндпоинт http://127.0.0.1:80000/files/, который вернет 
список загруженных файлов, среди которых будет последний загруженный файл,
статус которого изменится спустя 5 сек. после сохранения его на сервере.