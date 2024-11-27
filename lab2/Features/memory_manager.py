# memory_manager.py
class MemoryManager:
    def __init__(self):
        self.memory = None

    def store_memory(self, value):
        self.memory = value

    def add_to_memory(self, value):
        if self.memory is not None:
            self.memory += value
        else:
            self.memory = value

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = None
