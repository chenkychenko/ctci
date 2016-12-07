# 5.8 Draw Line
# ==============================================================================================
# A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to
# be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
# be split across rows). The height of the screen, of course, can be derived from the length of
# the array and the width. Implement a function that draws a horizontal line from (x1, y) to
# (x2, y).
# ==============================================================================================
def draw_line(screen, width, x1, x2, y):
    height = len(screen) / width
    # get which byte to toggle
    row_start_index = y * width
    col_start_index = x1 / 8
    start_byte = row_start_index + col_start_index
    
    col_end_index = x2 / 8 + 1
    end_byte = row_start_index + col_end_index
    
    screen[start_byte] = set_starting_bits(x1 % 8, screen[start_byte])
    screen[end_byte] = set_ending_bits(x2 % 8, screen[end_byte])
    set_middle_bytes(start_byte + 1, end_byte - 1, screen)
    
def set_starting_bits(start_index, byte):
    return byte & ((1 << (8 - start_index)) - 1)

def set_ending_bits(end_index, byte):
    return byte & ~((1 << (8 - end_index - 1)) - 1)

def set_middle_bytes(start_index, end_index, byte_array):
    i = start_index
    while i <= end_index:
        byte_array[i] |= 0xFF