#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.

line = "Ala ma kota,\n kot ma Alę."
words = line.split()

first_letters = ''.join([word[0] for word in words])
last_letters = ''.join([word[-1] for word in words])

print("Pierwsze znaki:", first_letters)
print("Ostatnie znaki:", last_letters)
