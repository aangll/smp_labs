from Shared.base_command import Command

class ExtremeValuesCommand(Command):
    def __init__(self, data):
        self.data = data
        self.extreme_values = None

    def execute(self):
        self.extreme_values = self.data.describe()
        return self.extreme_values

    def undo(self):
        self.extreme_values = None


class BasicVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.basic_visualization()


class ExtendedVisualizationCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.extended_visualization()
