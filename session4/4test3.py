data1=[10,20,30,40,50]
data2=[17,22,43,41,1]
data3=[10,20,30,40,50]

counter=0
incount=0
while counter < 4:
    if data1[counter] in data3:
        incount=incount+1
    counter=counter+1
if incount==5:
    print("lists are the same")
else:
    print("nope")

k=5
m=2
print(k&5)
print(k|m)
print(k^m)

mylist=[10,2,3,4,5]
y=10
z=20
if y in mylist and z in mylist:
    print("yup")
else:
    print("nope")