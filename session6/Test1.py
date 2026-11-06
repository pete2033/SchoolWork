import os
import matplotlib.pyplot as plt


print("current folder",os.getcwd())
print("current posix interface",os.name)
print("folders in this dir",os.listdir())
print("current PID",os.getpid())


departments = ['HR','IT','Sales','Finance']
employees= [10,25,15,12]

plt.bar(departments, employees, color="blue")

plt.show()

ages=[22,25,30,30,31,34,35,36,40,41,42,45,46,50,51,52]

plt.hist(ages, bins=5, color="lightgreen",edgecolor="black")

plt.show()
