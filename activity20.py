isdirty = True

while isdirty == True:
    wash_again = input("continue washing (yes/no) --->").lower()

    if wash_again == "yes":
        print("washing the clothes again...")
        continue
    else:
        print("washing stops now")
        break
