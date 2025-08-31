name = input("please input your name --->")
fare = eval(input("fare--->"))
isStudent= input("are you currently a student (yes?no"))

if isStudent.lower() == "yes":
      discount = fare * 0.2
      new_fare = fare - discount
      print("Hi" ,name,"your discount is",discount,"your newfare is",new_fare)
else:
       print("Hi",name,"you're only eligible  for regular price")
