#Kirjoita ohjelma, joka pyytää käyttäjältä päivän (1–31), kuukauden (1–12) ja vuoden. Tarkista, onko 
# annettu päivämäärä kelvollinen. Huomioi seuraavat asiat:
# • Kuukaudet, joissa on 30 päivää: huhtikuu (4), kesäkuu (6), syyskuu (9), marraskuu (11).
# • Helmikuussa (2) on normaalisti 28 päivää, mutta karkausvuonna 29 päivää.
# • BONUS: Kun saat ohjelman toimimaan voit huomioida myös karkausvuoden päivien
#lukumäärän laskemisessa. Karkausvuosi on vuosi, joka on jaollinen 4:llä, mutta ei 100:lla,
#paitsi jos se on jaollinen 400:lla.

päivä = int(input("Anna päivä"))
kuukausi = int(input("Anna kuukausi"))
vuosi = int(input("Anna vuosi"))

kuukauden_päivät = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}