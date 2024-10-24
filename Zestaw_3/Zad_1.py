#Kod jest błędny składniowo, w pythonie niepotrzebne są średniki na końcu linii, mogą być użyte, aby oddzielić wiele zmiennych znajdujących się w jednej linii. Również nawias w warunku if nie jest potrzebny. Nie powoduje to jednak błędnych wyników.
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

#Kod ma błąd składniowy, ponieważ nie można umieszczać instrukcji warunkowej if na tej samej linii co pętla for. W Pythonie po dwukropku musi wystąpić blok kodu, który jest wcięty i znajduje się w nowej linii.
for i in "axby": if ord(i) < 100: print (i)

#Kod jest poprawny składniowo
for i in "axby": print(ord(i) if ord(i) < 100 else i)

