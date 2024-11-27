# cli_interface.py
from Core.calculator import Calculator
from Shared.decimal_precision import DecimalPrecision
from Shared.settings_menu import SettingsMenu


class CLIInterface:
    def __init__(self):
        self.calculator = Calculator()
        self.precision = DecimalPrecision()
        self.settings_menu = SettingsMenu(self.calculator)

    def start(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Perform a Calculation")
            print("2. Go to Settings")
            print("3. Exit")

            choice = input("Select an option (1-3): ")

            match choice:
                case '1':
                    self.perform_calculation()
                case '2':
                    self.settings_menu.display()
                case '3':
                    print("Exiting program. Goodbye!")
                    break
                case _:
                    print("Invalid option. Please try again.")

    def perform_calculation(self):
        while True:
            num1, operator, num2 = self.calculator.get_input()

            try:
                result = self.calculator.calculate(num1, operator, num2)
                result = self.precision.format_result(result)
                print(f"Result: {result}")

                # Add the result to history
                expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}({num1})"
                self.calculator.add_to_history(expression, result)

                # Ask if the user wants to store the result in memory or add it
                self.memory_options(result)

            except Exception as e:
                print(f"Error: {str(e)}")

            if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
                break

    def memory_options(self, result):
        store_in_memory = input(
            "Do you want to store the result in memory (ms) or add it to existing memory (ma)? (ms/ma/no): ").lower()

        match store_in_memory:
            case 'ms':
                self.calculator.memory.store_memory(result)
                print(f"Result {result} stored in memory.")
            case 'ma':
                self.calculator.memory.add_to_memory(result)
                print(f"Result {result} added to existing memory.")
            case _:
                print("Result not stored in memory.")