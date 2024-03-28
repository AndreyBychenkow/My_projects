participants = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

first_day_participants = []

for i in range(0, len(participants), 2):
    first_day_participants.append(participants[i])

print("Первый день:", first_day_participants)
