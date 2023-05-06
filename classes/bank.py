class  Bank:
    amount =  4
    def __init__(self,name,number,branch):
        self.name = name
        self.number = number
        self.branch = branch
    def withdraws (self,withdraw):
        self.withdraw = withdraw
        return f"the fruits are{self.withdraw}"
    def depoosit(self,deposit):
        self.deposits= deposit
        return f"she brought {self.deposit}"
    def price(self,balance):
        self.balance= balance
        return f"hello your total is {self.balance}"
