def print_numbers(num):
    if num == 0:
        return
    print_numbers(num - 1)
    print(num)


user_input = int(input("Введите num: "))
print_numbers(user_input)
