#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

L = [1, 12, 123, 2, 23]
formatted_numbers = ''.join([str(num).zfill(3) for num in L])
print("Bloki trzycyfrowe:", formatted_numbers)
