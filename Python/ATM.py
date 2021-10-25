withdraw,balance = map(str,input().split())
withdraw = int(withdraw)
balance = float(balance)
print(withdraw,balance)
if withdraw%5==0 and withdraw+0.5<=balance:
    print(balance-withdraw-0.5)
else:
    print(balance)