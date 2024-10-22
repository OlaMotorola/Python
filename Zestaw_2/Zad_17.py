#Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().


line = "Ala ma kota,\n kot ma Alę."
words = line.split()

sorted_alpha = sorted(words)
sorted_by_length = sorted(words, key=len)

print("Alfabetycznie:", sorted_alpha)
print("Według długości:", sorted_by_length)
