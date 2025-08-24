amount= eval(input("enter any amount to deposit"))

print("here is a breakdown of your amount of your deposited amount using the ph denominations")

libo= amount//1000
libo_sukli=amount % 1000

fiveh=libo_sukli//500
fiveh_sukli=libo_sukli% 500

twoh= fiveh_sukli//200
twoh_sukli=fiveh_sukli%200

oneh=twoh_sukli//100
oneh_sukli=twoh_sukli%100

fifty=oneh_sukli//50
fifty_sukli=oneh_sukli%50

twenty=fifty_sukli//20
twenty_sukli=fifty_sukli%20

ten=twenty_sukli//10
ten_sukli=twenty_sukli%10

five=ten_sukli//5
five_sukli=ten_sukli%5

one=five_sukli//1
one_sukli=five_sukli%1

print(libo,"-1000")
print(libo_sukli)
print(fiveh,"-500")
print(fiveh_sukli)
print(twoh,"-200")
print(twoh_sukli)
print(oneh,"-100")
print(oneh_sukli)
print(fifty,"-50")
print(fifty_sukli)
print(twenty,"-20")
print(twenty_sukli)
print(ten,"-10")
print(ten_sukli)
print(five,"-5")
print(five_sukli)
print(one,"-1")
print(one_sukli)
