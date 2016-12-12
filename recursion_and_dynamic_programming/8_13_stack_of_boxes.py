# 8.13 Stack of Boxes
# ==============================================================================================
# You have a stack of n boxes, with widths w, heights h, and depths d. The boxes cannot be
# rotated and can only be stacked on top of one another if each box in the stack is strictly
# larger than the box above it in width, height, and depth. Implement a method to compute the
# height of the tallest possible stack. The height of a stack is the sum of the heights of each
# box.
# ==============================================================================================
class Box(object):
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def can_be_above(self, bottom):
        return (bottom.height > self.height
                and bottom.width > self.width
                and bottom.depth > self.depth)


def build_stack(boxes, bottom_index):
    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        if boxes[i].can_be_above(bottom):
            height = build_stack(boxes, i)
            max_height = max(max_height, height)
    max_height += bottom.height
    return max_height


def solve_stack(boxes):
    boxes = sorted(boxes, reverse=True)
    max_height = 0
    for i in range(len(boxes)):
        height = build_stack(boxes, i)
        max_height = max(height, max_height)
    return max_height
