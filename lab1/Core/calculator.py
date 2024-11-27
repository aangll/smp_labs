# calculator.py
from Features.memory_manager import MemoryManager
from Features.history_manager import HistoryManager
from Shared.decimal_precision import DecimalPrecision

class Calculator:
    def __init__(self):
        self.memory = MemoryManager()
        self.history = HistoryManager()
        self.precision = DecimalPrecision()

    def get_input(self):
        print("\n--- Enter Numbers ---")
        num1 = self._get_number("first")
        operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
        num2 = None
        if operator not in ['√']:
            num2 = self._get_number("second")
        return num1, operator, num2

    def _get_number(self, position):
        use_memory = input(f"Do you want to use the number stored in memory for the {position} number? (yes/no): ").lower()
        if use_memory == 'yes' and self.memory.get_memory() is not None:
            return self.memory.get_memory()
        else:
            return float(input(f"Enter the {position} number: "))

    def calculate(self, num1, operator, num2=None):
        match operator:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                return num1 / num2
            case '^':
                return num1 ** num2
            case '√':
                if num1 < 0:
                    raise ValueError("Cannot calculate the square root of a negative number.")
                return num1 ** 0.5
            case '%':
                return num1 % num2
            case _:
                raise ValueError("Invalid operator.")

    def set_precision(self, precision):
        self.precision.set_precision(precision)

    def add_to_history(self, expression, result):
        self.history.add_to_history(expression, result)
