import numpy as np
import matplotlib.pyplot as plt
import csv

#1

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


plt.figure(0)
plt.title("Average Salary")
plt.plot(ages_x, py_dev_y, 'o--r', label = "Python")
plt.plot(ages_x, js_dev_y, 'v:b', label = 'Js')
plt.plot(ages_x, dev_y, 's-.g', label = 'SimpleDev')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()


#2

China = 1405919000
India = 1377736000
USA = 329957441
Indonesia = 266911900
Pakistan = 219098526

plt.figure(1)
plt.title("World population")
coll1 = plt.bar(1, China, label = 'China')
coll1 = plt.bar(2, India, label = 'India')
coll1 = plt.bar(3, USA, label = 'USA')
coll1 = plt.bar(4, Indonesia, label = 'Indonesia')
coll1 = plt.bar(5, Pakistan, label = 'Pakistan')
plt.legend()


plt.figure(2)
vals = [1405919000, 1377736000, 329957441, 266911900, 219098526]
labels = ["China", "India", "USA", "Indonesia", "Pakistan"]
pie1 = plt.pie(vals, labels=labels)
plt.legend()


#3

x = np.arange(0,4*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
f2, (ax1,ax2) = plt.subplots(1, 2, sharex=True)
ax1.title.set_text('Sin')
ax2.title.set_text('Cos')
ax1.plot(x,y1)
ax2.scatter(x,y2)
plt.show()

#4

with open("yakutsk_2019.csv", encoding="cp1251") as csv_file:
    File = csv.DictReader(csv_file, delimiter=";")
    
    average = []
    month = 12
    sum = 0.0
    count = 0

    
    for row in File:
        next_Month = int(row["Date"][3:5])
        if (next_Month == month):
            sum += float(row["Temp"])
            count += 1
        else:
            month = next_Month
            average.append(sum/count)
            sum = float(row["Temp"])
            count = 1
    average.append(sum/count)
average.reverse()
allmonth = ["January", "February", "March", "April", "May", "June", "Jule", "August", "September", "October", "November", "December"]



plt.barh(allmonth, average)
plt.title("Average temperature, monthes in year")
plt.xlabel("Average temperature")
plt.ylabel("Month")
plt.show()



