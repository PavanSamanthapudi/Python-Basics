class OurBankAccount:
    def __init__(self, name, account_balance):
        self.name = name
        self.amount = account_balance
        print(f"{self.name} has Amount : {self.amount}")
    def withdrawAmount(self,amount):
        if amount > self.amount:
            print("Insufficient Balance")
        else:
            self.amount -= amount
        
        return self.amount

user_1 = OurBankAccount("Pavan", 2000)
balance = user_1.withdrawAmount(1000)
print(balance)
