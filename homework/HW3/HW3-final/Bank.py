from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
    
    def addAccount(self, accountType):
        # your code
        if hasattr(self, "SAVINGS") and hasattr(self, "CHECKING"):
            return
        else:
            if accountType == AccountType.SAVINGS:
                self.SAVINGS = 0
            else: 
                self.CHECKING = 0

    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS:
            return self.SAVINGS
        else: 
            return self.CHECKING
        
    def deposit(self, accountType, amount):
        if amount < 0:
            print("Withdrawal cannot be negative")
            return
        elif accountType == AccountType.SAVINGS:
            self.SAVINGS = self.SAVINGS + amount
        else: 
            self.CHECKING = self.CHECKING + amount

    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS:
            if amount > self.SAVINGS:
                print("Withdrawal cannot exceed account balance")
                return
            elif amount < 0:
                print("Withdrawal cannot be negative")
                return
            else:
                self.SAVINGS = self.SAVINGS - amount
        else:
            if amount > self.CHECKING:
                print("Withdrawal cannot exceed account balance")
                return 
            else:
                self.CHECKING = self.CHECKING - amount

    def __str__(self):
        part1 = 'Owner: ' + self.owner + ", "
        if self.SAVINGS:
            part2 = 'Type of account: Savings'
        else:
            part2 = 'Type of account: Checking'
        return(str(part1+part2))

