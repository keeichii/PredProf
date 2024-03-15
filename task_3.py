f = open('books.txt', encoding="utf-8").readlines()[1:]
while True:
    inp = input('Автор: ')
    out = []

    for i in range(1, len(f)):
        data = f[i].split('%')
        item = data[2].split(', ')
        if inp in item:
            out.append(str(data[4] + ' - ' + data[1] + ' - ' + data[0] + ' - ' + data[5]))

    if out != []:
        for item in out:
            print(item, end='')
    else: print('Данного автора в этой библиотеке нет')
    print('\n')
