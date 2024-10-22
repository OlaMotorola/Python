#Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

L = [1, 12, 123, 1234]
result = ''.join(str(num) for num in L)
print(result)
