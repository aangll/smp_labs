from Data.letters_5x5 import letters_5x5
from Functions.art_scaling import get_scaled_font

def generate_ascii_art(phrase, font_size, max_width=200, line_spacing=3):
    try:
        ascii_art = ['' for _ in range(5 * font_size)]  
        current_line = 0

        for char in phrase:
            if char in letters_5x5:
                letter_art = letters_5x5[char]
                if font_size == 5:
                    scaled_art = letter_art
                else:
                    scaled_art = get_scaled_font(letter_art, font_size)
                
                for i in range(len(scaled_art)):
                    if len(ascii_art[current_line + i]) + len(scaled_art[i]) > max_width:
                        current_line += len(scaled_art) + line_spacing 
                        if current_line + i >= len(ascii_art): 
                            ascii_art.extend(['' for _ in range(5 * font_size + line_spacing)])
                    
                    ascii_art[current_line + i] += scaled_art[i]
        
        return ascii_art[:current_line + len(scaled_art)] 
    except Exception as e:
        print(f"Помилка при генерації ASCII-арту: {e}")
        return []
