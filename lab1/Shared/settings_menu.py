# settings_menu.py
class SettingsMenu:
    def __init__(self, calculator):
        self.calculator = calculator

    def display(self):
        while True:
            print("\n--- Settings Menu ---")
            print("1. Change Decimal Precision")
            print("2. View Calculation History")
            print("3. Clear Memory")
            print("4. Return to Main Menu")

            choice = input("Select an option (1-4): ")

            match choice:
                case '1':
                    self.change_precision()
                case '2':
                    self.view_history()
                case '3':
                    self.clear_memory()
                case '4':
                    print("Returning to Main Menu.")
                    break
                case _:
                    print("Invalid option. Please try again.")

    def change_precision(self):
        precision = int(input("Enter the number of decimal places: "))
        self.calculator.set_precision(precision)
        print(f"Decimal precision set to {precision} places.")

    def view_history(self):
        print("\n--- Calculation History ---")
        history = self.calculator.history.get_history()
        if history:
            for entry in history:
                print(entry)
        else:
            print("No calculations performed yet.")

    def clear_memory(self):
        self.calculator.memory.clear_memory()
        print("Memory cleared.")
