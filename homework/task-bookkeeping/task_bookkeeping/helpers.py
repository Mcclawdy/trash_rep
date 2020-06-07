import os
import textwrap
import appdirs
from prettytable import PrettyTable
import datetime 
from datetime import date
import time


__all__ = (
    'prompt',
    'input_date',
    'input_float',
    'input_int',
    'print_table',
    'print_payment'
)

def prompt(msg , default = None, type_cast = None):
    """Запрашивает данные от пользователя и возвращает ввод"""
    while 1:
        value = input(f'{msg}: ')
        if not value:
            return default

        if type_cast is None:
            return value
        
        try:
            return type_cast(value)
        except ValueError as err:
            print(err)


def input_int(msg = 'Введите число', default = None):
    """Запрашивает и возвращает целое число от пользователя"""
    return prompt(msg, default, int)


def input_float(msg = 'Введите дробное  число', default = None):
    """Запрашивает и возвращает дробное число от пользователя"""
    return prompt(msg, default, float)



def input_date(msg = 'Введите дату в формате Год-месяц-день', default = None, ftm = '%Y-%m-%d'):
    """Запрашивает дату от пользователя"""
    return prompt(
        msg, default, lambda v: datetime.datetime.strptime(v, ftm)
    )


def print_table(headers, iterable):
    """Распечатывает таблицу на экран"""
    table = PrettyTable(headers)
    for row in iterable:
        table.add_row(row)
    print(table)


def print_payment():
    """Распечатывает задачу на экран."""
    print(textwrap.dedent(f'''
    ----------------------------------------------------------------
     Платеж: "{data['title']}"
     Сумма: {data['summary']:%d.%m.%Y}
     Количество: {data['quantity']}
     Дата создания: {data['created']}
    ----------------------------------------------------------------
    Описание: 
    {data['description']}
    ----------------------------------------------------------------
    '''))


def make_dirs_if_not_exists(path):
    """Создает все не существующие директории в переданном пути."""
    if not os.path.exists(path):
        os.makedirs(path, 0o755) 
    return path


user_config_dir = make_dirs_if_not_exists(
    appdirs.user_config_dir(__package__)
)

user_data_dir = make_dirs_if_not_exists(
    appdirs.user_data_dir(__package__)
)
