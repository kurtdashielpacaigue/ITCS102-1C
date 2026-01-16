import random
genshin_characters = [
    "Aether", "Lumine",
    "Amber", "Kaeya", "Lisa", "Jean", "Diluc",
    "Venti", "Xiangling", "Xingqiu", "Bennett", "Razor",
    "Zhongli", "Ningguang", "Keqing", "Ganyu", "Xiao", "Hu Tao",
    "Tartaglia", "Shenhe", "Yelan",
    "Raiden Shogun", "Kujou Sara", "Kamisato Ayaka", "Kamisato Ayato",
    "Yoimiya", "Sayu", "Thoma",
    "Nahida", "Nilou", "Cyno", "Alhaitham", "Dehya",
    "Furina", "Neuvillette", "Lyney", "Lynette", "Wriothesley"
]
hoyo=random.randint(0,37)
print(f'this is the number of your character:{hoyo}')
print("Your Character is:"+genshin_characters[hoyo])
