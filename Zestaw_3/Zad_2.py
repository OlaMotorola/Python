#Problem z tym kodem polega na tym, że metoda sort() działa in-place, co oznacza, że sortuje listę L bez zwracania żadnej wartości. Zamiast tego zwraca wartość None. Dlatego przypisanie L = L.sort() powoduje, że po wykonaniu tej operacji zmienna L będzie miała wartość None, a nie posortowaną listę.
L = [3, 5, 4] ; L = L.sort()

#Kod spowoduje błąd składniowy, ponieważ liczba wartości po prawej stronie przypisania (3 wartości: 1, 2, 3) nie zgadza się z liczbą zmiennych po lewej stronie (2 zmienne: x i y). Python wymaga, aby liczba zmiennych po lewej stronie odpowiadała liczbie wartości po prawej stronie.
x, y = 1, 2, 3

#Kod spowoduje błąd typu (TypeError). Dzieje się tak, ponieważ X jest krotką, a krotki są niemutowalne (immutable), co oznacza, że nie można zmieniać ich elementów po utworzeniu.
X = 1, 2, 3 ; X[1] = 4

#Kod spowoduje błąd indeksu (IndexError). Dzieje się tak, ponieważ próbuje zostać przypisana wartość do indeksu, który nie istnieje w liście.
X = [1, 2, 3] ; X[3] = 4

#Kod spowoduje błąd atrybutu (AttributeError), ponieważ obiekt typu str nie ma metody append().
X = "abc" ; X.append("d")

#Kod spowoduje błąd podczas próby uruchomienia, ponieważ funkcja map() wymaga co najmniej dwóch argumentów dla funkcji pow()
L = list(map(pow, range(8)))



