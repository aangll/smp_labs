def align_ascii_art(art, width, alignment):
    try:
        aligned_art = []
        
        for line in art:
            if alignment == 'left':
                aligned_art.append(line.ljust(width))
            elif alignment == 'right':
                aligned_art.append(line.rjust(width))
            elif alignment == 'center':
                aligned_art.append(line.center(width))
            else:
                aligned_art.append(line.center(width))  # Вирівнювання по замовчуванню
        
        return aligned_art
    except Exception as e:
        print(f"Помилка при вирівнюванні: {e}")
        return art
