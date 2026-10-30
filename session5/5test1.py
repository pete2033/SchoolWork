class BankAccount():
    def __init__(self, HolderName, AccountNumber, SortCode, ExpirationDate, HolderAddress, HolderPhoneNum, Balance):
        self.HolderName=HolderName
        self.AccountNumber=AccountNumber
        self.SortCode=SortCode
        self.ExpirationDate=ExpirationDate
        self.HolderAddress=HolderAddress
        self.HolderPhoneNum=HolderPhoneNum
        self.Balance=Balance

    def deposit(self, amount):
        print("current is",self.Balance)
        self.Balance+=amount
        print("new is",self.Balance)

    def withdraw(self, amount):
        print("current balance", self.Balance)
        if self.Balance -amount <0:
            print("nuh uh")
            return
        else:
            self.Balance-=amount
        print("new is",self.Balance)

    def ShowBalance(self):
        print(self.Balance)

    def AccountInfo(self):
        print("account holder name is",self.HolderName)
        print("account number is",self.AccountNumber)
        print("sort number is",self.SortCode)
        print("balance is",self.Balance)
    def InfoTwo(self):
        print("account holder name is",self.HolderName)
        print("holder address is",self.HolderAddress)
        print("phone number is",self.HolderPhoneNum)
        print("expiry date is",self.ExpirationDate)       


    def RegisterAddress(self, Address):
        self.HolderAddress=Address

    def RegisterPhone(self, Number):
        self.HolderPhoneNum=Number

def CreateCard(NewHolder):
        accountNew=BankAccount(NewHolder, 234567891, 111,"tomorrow","none","none",0)
        return accountNew

account1=BankAccount("J. SMITH",123456789,999,"yesterday","none","none",0)
account1.deposit(20)
account1.withdraw(30)
account1.ShowBalance()
account1.AccountInfo()
account2=CreateCard("J DOE")
account2.RegisterAddress("Lane Street")
account2.RegisterPhone(8765456764)
print(account2.HolderPhoneNum)
print(account2.HolderAddress)
account2.AccountInfo()
account2.InfoTwo()

print("hello world")



        