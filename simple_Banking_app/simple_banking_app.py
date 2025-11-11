class Bank:
    def __init__(self):
        self.bal = 0

    def check_balance(self):
        return self.bal   


    def deposit(self, amount):
        if amount < 0:
            return "Amount must be positive"
        self.bal += amount
        return self.bal


    def withdraw(self , val):
        if val<self.bal:
            return self.bal - val
        else:
            return "insufficient Balance"



