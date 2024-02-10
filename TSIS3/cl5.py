class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def refill(self,i):
        self.balance= self.balance + i 
        print(self.balance)
    
    def withdrawal(self,h):
        if h>self.balance:
            print("Error")
        else:
            self.balance=self.balance - h
            print("Money left", self.balance)

k=Account("Jeff",6700)

k.refill(8900)

k.withdrawal(3000)

k.withdrawal(20000)

