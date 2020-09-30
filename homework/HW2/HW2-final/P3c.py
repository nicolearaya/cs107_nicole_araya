def outer(balance):
    def withdrawal(w):
        nonlocal balance
        if w > balance:
            return
        else:
            balance = balance - w
            return balance
    return withdrawal

init_balance = 500
wd = outer(init_balance)
withdrawal_amount = 50
new_withdrawal_amount = 100
print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))
print("this does not work because the inner fuction does not have direct access to manipulating state of the outer function (balance). Names in the inner function (local scope) can not interfere with names in the global scope.")