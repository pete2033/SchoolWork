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
