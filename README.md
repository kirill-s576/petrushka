# Petrushka Project


### Main Stack:
    
- Backend:
    - Python
    - Framework: Flask
- Frontend:
    - JavaScript
    - Framework: Vue.js + Nuxt


### Этап 1.
#### Устанавливаем и настаиваем окружения для работы.

Back
1. ```python3 -m venv venv ``` Настраиваем виртуальное окружение Python.
2. ```source venv/bin/activate ``` Запускаем виртуальное окружение Python.
3. ```pip install flask ``` Устанавливаем Flask в виртуальное окружение
4. Создаем файл requirements.txt, в который будем вносить все зависимости связанные с проектом.

___

Front
1. Устанавливаем Node JS по интсрукции для своей операционной системы.
[Инструкции здесь](https://nodejs.org/ru/download/package-manager/)
2. Создаем чистый Nuxt Js проект по инструкции из официальной документации.
[Инструкции здесь](https://ru.nuxtjs.org/). <br>
По умолчанию добавляем плагины:
    - Axios.js для отправки http запросов.
    - Vuetify.js - UX/UI фреймворк для помощи в создании приятного интерфейса.
3. ``` npm run dev ``` Проверяем запускается ли проект.
7. Должна появится стартовая страница Nuxt.
![Alt Text](./docs/images/nuxt-start.gif)

### Этап 2.
#### Определяем цели проекта.

1. Создать базу данных для хранения информации.
2. Создать API для наполнения базы данных сторонним микросервисом.
3. Создать API для чтения информации из БД со стороны Frontend.
4. Документировать методы API.
5. Создать меню с выбором таблиц мониторинга.
6. Создать страницы с необходимыми таблицами и дать возможность переключаться между ними через меню.


### Этап 3.
#### Разработка базы данных.

Эскиз схемы БД.
![database-schema](./docs/images/DB_Schema.png)

Для создания таблиц базы данных и работы с ними мы будем использовать простую библиотеку Peewee
[Ссылка на документацию](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#)

Настройки подключения к базе данных задаются в файле
[config.py](./back/config.py)

Описание моделей находится в файле
[models.py](./back/src/database/models.py)

Перед запуском приложения нам необходимо создать таблицы согласно схеме
Для того, чтобы приложение перед каждым запуском сервера проверяло наличие нуджных таблиц в базе данных и создавало их - добавляем функцию в файл
[app.py](./back/app.py). Прямо перед запуском сервера.
```python
from src.database.models import create_all_tables

create_all_tables()
``` 
База данных готова к работе.


### Этап 4.
#### Разработка и создание API методов.

У нас имеется 4 объекта предметной области и соответственно 4 таблицы в базе данных.
Удобно использовать следующую схему работы с API:

GET    /<object>      - список объектов.
POST   /<object>      - создание нового объекта, где в теле запроса передается JSON с описанием его полей.
GET    /<object>/{id} - получение информации о конкретном объекте по его id.
POST   /<object>/{id} - обновить поля объекта по его id, где в теле запроса передается JSON с новыми данными объекта.
DELETE /<object>/{id} - удалить объект по id.

Стоит учесть, что записей в базе данных может быть очень много, поэтому для всех запросов на получение списка обхектов
добавляем новый параметр "page".
Количество объектов, которые отдаются на странице ограничивается в файле
[config.py](./back/config.py) переметром OBJECTS_PER_PAGE(по умолчанию 20).

Для выбора страницы отправляется параметрический GET запрос:
GET    /<object>?page=n , где n-номер страницы
Результатом работы этого метода будет JSON следующего формата:

```json
{
  "page": 1,
  "total": 1050,
  "objects": [
    {}, {}, {}
  ]
}
```

Созданные эндпоинты можно найти в файле роутера 
[router.py](./back/src/router.py)