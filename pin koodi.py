oikeapin = "3120"

pin = int(input("Anna PIN-koodi"))

while pin != oikeapin:
    print("Väärä pin. Yritä uudestaan")
    pin = input("Anna PIN-koodi")

print("PIN on oikein")