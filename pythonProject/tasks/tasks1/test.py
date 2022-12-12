technic = [('Ноутбук', 1500, 'Татьяна', '89002001020'),
           ('Смартфон', 500, 'Анна', '89202202325'),
           ('Проектор', 300, 'Андрей', '89505205656'),
           ('Принтер', 750, 'Игорь', '89303303236'),
           ('Планшет', 2300, 'Игорь', '89303303236'),
           ('Смартфон', 1000, 'Андрей', '89505205656'),
           ('Ноутбук', 4800, 'Татьяна', '89002001020'),
           ('Наушники', 780, 'Марина', '89562002350'),
           ('Сканер', 550, 'Сергей', '89808564559'),
           ('Планшет', 1200, 'Анна', '89202202325'),
           ('Ноутбук', 1100, 'Игорь', '89303303236'),
           ('Смартфон', 3500, 'Татьяна', '89002001020')]
technic2 = []


def refactor_list():
    temp = []
    for i in range(len(technic)):
        temp.append(technic[i][2])
        temp.append(" ")
        temp.append(technic[i][3])
        temp.append(": ")
        for y in range(len(technic)):
            if temp[0] == technic[y][2]:
                if technic[y][:2] not in temp:
                    temp.append(technic[y][0])
                    temp.append(" - ")
                    temp.append(technic[y][1])
                    temp.append("; ")
        if temp not in technic2:
            technic2.append(temp)
        temp = []
    for i in range(len(technic2)):
        for y in range(len(technic2[i])):
            print(technic2[i][y], end="")
        print()
