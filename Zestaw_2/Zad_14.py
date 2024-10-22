#Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

line = "Ala ma kota,\n kot ma Alę."
words = line.split()

longest_word = max(words, key=len)
longest_length = len(longest_word)

print("Najdłuższy wyraz:", longest_word)
print("Długość najdłuższego wyrazu:", longest_length)
