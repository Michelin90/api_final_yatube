![example workflow](https://github.com/Michelin90/api_final_yatube/actions/workflows/main.yml/badge.svg?style=for-the-badge)
# api_yatube
API, позволяющее создавать собственные публикации, просматривать публикации других авторов,
коментировать их, а так же осуществлять подписки на авторов других публикаций.

## Язык и инструменты:
[![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-blue?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![REST_FRAMEWORK](https://img.shields.io/badge/Django_REST_framework-3.12-blue?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)

## Автор:
Михаил [Michelin90](https://github.com/Michelin90) Хохлов

## Установка и запуск
### Клонировать репозиторий и перейти в него в командной строке:
```
https://github.com/Michelin90/api_final_yatube.git
```
```
cd api_final_yatube
```
### Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source venv/Scripts/activate
```
### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
python3 manage.py migrate
```
### Запустить проект:
```
python manage.py runserver
```
## Примеры запросов
### Создание публикации:
Отпарвьте POST-запрос к следующему эндпоитнту:
```
http://127.0.0.1:8000/api/v1/posts/
```
 в теле запроса обязательно заполните поле 'text'
 
 
### Получение списка публикаций:
Отпарвьте GET-запрос к следующему эндпоитнту:
```
http://127.0.0.1:8000/api/v1/posts/
```
### Получение публикаций по id:
Отпарвьте GET-запрос к следующему эндпоитнту:
```
http://127.0.0.1:8000/api/v1/posts/{id}
```
### Подробная документация проекта:
Чтобы ознакомиться с подробной документацией проекта, перейдите по ссылке:
http://127.0.0.1:8000/redoc/