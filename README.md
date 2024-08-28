# api_final

### Описание:

API для Yatube -- площадки, которая позволяет пользователям делиться публикациями и фотографиями, комментировать посты и подписываться на других пользователей.

### Стек:
* Python
* Django
* Django REST framework

### Как установить и запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:NikitaPreis/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/scripts/activate
```

Обновить pip и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
