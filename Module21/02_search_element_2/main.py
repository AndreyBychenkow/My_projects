def find_key(dictionary, target_key, max_depth=None, current_depth=0):
    if isinstance(dictionary, dict):
        if target_key in dictionary:
            print(f"Значение ключа '{target_key}': {dictionary[target_key]}")
            return
        elif max_depth is not None and current_depth >= max_depth:
            print(f"Значение ключа '{target_key}': None")
            return
        else:
            for key, value in dictionary.items():
                find_key(value, target_key, max_depth, current_depth + 1)
    elif current_depth == 0:
        print("Переданный объект не является словарем.")


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

target_key = input("Введите искомый ключ: ")
use_max_depth = input("Хотите ввести максимальную глубину? Y/N: ").lower() == 'y'

if use_max_depth:
    max_depth = int(input("Введите максимальную глубину: "))
    find_key(site, target_key, max_depth)
else:
    find_key(site, target_key)
