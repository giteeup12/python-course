# get load details
money_owed = float(input("how much money do you owe, in dollars?\n")) # 50,000
apr = float(input('what is the rate\n'))
payment = float(input('what will your monthly payment be in dollars?\n'))
months = int(input('how many months\n '))
# divid by 100 then by 12
monthly_rate = apr/100/12
for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    money_owed = money_owed - payment
    print("paid",  payment, "of which", interest_paid, "was interest",end= ' ')
    print("now I owe", money_owed)