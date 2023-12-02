import readchar
import os
import random

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 11

my_position = [1, 1]

tail_len = 0
tail = []

map_objects = []

while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0,MAP_WIDTH), random.randint(0,MAP_HEIGHT)]

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)

while (1):
    print("+" + ("-" * MAP_WIDTH*3) + "+")
    for i in range(MAP_HEIGHT):
        print("|", end="")

        for k in range(MAP_WIDTH):
            char = " "
            for obj in map_objects:
                if obj[POS_X] == k and obj[POS_Y] == i:
                    char = "*"
            
            for tail_piece in tail:
                if tail_piece[POS_X] == k and tail_piece[POS_Y] == i:
                    char = "@"

            if my_position[POS_X] == k and my_position[POS_Y] == i:
                char = "@"
                if [k, i] in map_objects:
                    map_objects.remove([k, i])
                    tail_len += 1

            print(" {} ".format(char), end="")
        print("|")

    print("+" + ("-" * MAP_WIDTH*3) + "+")

    direction = readchar.readchar()

    if direction == "w":
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
        tail.insert(0, my_position.copy())
        tail = tail[:tail_len]
    elif direction == "s":
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
        tail.insert(0, my_position.copy())
        tail = tail[:tail_len]
    elif direction == "a":
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
        tail.insert(0, my_position.copy())
        tail = tail[:tail_len]
    elif direction == "d":
        my_position[POS_X] +=1
        my_position[POS_X] %= MAP_WIDTH
        tail.insert(0, my_position.copy())
        tail = tail[:tail_len]
    elif direction == "q":
        break

    os.system('clear')
