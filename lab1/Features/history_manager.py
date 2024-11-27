# history_manager.py
class HistoryManager:
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def get_history(self):
        return self.history
