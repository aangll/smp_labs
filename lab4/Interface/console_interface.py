from Interface.input_handler import get_user_input, get_font_size
from Functions.art_generator import generate_ascii_art
from Functions.art_alignment import align_ascii_art
from Interface.output_handler import apply_color, display_art_with_replacement
from FileHandler.file_saver import save_to_file

def start_console_interface():
    try:
        # Отримання введення користувача
        phrase = get_user_input("Введіть текст для ASCII-арту: ")
        font_size = get_font_size()

        # Генерація ASCII-арту
        ascii_art = generate_ascii_art(phrase, font_size, max_width=200, line_spacing=3)

        # Вибір кольору для ASCII-арту
        color = "black_white"
        colored_art = apply_color(ascii_art, color)

        # Вибір вирівнювання ASCII-арту
        alignment = input("Виберіть вирівнювання (left, right, center): ").strip().lower()
        width = 200
        aligned_art = align_ascii_art(colored_art, width, alignment)

        # Виведення результату з заміною пробілів
        print("\nРезультат:")
        display_art_with_replacement(aligned_art)

        # Збереження у файл
        save_choice = get_user_input("Зберегти результат у файл? (y/n): ", ['y', 'n'])
        if save_choice == 'y':
            filename = input("Введіть ім'я файлу: ")
            save_to_file(ascii_art, filename)
            print(f"ASCII-арт збережено у файл: assets/{filename}.txt")

    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")

