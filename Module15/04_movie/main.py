films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

favorite_films = []

num_films = int(input("Сколько фильмов хотите добавить?"))

for i in range(num_films):
    film_title = input("\nВведите название фильма: ")

    if film_title in films:
        favorite_films.append(film_title)
        print("Фильм", film_title,  "успешно добавлен в список любимых.")

    else:
        print("Ошибка: Фильма", film_title,  "у нас нет")

print("\nВаш список любимых фильмов:", favorite_films)
