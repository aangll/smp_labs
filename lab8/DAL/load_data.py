import pandas as pd
from Shared.base_command import Command

class LoadDataCommand(Command):
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def execute(self):
        self.data = pd.read_csv(self.filename, delimiter=';')
        return self.data
