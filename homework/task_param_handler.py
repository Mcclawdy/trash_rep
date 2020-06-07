from abc import ABCMeta, abstractmethod
import os
import pickle
import json


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}
 
    def add_param(self, key, value):
        self.params[key] = value
 
    def get_param(self, key):
        return self.params.get(key)
 
    def get_all_params(self):
        return self.params
 
    def remove_param(self, key):
        del self.params[key]

    def remove_all_params(self):
        self.params = {}

    @abstractmethod
    def read(self):
        pass
 
    @abstractmethod
    def write(self):
        pass


class ParamHandlerException(Exception):
    pass

class ParamHandlerFactory(object):
    types = {}
 
    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name.')
 
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler.'.format(klass)
            )
        cls.types[name] = klass
 
    @classmethod
    def create(cls, source):
        # Шаблон "Simple Factory"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found.'.format(ext)
            )
        return klass(source)


class JsonParamHandler(ParamHandler):
    def read(self):
        """
        Чтение json файла и присвоение параметров self.params
        """
        with open(self.source, 'rb') as f:
            f = json.load(f)
            for i in f:
                self.params[i] = f[i]
            
    def write(self):
        """
        Запись параметров self.params в json файл
        """
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)
 

class PickleParamHandler(ParamHandler):
    
    def read(self):
        """Чтение в формате Pickle и присвоение значений в self.params"""
        with open(self.source, 'rb') as f:
            f = pickle.load(f)
            for i in f:
                self.params[i] = f[i]

    def write(self):
        """Запись в формате Pickle параметров self.params"""
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


ParamHandlerFactory.add_type('json', JsonParamHandler)
ParamHandlerFactory.add_type('pickle', PickleParamHandler)
# config = ParamHandlerFactory.create('./params.json')
# config.add_param('key1', 'val1')
# config.add_param('key2', 'val2')
# config.add_param('key3', 'val3')
# config.write()
# print(config.read())

# config = ParamHandlerFactory.create('./params.pickle')
# config.add_param('key1', 'val1')
# config.add_param('key2', 'val2')
# config.add_param('key3', 'val3')
# config.write()
# print(config.read())
# config = ParamHandlerFactory.create('./d.pickle')
# print(config.read())