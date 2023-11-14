import re

from datetime import datetime
from fastapi import FastAPI
from tinydb import TinyDB


db = TinyDB('db.json')
app = FastAPI()

EMAIL_REGEX = r'^[\w\.]+@[\w\.]+\.\w+$'
PHONE_REGEX = r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$'
DATE_FORMATS = ['%d.%m.%Y', '%Y-%m-%d']


def check_value_is_date(value):
    '''
    Функция принимающая значение валидируемого поля,
    В случае если данные указаны в одном из двух вариантов
    даты, присваиваем им типа данных 'date'.
    '''
    for date_format in DATE_FORMATS:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            pass
    return False


def set_data_type(request_data):
    '''
    Функция валидирующая данные.
    По задумке сервис поддерживает 4 типа данных:
    date, phone, email, text.
    Проверяем что данные соответствуют одному из этих типов
    в случае если данные не подходят не к одному из типов,
    указываем что данные указаны не верно.

    '''
    result = {}
    errors = []
    for field, value in request_data:
        str_value = str(value)
        if check_value_is_date(str_value):
            result[field] = 'date'
        elif re.match(PHONE_REGEX, str_value):
            result[field] = "phone"
        elif re.match(EMAIL_REGEX, str_value):
            result[field] = "email"
        elif isinstance(value, str):
            result[field] = "text"
        else:
            errors.append({'validation error':
                           f'field {field} contains invalid data'})
    return result, errors


def find_best_match(request_data, template_data):
    '''
    Функция определяющая к какой форме данные подходят лучше всего.
    Поскольку количество передаваемых полей со значением
    в body запроса не ограничено, это нужно для того, чтобы найти форму,
    к которой подходит больше всего полей.
    Перед началом поиска подходящей формы проверяем что не было ошибок
    при валидации данных.
    После этого проверяем что все ключи и их типы данных совпадают с данными
    кокой-то формы, и если такая форма есть, возвращаем её.
    Если же такой формы нет, возвращаем входящие данные с типом данных
    в качестве значений ключей.
    '''
    result, errors = set_data_type(request_data)
    if errors:
        return errors
    best_match_count = 0
    best_match_template = {}
    for template in template_data:
        template_keys = template.keys() - {'name'}
        if (all(key in dict(request_data) for key in template_keys)
                and all(result[key] == template[key] for key in result
                        if key in template)):
            match_count = sum(
                key in dict(request_data) for key in template_keys)
            if match_count > best_match_count:
                best_match_count = match_count
                best_match_template = template

    if best_match_count > 0:
        return best_match_template['name']
    return result


@app.post("/get_form")
async def get_form(request: dict):
    return find_best_match(request.items(), db.all())
