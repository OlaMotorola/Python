def rysuj_miarke(dlugosc):
    linia_kreski = ""
    for i in range(dlugosc):
        linia_kreski += "|...."
    linia_kreski += "|\n"

    linia_liczby = ""
    for i in range(dlugosc + 1):
        linia_liczby += f"{i:<5}"

    miarka = linia_kreski + linia_liczby

    return miarka


print(rysuj_miarke(12))