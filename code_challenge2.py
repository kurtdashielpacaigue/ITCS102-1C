cash= eval(input("enter amount to deposit:"))
print("here is a breakdown of your deposit:")

thou= cash//1000
cash = cash- thou*1000

five= cash//500
cash = cash- five *500

two= cash//200
cash= cash- two*200

one= cash//100
cash=cash-one*100

fifty= cash//50
cash= cash-fifty*50

twenty= cash//20
cash= cash-twenty*20

ten= cash//10
cash= cash- ten*10

fiveee= cash//5
cash= cash-fiveee*5

oneee= cash//1
cash=cash-fiveee*1

print(thou,"-1000")
print(five,"-500")
print(two,"-200")
print(one,"-100")
print(fifty,"-50")
print(twenty,"-20")
print(ten,"-10")
print(fiveee,"-5")
print(oneee,"-1")
