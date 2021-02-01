import csv
hypo = ("%","%","%","%","%","%")

with open("data11.csv") as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    print(readcsv)
    data = []
    print("\n The given training examples are ")
    for row in readcsv:
        print(row)
        if row[len(row) - 1].upper() == 'YES':
            data.append(row)
    print("\n The Positive examples are ")
    for x in data:
        print(x)
    print("\n")
    TotalExamples = len(data)
    i = 0
    j = 0
    k = 0
    print("Steps of Find-S are ", hypo)
    lists = []
    p = 0
    d = len(data[p]) - 1
    for j in range (d):
        lists.append(data[i][j])
    hypo = lists
    i = 1
    for i in range(TotalExamples):
        for k in range (d):
            if hypo[k] != data[i][k]:
                hypo[k] = '?'
                k = k + 1
            else:
                hypo[k]
    i += 1
    print("\n The Maximally specific Find-S is ")
    lists = []
    for i in range(d):
        lists.append(hypo[i])
    print(lists)