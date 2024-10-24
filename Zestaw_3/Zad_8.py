def wspolne_i_rozne_elementy(seq1, seq2):
    set1 = set(seq1)
    set2 = set(seq2)

    wspolne = list(set1 & set2)
    wszystkie = list(set1 | set2)

    return wspolne, wszystkie


seq1 = [1, 2, 3, 4, 4, 5]
seq2 = [4, 5, 6, 7, 8]
wspolne, wszystkie = wspolne_i_rozne_elementy(seq1, seq2)
print("Wspólne elementy:", wspolne)
print("Wszystkie elementy:", wszystkie)
