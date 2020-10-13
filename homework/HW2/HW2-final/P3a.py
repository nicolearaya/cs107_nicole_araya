def outer(balance):
    def withdrawal(w):
        if w > balance:
            return
        else:
            new_bal = balance - w
            return new_bal
    return withdrawal

init_balance = 500
withdrawal_amount = 50
new_withdrawal_amount = 100
wd = outer(init_balance)
print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))
print("this does not work because the closure captures the initial balance but never updates it, so consecutive withdrawals are taken without the balance dropping to reflect these changes.")