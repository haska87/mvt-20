# 1
import matplotlib.pyplot as plt

plt.style.use('seaborn')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

plt.plot(ages_x, py_dev_y, label="Python")
plt.plot(ages_x, js_dev_y, label="JavaScript")
plt.plot(ages_x, dev_y, label="All Devs")

plt.title("Средняя зарплата программистов")
plt.xlabel("Возраст")
plt.ylabel("Зарплата")

plt.legend()
plt.tight_layout()
plt.show()


#2
import matplotlib.pyplot as plt

plt.style.use('seaborn')

countries = ["Китай", "Индия", "США", "Индонезия", "Пакистан"]
population = [1405919000, 1377736000, 329957441, 266911900, 219098526]
countries.reverse()
population.reverse()

plt.barh(countries, population)
plt.title("Самые населённые страны мира")
plt.xlabel("Страны")
plt.ylabel("Население")

plt.legend()
plt.tight_layout()
plt.show()

plt.pie(population, labels=countries, autopct='%1.1f%%')
plt.title("Самые населённые страны мира")
plt.xlabel("Страны")
plt.ylabel("Население")

plt.legend()
plt.tight_layout()
plt.show()


#3
import matplotlib.pyplot as plt
import math as m

plt.style.use('seaborn')

x = []
sinx = []
cosx = []
h = 0.1

for i in range(-100, 100):
    x1 = i * h
    x.append(x1)
    sinx.append(m.sin(x1))
    cosx.append(m.cos(x1))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(x, sinx, label="Sin(x)")
ax1.set_ylabel("y")

ax2.plot(x, cosx, label="Cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.legend()
plt.tight_layout()
plt.show()


#4
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv("yakutsk_2019.csv", sep=";", encoding='cp1251')

time = data["Date"].to_dict()
date = list(time.keys())
temperature = list(time.values())

months = ["12"]
temp = [0]
days = [0]
lastMonth = 0
for i in range(len(date)):
    m = date[i][3:5]
    if months[lastMonth] != m:
        months.append(m)
        temp.append(0)
        days.append(0)
        lastMonth += 1
    temp[lastMonth] += temperature[i]
    days[lastMonth] += 1

for i in range(len(temp)):
    temp[i] /= days[i]

plt.barh(months, temp)
plt.title("Среднемесячная температура в Якутске")
plt.xlabel("Температура")
plt.ylabel("Месяц")

plt.legend()
plt.tight_layout()
plt.savefig("graph.png")

plt.show()
