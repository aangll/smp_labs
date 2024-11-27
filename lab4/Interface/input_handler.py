def get_user_input(prompt, valid_options=None):
    """Отримання введення користувача з валідацією"""
    while True:
        user_input = input(prompt)
        if valid_options and user_input not in valid_options:
            print(f"Невірний вибір. Доступні варіанти: {', '.join(valid_options)}")
        else:
            return user_input

def get_font_size():
    try:
        font_size = int(input("Введіть бажаний розмір шрифту (5, 7, 10): ") or 5)
        if font_size not in [5, 7, 10]:
            raise ValueError("Неправильний розмір шрифту")
        return font_size
    except ValueError as e:
        print(f"Помилка: {e}. Використано стандартний розмір шрифту 5.")
        return 5
