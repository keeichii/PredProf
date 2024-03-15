f = open('books.txt', encoding="utf-8").readlines()
fout = open('books_new.csv',  'w', encoding="utf-8")
fout.write('authors,ratings_authors\n')
classes = {}

for i in range(1, len(f)):
    data = f[i].split('%')
    for item in data[2].split(','):
        if item not in classes:
            classes[item] = []
        classes[item].append(float((data[5].strip()).replace(',', '.')))

data = []
for i in classes:
    data.append([i, round(sum(classes[i]) / len(classes[i]), 2)])
    fout.write(','.join([i, str(round(sum(classes[i]) / len(classes[i]), 2))]))
    fout.write('\n')
data = sorted(data, key=lambda x: x[1])
print(data[0][0], '-', data[0][1])


