import logging
from .LabCommand import RunLabCommand

class LabCommandFactory:
    """Фабричний клас для створення команд запуску лабораторних робіт"""
    def create_commands(self, labs):
        commands = {}
        for lab_num, path in labs.items():
            commands[lab_num] = RunLabCommand(path)
        logging.debug("Команди для лабораторних робіт створені")
        return commands
