# Тестовое задание - Меню для ресторана


## Технологический стек
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)


## Описание проекта
Это приложение для управления меню ресторана. Оно позволяет просматривать опубликованные блюда в различных категориях, если в категории нет блюд (или все блюда данной категории не опубликованы) - выборка будет пустой. В выборку попадают толькоопубликованные Блюда. Через административную панель возможно добавить, отредактировать, удалить или снять с публикации блюдо, а также добавить или удалить категорию блюд. Используется БД sqlite3.


## Запуск проекта

- Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```
git clone https://github.com/SMolodtsova13/restaurant_test_proj.git
```

- Установить и активировать виртуальное окружение

```
source /venv/bin/activate
```

- Установить зависимости из файла requirements.txt

```
pip install -r requirements.txt
```
```
python -m pip install --upgrade pip
```

### Выполните миграции:
```
python manage.py migrate
```

- В папке с файлом manage.py выполнить команду:
```
python manage.py runserver
```

- Создание супер пользователя 
```
python manage.py createsuperuser
```


## Основные адреса: 

| Адрес                        | Описание |
|:-----------------------------|:---------|
| 127.0.0.1:8000               | Главная страница |
| 127.0.0.1:8000/admin/        | Для входа в панель администратора |
| 127.0.0.1:8000/api/v1/foods/ | Описание работы API |



## Автор:  
_Молодцова Светлана_  
**telegram** _@smolodtsova_