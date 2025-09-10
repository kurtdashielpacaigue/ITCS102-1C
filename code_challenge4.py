print("Choose your mango")
print("Choose your genre")
print("1. hentai")
print("2. action")
print("3. romcom")
choice = input("Choice 1/2/3: ")

if choice == "1":
    hentai1 = "hentai"
    print("\nYou selected:", hentai1)

    print("1. short")
    print("2. medium")
    print("3. long")
    far = input("Choices are 1/2/3: ")

    if far == "1":
        short1 = "short"
        print("\nYou selected:", short1)
        print("Choose year")
        print("1. 2000")
        print("2. 2010")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour hentai is Boku no Pico (2000)")
        elif decade == "2":
            print("Your hentai is Eromanga Sensei (2010)")
        else:
            print("CHANGE UR LIFE")

    elif far == "2":
        medium1 = "medium"
        print("\nYou selected:", medium1)
        print("Choose year")
        print("1. 2000")
        print("2. 2010")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour hentai is La Blue Girl (2000)")
        elif decade == "2":
            print("Your hentai is High School DxD (2010)")
        else:
            print("CHANGE UR LIFE")
    
    elif far == "3":
        long1 = "long"
        print("\nYou selected:", long1)
        print("Choose year")
        print("1. 2000")
        print("2. 2010")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour hentai is Bible Black (2000)")
        elif decade == "2":
            print("Your hentai is Monster Musume (2010)")
        else:
            print("CHANGE UR LIFE")

elif choice == "2":
    action1 = "action"
    print("\nYou selected:", action1)

    print("1. short")
    print("2. medium")
    print("3. long")
    far = input("Choices are 1/2/3: ")

    if far == "1":
        short1 = "short"
        print("\nYou selected:", short1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour action is Attack on Titan (2010)")
        elif decade == "2":
            print("Your action is Hellsing Ultimate (2000)")
        else:
            print("THERES NO ANIME FOR YOU SORRY SIR")

    elif far == "2":
        medium1 = "medium"
        print("\nYou selected:", medium1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour action is Fullmetal Alchemist: Brotherhood (2010)")
        elif decade == "2":
            print("Your action is Cowboy Bebop (2000)")
        else:
            print("THERES NO ANIME FOR YOU SORRY SIR")
    
    elif far == "3":
        long1 = "long"
        print("\nYou selected:", long1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour action is Bleach (2010)")
        elif decade == "2":
            print("Your action is Naruto (2000)")
        else:
            print("THERES NO ANIME FOR YOU SORRY SIR")

elif choice == "3":
    romcom1 = "romcom"
    print("\nYou selected:", romcom1)

    print("1. short")
    print("2. medium")
    print("3. long")
    far = input("Choices are 1/2/3: ")

    if far == "1":
        short1 = "short"
        print("\nYou selected:", short1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour romcom is Teasing Master Takagi-san (2010)")
        elif decade == "2":
            print("Your romcom is Lovely Complex (2000)")
        else:
            print("JUST LIKE GIRLS WE DON'T HAVE ANY")

    elif far == "2":
        medium1 = "medium"
        print("\nYou selected:", medium1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour romcom is My Teen Romantic Comedy SNAFU (2010)")
        elif decade == "2":
            print("Your romcom is His and Her Circumstances (2000)")
        else:
            print("JUST LIKE GIRLS WE DON'T HAVE ANY")
    
    elif far == "3":
        long1 = "long"
        print("\nYou selected:", long1)
        print("Choose year")
        print("1. 2010")
        print("2. 2000")
        decade = input("Choice 1/2: ")

        if decade == "1":
            print("\nYour romcom is Clannad (2010)")
        elif decade == "2":
            print("Your romcom is Kare Kano (2000)")
        else:
            print("JUST LIKE GIRLS WE DON'T HAVE ANY")

else:
    print("Invalid choice. Please choose a valid genre.")