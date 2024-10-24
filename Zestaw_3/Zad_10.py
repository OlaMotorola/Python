#Ręczne definiowanie
roman_to_arabic1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

#Przy użyciu funkcji dict()
roman_to_arabic2 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

#Przy użyciu krotek
roman_to_arabic3 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])


def roman2int(roman):
    roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_to_arabic[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


