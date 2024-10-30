def flatten(sequence):
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))

