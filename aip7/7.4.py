import random
group1 = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Козлов", "Новиков", "Волков", "Морозов", "Алексеев", "Лебедев"]
group2 = ["Михайлов", "Павлов", "Иванов", "Захаров", "Романов", "Дягилев", "Пупченко", "Корнеев", "Николаев", "Дягтерёв"]
team = tuple(random.sample(group1, 5) + random.sample(group2, 5))
print(f"Группа1: {group1}")
print(f"Группа2: {group2}")
print(f"Спортивная команда: {team}")
print("Длина кортежа: ", len(team))
sorted_team = tuple(sorted(team))
print(f"Команда по алфавиту: {sorted_team}")
if "Иванов" in team:
    print("Иванов в команде")
else:
    print("Иванов не в команде")
print('Фамилия "Иванов" встречается количество раз: ', team.count("Иванов")) 
