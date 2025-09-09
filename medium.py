price= eval(input("input item price"))
qty= eval(input("input item price"))

cost= price*qty

if cost >=100:
            discount= cost*0.10
            new_cost= cost-discount
            print("new cost original",cost,"with discount of 10%")
            print("new price is",new_cost)

else: 
       print("no discount applied nigga,Original price is",cost)
