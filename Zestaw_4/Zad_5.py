def odwracanie_iteracyjnie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rekurencyjnie(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rekurencyjnie(L, left + 1, right - 1)

lista = [1, 2, 3, 4, 5, 6]
odwracanie_iteracyjnie(lista, 1, 4)
print(lista)
odwracanie_rekurencyjnie(lista, 1, 4)
print(lista)
