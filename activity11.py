temp= eval(input("enter tempreature outside --->"))

if temp >= 1 and temp<=20:
        print("temperature is considered cold")
elif temp >=21 and temp <=30:
        print("temperature is considered as moderately cold")
elif temp >=31 and temp <=37:
        print("temperature is considered as normal temp")
elif temp >=38 and temp <=45:
        print("temperature is considered as hot")
elif temp >=45 and temp <=50:
        print("temperature is considered boiling hot ")
elif temp >=51:
        print("temperature is considered as dangerous temp")
elif temp <=1:
        print("temperature is considered as freezing")



else:
    print("invalid temperature")
