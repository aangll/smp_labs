import logging
from datetime import datetime
from .LabCommandFactory import LabCommandFactory

# Шляхи до файлів для кожної лабораторної роботи
paths = {
    "1": 'C:/Users/Angelina/Desktop/project/lab1/runner.py',
    "2": 'C:/Users/Angelina/Desktop/project/lab2/runner.py',
    "3": 'C:/Users/Angelina/Desktop/project/lab3/runner.py',
    "4": 'C:/Users/Angelina/Desktop/project/lab4/runner.py',
    "5": 'C:/Users/Angelina/Desktop/project/lab5/runner.py',
    "6": 'C:/Users/Angelina/Desktop/project/lab6/runner.py',
    "7": 'C:/Users/Angelina/Desktop/project/lab7/runner.py',
    "8": 'C:/Users/Angelina/Desktop/project/lab8/runner.py',
}

class Runner:
    """Клас Singleton для управління запуском лабораторних робіт"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Runner, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "labs"):
            self.labs = paths
            self.history = []
            self.lab_commands = LabCommandFactory().create_commands(self.labs)
        logging.debug("Ініціалізовано Runner")

    def show_menu(self):
        """Відображає головне меню вибору дій"""
        logging.info("Відображення головного меню")
        print("\nВиберіть дію:")
        print("1. Запустити лабораторну роботу")
        print("2. Відміна останнього запуску")
        print("3. Переглянути історію запусків")
        print("0. Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            self.run_lab()
        elif choice == "2":
            self.undo_last_command()
        elif choice == "3":
            self.show_history()
        elif choice == "0":
            logging.info("Вихід з програми")
            print("Вихід з програми...")
        else:
            logging.warning("Невірний вибір в меню")
            print("Невірний вибір")

    def run_lab(self):
        """Запускає вибрану лабораторну роботу та додає запис в історію"""
        logging.info("Запуск лабораторної роботи")
        print("Виберіть лабораторну роботу для запуску:")
        for lab_num in self.labs.keys():
            print(f"Лабораторна робота {lab_num}")
        choice = input("Ваш вибір: ")

        if choice in self.lab_commands:
            command = self.lab_commands[choice]
            command.execute()
            self.history.append((choice, datetime.now()))
            logging.debug(f"Лабораторна робота {choice} запущена")
        else:
            logging.warning("Невірний вибір лабораторної роботи")
            print("Невірний вибір")

    def undo_last_command(self):
        """Скасовує останній запуск лабораторної роботи"""
        logging.info("Скасування останнього запуску лабораторної роботи")
        if self.history:
            last_choice, timestamp = self.history.pop()
            print(f"Скасування запуску лабораторної роботи {last_choice}, запущеної о {timestamp}")
            logging.debug(f"Скасовано запуск лабораторної роботи {last_choice}")
        else:
            print("Історія порожня. Немає запусків для скасування.")
            logging.info("Історія порожня при спробі скасування")

    def show_history(self):
        """Відображає історію запусків лабораторних робіт"""
        logging.info("Перегляд історії запусків")
        if self.history:
            print("\nІсторія запусків:")
            for lab_num, timestamp in self.history:
                print(f"Лабораторна робота {lab_num}, запущено о {timestamp}")
        else:
            print("Історія запусків порожня.")
            logging.info("Історія запусків порожня")
