def find_key(dictionary, target_key):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            result = find_key(value, target_key)
            if result is not None:
                return result
        elif key == target_key:
            return value
    return None


def create_site(product_name):
    site_template = {
        'html': {
            'head': {
                'title': f'Куплю/продам {product_name} недорого'
            },
            'body': {
                'h2': f'У нас самая низкая цена на {product_name}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }
    return site_template


num_sites = int(input("Сколько сайтов: "))
sites = []

for i in range(num_sites):
    product_name = input(f"Введите название продукта для нового сайта {i + 1}: ")
    new_site = create_site(product_name)
    sites.append(new_site)

    print(f"Сайт для {product_name}:")
    for site in sites:
        print(f"site = {site}")
