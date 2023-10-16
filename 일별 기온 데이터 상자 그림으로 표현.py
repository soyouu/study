import csv 
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

day=[]
for i in range(31):
    day.append([])

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()