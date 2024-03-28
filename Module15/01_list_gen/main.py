while True:

    N = int(input("Введите целое число N: "))
    numbers = []

    for i in range(1, N + 1, 2):
        numbers.append(i)

    print("Список нечетных чисел от 1 до", N , ":", numbers, "\n")
