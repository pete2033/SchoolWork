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


departments = ['HR','IT','Sales','Finance']
employees= [10,25,15,12]
colors=["gold","skyblue","lightgreen","lightcoral"]
plt.pie(employees, labels=departments, colors=colors,autopct="%1.1f%%",startangle=90)
plt.axis("equal")
plt.title("Employee Percentage by Department")
plt.show()

x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.subplot(2,2,1)
plt.bar(x,y)
plt.title("Bar Chart")
plt.subplot(2,2,2)
plt.hist(y)
plt.title("Histogram")
plt.subplot(2,2,3)
plt.pie(y, labels=x)
plt.title("Pie Chart")
plt.subplot(2,2,4)
plt.plot(x,y, marker="o")
plt.title("Line Graph")

plt.tight_layout()
plt.show()
