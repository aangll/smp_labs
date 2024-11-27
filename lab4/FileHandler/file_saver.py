import os

from Data.letters_5x5 import letters_5x5


def save_to_file(content, filename):
    """Збереження ASCII-арту у файл"""
    if not os.path.exists('../assets'):
        os.makedirs('../assets')

    # with open(f'assets/{filename}.txt', 'w') as file:
    #     file.writelines(content)

        with open(f'assets/{filename}.txt', 'w') as file:
            for content in letters_5x5:
                file.write("%s\n" % content)