results = [9, 12, 5, 8, 10, 3, 7, 6]

for i in range(len(results) - 1, -1, -1):
    if results[i] % 2 == 0:
        print(results[i])
