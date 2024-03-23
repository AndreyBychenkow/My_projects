def sum_of_digits(n):
    summ = 0
    while n > 0:
        digit = n % 10
        summ += digit
        n //= 10
    return summ


def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


num = int(input("Введите число: "))
sum_digits = sum_of_digits(num)
count_digits_num = count_digits(num)
difference = sum_digits - count_digits_num

print(f"Сумма чисел: {sum_digits}")
print(f"Количество цифр в числе: {count_digits_num}")
print(f"Разность суммы и количества цифр: {difference}")
