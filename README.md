# Тестовое задание от AppEvent

## [Тестовое задание](tz/APPEVENT-1041268741-200121-1222.pdf)

### Рукводоство по запуску
-установить python 3.9

Создать файл .env и заполнить его:
```
NAME_DB = your db name
USER_DB = your db username
PASSWORD_DB = your db username's password
HOST_DB = your db host
PORT_DB = your db port
```

Установка зависимостей и запуск сервера

```commandline
cd folder_with_project\
pip install -r requirements
python manage.py makemigrations
python manage.py migrate
python mange.py runserver localhost:8000
```

### API

#### Получить список новостей с HackerNews: [/posts/](http://localhost:8000/posts/)
POST-запрос
```
Список новостей успешно обновлён!
```

#### Получить список доступных новостей: [/posts](http://localhost:8000/posts)
GET-запрос
```json
[
    {
        "id": 1,
        "title": "Brad Cox, creator of Objective-C, has passed away",
        "url": "https://en.wikipedia.org/wiki/Brad_Cox",
        "created": "2021-01-24T14:18:51.197Z"
    }
]
```

#### Сортировка по атрибутам:
Список доступных атрибутов: id, title, url, created

GET-запросы:

Сделать сортировку по возрастанию атрибутов: [/posts?order=attrubute_name](http://localhost:8000/post?order=attribute_name)
```json
[
    {
        "id": 1,
        "title": "My remote Set up as a Shopify developer and Freelancer (Hardware and software)",
        "url": "https://iliashaddad.medium.com/my-remote-set-up-as-a-shopify-developer-and-freelancer-hardware-software-7a774e0e4fd5",
        "created": "2021-01-24T20:50:13Z"
    },
    {
        "id": 2,
        "title": "Scottish environment agency still struggling against cyber-attack",
        "url": "https://www.theguardian.com/uk-news/2021/jan/22/scottish-environment-agency-struggling-cyber-attack",
        "created": "2021-01-24T20:50:13Z"
    }
]
```

Сделать сортировку по убыванию атрибутов: [/posts?order=-attrubute_name](http://localhost:8000/post?order=-attribute_name)
```json
[
    {
        "id": 10,
        "title": "Rupert Murdoch’s attempt to shakedown Facebook and Google",
        "url": "https://kangaroocourtofaustralia.com/2020/09/13/rupert-murdochs-attempt-to-shakedown-facebook-and-google-is-underwritten-by-scott-morrison-and-the-liberal-party/",
        "created": "2021-01-24T20:50:13Z"
    },
    {
        "id": 9,
        "title": "Ion Trap Quantum Computer",
        "url": "https://spectrum.ieee.org/tech-talk/computing/hardware/commercial-iontrap-quantum-computers-showing-rapid-scaleup",
        "created": "2021-01-24T20:50:13Z"
    }
]
```

#### Вызвать подмножество данных [/posts?offset=number&limit=number](http://localhost:8000/post?offset=number&limit=number)

GET-запрос

По умолчанию offset=0, limit=5

#### Задание нескольких параметров:

Для задания нескольких параметров перечесляем их через символ '&'

Пример: [/posts?order=id&offset=5&limit=10](http://localhost:8000/post?order=id&offset=5&limit=10)


