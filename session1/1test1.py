def FindInList(toFind, goodList):
    goodList=goodList.split(",")
    print(goodList)
    print(type(goodList))
    goodList=tuple(goodList)
    print(goodList)
    print(type(goodList))
    counter=0
    while counter < (len(goodList)-1):
        if toFind==goodList[counter]:
            return True
            print("t")
            break
        else:
            counter=counter+1       



print("hello world")
print("how are you?")
print("i am \t fine")#the \t character adds a tab
print("you sure?\nyes")#and the \n adds anew line
userFeeling=input("How are you feeling, user?\n")
print("you are feeling",userFeeling+". \nIs this good or bad?")
UserFeelingOpinion=input("")
good=FindInList(UserFeelingOpinion, "good,g")
if good==True:
    print("glad to hear it")
else:
    print("oh")
