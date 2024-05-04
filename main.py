import requests
import datetime as dt

# Вывод на момент сдачи ДЗ:
# Wilson VonRueden ID: 52
# Сумма всех состояний (первые 76 записей): 33329.8
# Самый старый: Anita Greenfelder
# Самый бедный: Miss Taylor Willms
# Родились в апреле: 4

url = 'https://66095c000f324a9a28832d7e.mockapi.io/users'
response = requests.get(url)

# срез для использования только первых 76 id (дальше будут добавленные студентами)
res = response.json()[:76]

# Я пока плохо знаю итераторы.
# Мне кажется, таким образом я прерываю перебор при нахождении первого вхождения
scouting = next((i for i in res if i.get("name") == 'Wilson VonRueden'), None)
print(f'Wilson VonRueden ID: {scouting.get('id')}')

print(f'Сумма всех состояний (первые 76 записей): {sum(float(i.get("state", 0)) for i in res)}')

time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
print(f'Самый старый: {min(res, key=lambda x: dt.datetime.strptime(x.get("birth"), time_format)).get("name")}')
print(f'Самый бедный: {min(res, key=lambda x: float(x.get("state"))).get("name")}')
print(f'Родились в апреле: {sum(1 for i in res if i.get("birth").split("-")[1] == "04")}')

# для визуальной проверки правильности последовательности, вывод закомментирован
ascending_to_death = sorted(res, key=lambda x: dt.datetime.strptime(x.get("birth"), time_format))
descending_by_success = sorted(res, key=lambda x: float(x.get("state")), reverse=True)
# print('Даты рождения по восходящей')
# [print(f'{j} {i.get("name")}, {i.get("birth")}') for j, i in enumerate(ascending_to_death, 1)]
# print('Состояние по нисходящей')
# [print(f'{j} {i.get("name")}, {i.get("state")}') for j, i in enumerate(descending_by_success, 1)]

print('\nSo long...')
