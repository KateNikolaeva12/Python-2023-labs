list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players = len(list_players)  # Общее количество игроков
k = players//2  # Количество игроков в команде
first_team = list_players[:k]
second_team = list_players[k:]
print(first_team)
print(second_team)
