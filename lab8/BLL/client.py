from UI.visualization import VisualizationReceiver

class Client:
    def __init__(self):
        self.data = None
        self.receiver = VisualizationReceiver(None)
        self.command_stack = []

    def run_command(self, command):
        command.execute()
        self.command_stack.append(command)

    def undo_last_command(self):
        if self.command_stack:
            undone_command = self.command_stack.pop()
            undone_command.undo()
            print(f"Undoing last command: {undone_command}")
