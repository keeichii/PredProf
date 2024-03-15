f = open('books.txt', encoding="utf-8").readlines()[1:]
fout = open('top_10_authors.csv',  'w', encoding="utf-8")
classes = {}


full_data = []
for i in range(1, len(f)):
    data = f[i].split('%')
    for item in data[2].split(', '):
        if item not in classes:
            classes[item] = 0
        classes[item] += 1

for item in sorted(classes.items(), reverse=True, key=lambda x: x[1])[:10]:
    fout.write(item[0] + '\n')
fout.close()