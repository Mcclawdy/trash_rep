from collections import OrderedDict, namedtuple
from datetime import date, datetime
import pkg_resources
from textwrap import dedent
import sys

from . import helpers as h
from . import storage
from .services import make_connection

Action = namedtuple('Action', ('func', 'title'))
actions = OrderedDict()


def action(cmd, title):
    def decorator(func):
        actions[str(cmd)] = Action(func, title)
        return func
    return decorator


def input_payment():
    """запрашивает id и возвращает его платеж"""
    payment_id = h.input_int('Введите id платежа для поиска')
    payment = storage.get_payment_by_id(payment_id)

    if payment is None:
            print(f'Платежа {payment} не существует')
    return payment


def input_payment_data(payment = None):
    """Ввод данных о платеже"""
    payment = dict(payment) if payment is not None else {}
    data = {}

    data['title'] = h.prompt('Введите название' , default = payment.get('title', ''))

    data['summary'] = h.input_float('Введите сумму', default = payment.get('summary', ''))

    data['quantity'] = h.input_int('Введите количество(по умолчанию 1)', default = payment.get('quantity', 1))
    
    data['created'] = h.input_date('Введите дату платежа в формате Год-месяц-день',  default = payment.get('created', datetime.today()))

    data['description'] = h.prompt('Введите описание', default = payment.get('description', ''))

    return data


@action('1', 'Добавить платеж')
def action_add_payment():
    """Добавить платеж"""
    payment = input_payment_data()
    storage.create_payment(**payment)
    print(f'''Платеж"{payment['title']}" добавлен''')


@action('2', 'Отредактировать платеж')
def action_edit_payment():
    """Отредактировать платеж"""
    payment = input_payment()
    if payment is not None:
        data = input_payment_data(payment)
        storage.update_payment(payment['id'], **data,)
        print(f'Информация о платеже "{payment["id"]}" изменина')


@action('3', 'Вывести все платежи за указанный период')
def action_show_payments_per_date():
    """Вывести все платежи за указанный период"""
    print('Даты указываются в формате Год-месяц-день')
    first_date = h.input_date('Укажите первую дату')
    second_date = h.input_date('Укажите вторую дату')
    get_data = storage.get_payments_per_date(first_date, second_date)
    h.print_table(
        [
           'ID', 'Название', 'Сумма', 'Количество','Дата платежа','Описание'
        ],
        get_data
    )



@action('4', 'Вывести топ самых крупных платежей')
def action_show_top_payments():
    """Вывести топ самых крупных платежей"""
    top = h.input_int('Сколько вывести платежей?')
    get_data = storage.get_top_of_payments(top)
    h.print_table(
        [
            'ID', 'Название', 'Сумма', 'Количество', 'Дата платежа', 'Описание'
        ],
        get_data
    )
        

@action('m', 'Показать меню')
def action_show_menu():
    """Показаь меню"""
    for cmd, action in actions.items():
        print(f'{cmd}. {action.title}')

@action('q', 'Выйти')
def action_exit():
    """Выйти"""
    sys.exit(0)
#0 - завершение программы без ошибок



def main():
    schema_path = pkg_resources.resource_filename(__package__, 'resources/schema.sql')
    storage.initialize(schema_path)
    action_show_menu()
    while 1:
        cmd = input('\nВведите команду: ').strip()
        action = actions.get(cmd)
        if action:
            action.func()
        else:
            print('Вы ввели не верную команду')