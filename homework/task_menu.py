from abc import ABCMeta, abstractmethod


class CommandException(Exception):
        pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class Menu(metaclass=ABCMeta):
    def __init__(self):
        self.tasks = {}
        self.tasks_count = 0

    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))
        self.tasks[name] = klass

    def execute(self, name, *args, **kwargs):
        if name not in self.tasks:
            raise CommandException('Command with name "{}" not found'.format(name))
        klass = self.tasks.get(name)
        return klass(*args, **kwargs).execute()

    def __next__(self):
        if self.tasks_count >= len(list(self.tasks.items())):
            raise StopIteration
        else:
            command = list(self.tasks.items())[self.tasks_count]
            self.tasks_count += 1
            return command

    def __iter__(self):
        return self