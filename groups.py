data = [
    {
        "firstName": "Игорь",
        "secondName": "Иванов",
        "patronymic": "Иванович",
        "role": "student",
        "rfidId": [0, 672534, 23443325, 6575675, 65464455, 45654565],
        "fingerId": [576786876876988678976, 12345423165542156341265]
    },
    {
        "firstName": "Александр",
        "secondName": "Кузнецов",
        "patronymic": "Сергеевич",
        "role": "student",
        "rfidId": [467234, 42344332, 4657567, 46546445, 44565456],
        "fingerId": [476786876876988678976, 41234542316542156341265]
    },
    {
        "firstName": "Георгий",
        "secondName": "Иванов",
        "patronymic": "Иванович",
        "role": "student",
        "rfidId": [637234, 32344332, 3657567, 36546445, 34565456],
        "fingerId": [736786876876988678976, 13234542316542156341265]
    },
    {
        "firstName": "Илья",
        "secondName": "Соловьёв",
        "patronymic": "Григорьевич",
        "role": "teacher",
        "rfidId": [617234, 21344332, 6157567, 61546445, 41565456],
        "fingerId": [726786876876988678976, 12234542316542156341265]
    }
]

for i in data:
    print(i["firstName"])
    for j in i["rfidId"]:
        if j == 0: print(j)