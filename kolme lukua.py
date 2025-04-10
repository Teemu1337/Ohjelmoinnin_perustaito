luku1 = int(input("Syötä 1. luku"))
luku2 = int(input("Syötä 2. luku"))
luku3 = int(input("Syötä 3. luku"))

if luku1 <= luku2 <= luku3:
    pienin, keskimmäinen, suurin = luku1, luku2, luku3
elif luku1 <= luku3 <= luku2:
    pienin, keskimmäinen, suurin = luku1, luku3, luku2
elif luku2 <= luku1 <= luku3:
    pienin, keskimmäinen, suurin = luku2, luku1, luku3
elif luku2 <= luku3 <= luku1:
    pienin, keskimmäinen, suurin = luku2, luku3, luku1
elif luku3 <= luku1 <= luku2:
    pienin, keskimmäinen, suurin = luku3, luku1, luku2
else:
    pienin, keskimmäinen, suurin = luku3, luku2, luku1   

print(f"Järjestys: {pienin}, {keskimmäinen}, {suurin}")