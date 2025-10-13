laon= eval(input("enter po amount -->"))
laon_period = eval(input("enter loan period in years"))
laon_period *= 12
balance = laon
principal =laon / laon_period
print("PAYMENT SCHEDULE")
print("MONTH\t|monthly payment\t|interest\t|principal\t|remaining balance\|")
for i in range(1,laon_period +1,1):
    balance -=principal
    interest = balance *0.03
    monthly = principal + interest
    print(f"{i}\t\t{round(principal,2)}\t\t\t{round(balance,2)}\t\t\t{round(interest,2)}\t\t\t{round(monthly,2)}")
