import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high=[]
low=[]

for row in data:
    if row[-1] != '' and row[-2] != '':
        date = row[0].split('-')
        if 1983 <= int(date[0]):
            if date[1] == '08' and date[2] == '30':
                high.append(float(row[-1]))
                low.append(float(row[-2]))

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('내 생일의 기온 변화 그래프')
plt.plot(high, 'hotpink', label='high')
plt.plot(low, 'skyblue', label='low')
plt.legend()
plt.show()