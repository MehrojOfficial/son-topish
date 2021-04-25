"""
</>
Date: 04.25.2021
Time: 1:20 PM
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Son topish o'yini"
</>
"""
from random import randint

def son_top(x=10):
    """Kompyuter o'ylagan sonni foydalanuvchi topadigan funksiya"""
    komp_son = randint(0,x)
    print(f"Keling, son topish o'yini o'ylaymiz!",
      f"\n0 dan {x} gacha oraliqda bitta son o'yladim. Topa olasizmi?")
    komp_natija = True
    komp_xato = 0
    while komp_natija:
        komp_check = int(input(">>> "))
        if komp_check == komp_son:
            komp_natija = False
        if komp_check != komp_son:
            if komp_check < komp_son:
                print(f"Xato. Men o'ylagan son {komp_check} dan katta. Yana harakat qiling")
                komp_xato += 1
            elif komp_check > komp_son:
                print(f"Xato. Men o'ylagan son {komp_check} dan kichik. Yana harakat qiling")
                komp_xato += 1
    if komp_natija == False:
        if komp_xato == 0:
            print(f"Tabriklayman! To'g'ri va aniq topdingiz! {komp_son} sonini o'ylagandim. \nQoyil, umuman xato qilmadingiz.")
        elif komp_xato != 0 and komp_xato < 4:
            print(f"Tabriklayman! To'g'ri topdingiz! {komp_son} sonini o'ylagandim. \nQoyil, bor-yo'g'i {komp_xato} marta adashdingiz xolos. ")
        elif komp_xato != 0 and komp_xato >= 4:
            print(f"Tabriklayman! To'g'ri topdingiz! {komp_son} sonini o'ylagandim. \n{komp_xato} marta adashdingiz.")
    return komp_xato

def pc_top():
    """Foydalanuvchi o'ylagan sonni kompyuter topadigan funksiya"""
    input(f"\nAna endi sizning navbatingiz. Biror son o'ylang va tayyor bo'lgach ENTER ni bosing ")
    player_natija = True
    player_xato = 0
    x=0
    y=10
    while player_natija:
        player_son = randint(x,y)
        player_check = input(f"Siz {player_son} ni o'yladingimi ? \nTo'g'ri bo'lsa T ni kiriting \nKattaroq son o'ylagan bo'lsangiz + ni kiriting \nKichikroq son o'ylagan bo'lsangiz esa - ni kiriting\n>>> ")
        if player_check == "T" or player_check == "t":
            player_natija = False
        elif player_check == "+":
            x = player_son + 1 
            player_xato += 1
        elif player_check == "-":
            y = player_son - 1
            player_xato += 1
    if player_natija == False:
        if player_xato == 0:
            print(f"\nSiz o'ylagan sonni topishda umuman adashmadim.")
        elif player_xato < 4:
            print(f"\nSiz o'ylagan sonni topishda bor-yo'g'i {player_xato} martagina adashdim.")
        elif player_xato >= 4:
            print(f"\nSiz o'ylagan sonni topishda {player_xato} marta adashdim.")
    return player_xato

first = son_top()
second = pc_top()

def winner():
    """Kim kam xato qilganiga qarab g'olibni e'lon qiluvchi funksiya"""
    if first < second:
        print(f"\nTabriklayman!!! Siz yutdingiz! \nMen {second} marta, siz esa {first} marta adashdingiz.")
    elif first > second:
        print(f"\nTabriklang !!! Men yutdim! \nMen {second} marta, siz esa {first} marta adashdingiz. ")
    elif first == second:
        print(f"\nDurrang! Ikkimiz ham yutdik! \nSiz ham, men ham {second} martadan xato qildik.")
