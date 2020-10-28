from matplotlib import pyplot as plt
import numpy as np
import csv

####### 1

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


plt.plot(ages_x, py_dev_y, label="Python")
plt.plot(ages_x, js_dev_y, label="JS")
plt.plot(ages_x, dev_y, linestyle='--', label="All Devs")

plt.title("1. Средняя зарплата программиста")
plt.xlabel("Возраст")
plt.ylabel("Зарплата в USD")

plt.legend()
plt.tight_layout()
plt.show()

####### 2

fig1, (ax1, ax2) = plt.subplots(2, 1)

slices = [1405919000, 	1377736000, 329957441, 266911900, 219098526]
labels = ['Китай', 'Индия', 'США', 'Индонезия', 'Пакистан']

ax1.pie(slices, labels=labels, startangle=90, wedgeprops={'edgecolor':'black'}, autopct='%1.1f%%')
ax1.set_title("2. Cамые населенные страны мира")

ax2.barh(labels, slices)
ax2.set_ylabel("Страны")
ax2.set_xlabel("Население")

plt.tight_layout()
plt.show()

####### 3

fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

x = np.arange(0, 4*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

ax1.plot(x, y1)
ax1.set_ylabel("y")
ax1.set_title("sin(x)")

ax2.plot(x, y2)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("cos(x)")

plt.tight_layout()
plt.show()

####### 4

with open("yakutsk_2019.csv", encoding="cp1251") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=";")
    
    average_temp = []
    month = 12
    sum = 0.0
    cnt = 0
    for row in reader:
        newMonth = int(row["Date"][3:5])
        if newMonth == month:
            sum += float(row["Temp"])
            cnt += 1
        else:
            month = newMonth
            average_temp.append(sum/cnt)
            sum = float(row["Temp"])
            cnt = 1
    average_temp.append(sum/cnt)

average_temp.reverse()

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

plt.barh(months, average_temp)
plt.title("4. Средние температуры по месяцам")
plt.ylabel("Месяц")
plt.xlabel("Средняя температура")

plt.tight_layout()
plt.show()
