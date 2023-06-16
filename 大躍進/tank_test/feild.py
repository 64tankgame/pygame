from setting import *
import random

map = []
block_size = 20
map_row = int(HEIGHT/block_size)
map_col = int(WIDTH/block_size)
for row in range(map_row):
    map.append([])
    for col in range(map_col):
        if col == 0 or col == map_col -1:
            map[row].append(1)
        map[row].append(0)

item_type = [0,1]

for row in range(1,map_row - 3):
    for col in range(1,map_col - 1):
        map[row][col] = random.choices(item_type,weights=[10,1])[0]

