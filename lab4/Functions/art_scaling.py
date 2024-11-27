def scale_art(art, scale_factor):
    try:
        scaled_art = []
        for line in art:
            scaled_line = ''.join([char * scale_factor for char in line])  
            for _ in range(scale_factor):
                scaled_art.append(scaled_line) 
        return scaled_art
    except Exception as e:
        print(f"Помилка при масштабуванні ASCII-арту: {e}")
        return art

def get_scaled_font(letter_art, target_size):
    try:
        scale_map = {5: 1, 7: 2, 10: 3}
        scale_factor = scale_map.get(target_size, 1)
        return scale_art(letter_art, scale_factor)
    except KeyError:
        print("Помилковий розмір шрифту. Використано стандартний масштаб.")
        return letter_art
