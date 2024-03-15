f = open('books.txt', encoding="utf-8").readlines()[1:]
classes = {}

for i in range(1, len(f)):
    data = f[i].split('%')
    item = data[4]
    if item not in classes:
        classes[item] = []
    classes[item].append(data[2])
    classes[item].append(float((data[5].strip()).replace(',', '.')))

data = []
for item in classes:
    data.append([item, classes[item][0], classes[item][1]])

for i in range(len(data)):
    for j in range(i, len(data)):
        if data[i][2] < data[j][2]:
            data[i], data[j] = data[j], data[i]

for i in range(3):
    print(data[i][0], '-', data[i][1], '-', data[i][2])

