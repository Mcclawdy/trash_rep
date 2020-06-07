#этот модуль работать с БАЗОЙ ДАННЫХ
from datetime import date , datetime
from .decorators import with_connection


SQL_CREATE_NEW_PAYMENT = 'INSERT INTO bookkeeping (title, summary, quantity, created, description) VALUES (?, ?, ?, ?, ?)'

SQL_UPDATE_PAYMENT = 'UPDATE bookkeeping SET title=?, summary=?, quantity=?, created=?, description=? WHERE id=?'

SQL_SELECT_ALL_PAYMENTS = 'SELECT id, title, summary, quantity, created, description FROM bookkeeping'

SQL_SELECT_TOP_OF_PAYMENT = f'{SQL_SELECT_ALL_PAYMENTS} ORDER BY summary * quantity DESC LIMIT ?' 

SQL_SELECT_PAYMENT_BY_NAME = f'{SQL_SELECT_ALL_PAYMENTS} WHERE title = ?'

SQL_SELECT_PAYMENTS_PER_DATE = f'{SQL_SELECT_ALL_PAYMENTS} WHERE created  BETWEEN ? AND ?'


@with_connection()
def initialize(conn, creation_shema):
    with open(creation_shema) as f:
        conn.executescript(f.read())


@with_connection()
def create_payment(conn, title, summary = 0, quantity = 1, created = datetime.today(), description = ''):
    conn.execute(SQL_CREATE_NEW_PAYMENT, (title, summary, quantity, created, description))


@with_connection()
def update_payment(conn, payment_id, title, summary, quantity, description):
    conn.execute(SQL_UPDATE_PAYMENT, (title, summary, quantity, description, payment_id))


@with_connection()
def get_top_of_payments(conn, limit=1):
    cursor = conn.execute(SQL_SELECT_TOP_OF_PAYMENT, (limit,))
    return cursor.fetchall()


@with_connection()
def get_payment_by_id(conn, payment_id):
    return conn.execute(SQL_SELECT_ALL_PAYMENTS, (payment_id,)).fetchone()


@with_connection()
def get_payments_per_date(conn, date_one, date_two):
    cursor = conn.execute(SQL_SELECT_PAYMENTS_PER_DATE, (date_one, date_two))
    return cursor.fetchall()