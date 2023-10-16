import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
feb=[]
sep=[]

for row in data:
    month = row[0].split('-')
    if row[-1] != '':
        if month[1] == '02':
            feb.append(float(row[-1]))
        if month[1] == '09':
            sep.append(float(row[-1]))

plt.hist(feb, bins=100, color='r', label='Feb')
plt.hist(sep, bins=100, color='b', label='Sep')
plt.legend()
plt.show()