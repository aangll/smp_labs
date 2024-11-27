import subprocess
import logging

class LabCommand:
    """Абстрактний клас для команд, що запускають лабораторні роботи"""
    def execute(self):
        raise NotImplementedError("Метод execute() має бути реалізований")


class RunLabCommand(LabCommand):
    """Команда для запуску лабораторної роботи"""
    def __init__(self, path):
        self.path = path

    def execute(self):
        """Виконує команду для запуску лабораторної роботи"""
        logging.debug(f"Запуск скрипту {self.path}")
        subprocess.run(['python', self.path])
