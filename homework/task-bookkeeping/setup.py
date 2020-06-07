"""
name:    имя пакета
version: версия пакета

description:  краткое описание пакета
url:          URL-адрес пакета
license:      лицензия
author:       автор пакета
author_email: почта автора

packages:   пакеты, которые
            нужно скопировать при установке
            (без рекурсии)
py_modules: модули, которые
            нужно скопировать при установке
scripts:    запускаемые из консоли команды
install_requires: прямые зависимости пакета
"""

from setuptools import setup

setup(
    name='task-bookkeeping',
    version='0.0.0',
    description='console bookkeeping',
    license='Apache License 2.0',
    author='Zavmerov Nikita',
    author_email='McClawdy@gmail.com',
    packages=['task_bookkeeping'],
    entry_points={
        'console_scripts': [
            'bookkeeping = task_bookkeeping:main',
        ],
    },
    install_requires=[
        'appdirs',
        'prettytable',
    ],
    package_data={
        'task_bookkeeping': ['resources/*'],
    }
)






