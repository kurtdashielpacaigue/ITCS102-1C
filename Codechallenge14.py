Animelist = []  
while True:

    Anime = input("Enter your anime you weeb(or type 'exit' to terminate): ")
    if Anime.lower() == 'exit':
        print("Program ended weeb.")
        break
    Animelist.append(Anime)
    print(f"'{Anime}' has added.")

print("Your list:")
for Animee in Animelist:
    print(f"- {Animee}")
    
