def remove_max_elements(video_cards, n):
    for _ in range(n):
        video_cards.remove(max(video_cards))
    return video_cards


num_cards = int(input("Количество видеокарт: "))
video_cards = []

for i in range(num_cards):
    card_model = int(input(f"Видеокарта {i + 1}: "))
    video_cards.append(card_model)

print("\nСтарый список видеокарт:", video_cards)
new_video_cards = remove_max_elements(video_cards, 2)

print("Новый список видеокарт:", new_video_cards)
