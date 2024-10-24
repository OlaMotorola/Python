def sumy_sekwencji(sekwencje):
    return [sum(sekwencja) for sekwencja in sekwencje]

sekwencje = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

wynik = sumy_sekwencji(sekwencje)
print(wynik)
