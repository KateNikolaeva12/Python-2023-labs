list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players = len(list_players)  # Общее количество игроков
team = players/2  # Количество игроков в команде
first_team = list_players[0:int(team)]
second_team = list_players[int(team):]
print(first_team)
print(second_team)