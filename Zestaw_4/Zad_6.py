def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)
        else:
            total += item
    return total

sequence = [1, 2, [3, 4, [5, 6]], (7, 8)]
print(sum_seq(sequence))
