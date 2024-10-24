def rysuj_prostokat(rows, cols):
    pozioma_linia = "+---" * cols + "+\n"
    pionowa_linia = "|   " * cols + "|\n"

    prostokat = ""
    for _ in range(rows):
        prostokat += pozioma_linia
        prostokat += pionowa_linia
    prostokat += pozioma_linia

    return prostokat

print(rysuj_prostokat(2, 4))