# BANKAPP
# As a bank customer, I want to withdraw money from my account so that I can access my funds when needed.

# As a bank customer, I want to see my current account balance so that I can keep track of my finances.

# As a bank customer, I want to see the total balance in the bank so that I can know how much money the bank is holding.

# As a bank customer, I want to be able to create a savings account with my account number, account holder name, and initial balance.

# As a savings account holder, I want my account to earn interest based on the account balance.

# As a savings account holder, I want to deposit money into my account, earn interest, and see my updated account balance.

# As a bank, I want to log all transactions made by customers to maintain a record of account activity.

# As a bank, I want to provide transaction logs for customers so that they can verify their recent account activities.

# As a bank, I want to ensure that customers cannot withdraw more money than they have in their accounts and receive a notification if they attempt to do so.

# As a bank, I want to provide a user-friendly interface for customers to interact with their accounts, making it easy for them to manage their finances.

#### Tools#
#1. Class
#2. INSTANCE
#3. class atributes and methods
#4. Instance attributes and methods
#5. inheritance
#6. decorater

#####Notes
#An instance is an indiv object

class Bank_Accounts:
    def __init__(self,acc_number,acc_name,balance): 
        self.acc_number=acc_number
        self.acc_name=acc_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
    
    def check_balance(self):
        print(f'Hello {self.acc_name}, Your current balance is ${self.balance}')
#object
mary=Bank_Accounts(12242303,'Mary',700)
mary.deposit(200)
mary.check_balance()