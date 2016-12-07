# 8.2 Robot in a Grid
# ==============================================================================================
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot
# can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top
# left to the bottom right.
# ==============================================================================================
def path_helper(rows, cols):
    grid = [[0] * cols] * cols
    return find_robot_path(grid, 0, 0, (rows-1, cols-1))
    
def find_robot_path(grid, x, y, dest):
    if x >= len(grid[0]) or y >= len(grid) or grid[x][y] == 1:
        return False # cannot go here
    if x == dest[0] and y == dest[1]:
        return True
    return find_robot_path(grid, x+1, y, dest) or find_robot_path(grid, x, y+1, dest)

grid = [[0,1,1],
        [0,0,1],
        [0,0,0]]
# print find_robot_path(grid, 0, 0, (2,2))


def get_robot_path(grid, x, y, dest, cur_path, all_paths):
    if x >= len(grid[0]) or y >= len(grid) or grid[x][y] == 1:
        return # cannot go here
    cur_path.append((x,y))
    if x == dest[0] and y == dest[1]:
        all_paths.append(cur_path)
        return
    (get_robot_path(grid, x+1, y, dest, cur_path[:], all_paths) 
            or get_robot_path(grid, x, y+1, dest, cur_path[:], all_paths))
    cur_path.pop()

def robot_path_helper(grid):
    all_paths = []
    get_robot_path(grid, 0, 0, (2,2), [], all_paths)
    return all_paths

paths = robot_path_helper(grid)
print paths