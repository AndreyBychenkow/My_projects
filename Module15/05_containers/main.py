container_weights = []
num_containers = int(input("Количество контейнеров: "))
print()

for i in range(num_containers):
    weight = int(input("Введите вес контейнера:( до 200 кг ) "))

    if 1 <= weight <= 200:
        container_weights.append(weight)
    else:
        print("Масса контейнера не должна превышать 200 кг")

new_weight = int(input("\nВведите вес нового контейнера: "))
position = 1

for weight in container_weights:
    if new_weight <= weight:
        position += 1

print("\nНомер, который получит новый контейнер:", position)
