def backpack(items, max_weight):
    sorted_items = sorted(items, key=lambda x: x[1] / x[2], reverse=True)

    selected_items = []

    current_weight = 0
    for item in sorted_items:
        if current_weight + item[1] <= max_weight:
            selected_items.append(item)
            current_weight += item[1]

    return selected_items


items_dict = {
    "спальник": (2.5, 50),
    "палатка": (3.0, 100),
    "еда": (1.5, 30),
    "фонарик": (0.2, 20),
    "карта": (0.3, 15),
    "котелок": (1.0, 40)
}

max_weight = 5.0

items_list = [(item, weight, cost) for item, (weight, cost) in items_dict.items()]

selected_items = backpack(items_list, max_weight)

print("Вещи для похода в рюкзаке:")
for item, weight, cost in selected_items:
    print(f"{item}: {weight} кг, стоимость: {cost}")
