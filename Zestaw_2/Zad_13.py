#Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

line = "Ala ma kota,\n kot ma Alę."
words = line.split()
total_length = sum(len(word) for word in words)
print("Łączna długość wyrazów:", total_length)
