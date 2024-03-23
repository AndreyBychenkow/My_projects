def smallest_divisor(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return divisor

    return n


while True:
    num = int(input("Введите число: "))
    smallest_div = smallest_divisor(num)
    print("Наименьший делитель, отличный от единицы:", smallest_div, "\n")
