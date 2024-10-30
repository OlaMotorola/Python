def make_ruler(n):
    top_line = "|"
    for i in range(n):
        top_line += "....|"

    bottom_line = ""
    for i in range(n + 1):
        bottom_line += f"{i:<5}"

    return top_line + "\n" + bottom_line


def make_grid(rows, cols):
    horizontal_line = "+" + ("---+" * cols)

    vertical_line = "|" + ("   |" * cols)

    grid = ""
    for _ in range(rows):
        grid += horizontal_line + "\n" + vertical_line + "\n"
    grid += horizontal_line

    return grid

print(make_ruler(12))
print(make_grid(2, 4))

