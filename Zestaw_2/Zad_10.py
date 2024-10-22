#Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = "Ala ma kota,\nkot ma Alę."
word_count = len(line.split())
print("Liczba wyrazów:", word_count)