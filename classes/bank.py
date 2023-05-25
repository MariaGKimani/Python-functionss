class  Bank:
    def __init__(self,name,balance,branch,deposits,withdrawals,loan_balance):
        self.name = name
        self.balance=balance
        self.branch = branch
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    def  check_balance(self):
        return f"{self.balance}"
    def deposit(self, amount):
        self.balance += amount
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)
        print(f"Deposited {amount} into the account.")
    def transacts(self):
        for transaction in self.deposits:
            print(transaction)
    def withdrawal(self, amount):
        self.balance -= amount
        transactions = {
            "amount": amount,
            "narration": "Withdraw"
        }
        self.withdrawals.append(transactions)
        print(f"withdrawed {amount} from the account.")
    def transacts(self):
        for transactions in self.withdrawals:
            print(transactions)
    def borrow_loan(self,amount):
        if self.balance == 0 and amount > 100 and len(self.loan_balance >= 10):
            self.loan_balance += amount;
    def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")

    def borrow_loan(self,loan_amount):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if self.loan_balance==0 and loan_amount>100 and len(self.deposits)>=10 and loan_amount > total_deposits / 3:
           return
        self.loan_balance+=loan_amount
        self.balance+=loan_amount
        
    def repay_loan(self,amount):
        self.loan_balance-=amount
        if amount>self.loan_balance:
            extra=self.loan_balance-amount
            self.balance+=extra

 

# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
   
bank = Bank("KCB",20000,"Thika branch",10000,40000,0)
bank.check_balance()
bank.deposit(20)
bank.withdrawal(50)

bank.transacts()


# Add a new method  print_statement which combines
# both deposits and withdrawals into one list and, 
# using a for loop, prints each transaction
#  in a new line like this
# deposit - 1000
# withdrawal - 500





