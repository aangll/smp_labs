def apply_color(art, color):
    try:
        color_codes = {
            'black_white': '\033[0m',   
            'red': '\033[31m',          
            'green': '\033[32m',      
            'yellow': '\033[33m',       
            'blue': '\033[34m',         
            'gray': '\033[90m',         
        }
        color_code = color_codes.get(color, '\033[0m')
        reset_code = '\033[0m'
        colored_art = [color_code + line + reset_code for line in art]
        return colored_art
    except KeyError:
        print(f"Невідомий колір: {color}. Використано стандартний чорний-білий.")
        return art

def display_art_with_replacement(art):
    replacement_symbol = input("Введіть символ для заміни пробілів (або натисніть Enter, щоб залишити пробіли): ")
    if replacement_symbol:
        art = [line.replace(' ', replacement_symbol) for line in art]
    
    for line in art:
        print(line)
