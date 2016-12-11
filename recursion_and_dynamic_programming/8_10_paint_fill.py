# 8.10 Paint Fill
# ==============================================================================================
# Implement the paint fill function that one might see on many image editing programs. That is,
# given a screen (represented by a two-dimentional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.
# ==============================================================================================
class Color:
    Red, Blue, Yellow = range(3)


def do_paint_fill(screen, row, col, color):
    if screen[row][col] == color:
        return False
    return paint_fill(screen, row, col, screen[row][col], color)


def paint_fill(screen, row, col, ocolor, ncolor):
    # if out of bounds:
    if row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0]):
        return
    if screen[row][col] == ocolor:  # if not the color we want
        screen[row][col] = ncolor
        paint_fill(screen, row + 1, col, ocolor, ncolor)  # pixel up
        paint_fill(screen, row - 1, col, ocolor, ncolor)  # pixel down
        paint_fill(screen, row, col + 1, ocolor, ncolor)  # pixel right
        paint_fill(screen, row, col - 1, ocolor, ncolor)  # pixel left


screen = [[Color.Red, Color.Blue, Color.Blue],
          [Color.Blue, Color.Blue, Color.Yellow],
          [Color.Blue, Color.Blue, Color.Blue]]

for i in screen:
    print i

do_paint_fill(screen, 1, 1, Color.Yellow)
for i in screen:
    print i