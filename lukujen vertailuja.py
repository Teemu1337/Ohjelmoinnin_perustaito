ikä = int(input("Syötä ikä: "))

if ikä < 0 or ikä > 150:
    print("Virheellinen ikä!")
elif ikä < 6:
    print("Esikoululainen")
elif ikä == 14:
    print("Haastava ikä")

elif ikä == 15:
    print("Olet skibidi")
elif 16 <= ikä <= 18:
    print("Lähes aikuinen")
elif 18 < ikä < 30:
    print("Olet täysi-ikäinen, muttet vielä keski-iän kriisissä")
elif 30 <= ikä < 45:
    print("Olet keski-iässä")
elif 45 < ikä < 65:
    print("Vielä ehtii ennen eläkettä!")
else:
    print("Olet eläkeläinen")