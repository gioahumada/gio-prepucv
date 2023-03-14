import readchar
import os

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

while True:

    print('+'+'-'*(MAP_WIDTH*3) + '+')

    for cordinate_y in range(MAP_HEIGHT):
        print('|', end='')
        for cordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                print(' @ ', end='')
            else:
                print('   ', end='')
        print('|')

    print('+'+'-'*(MAP_WIDTH*3) + '+')

    #ask user where he wants to go 

    # direction = input('¿Donde te quieres mover? [WASD]: ')
    direction = readchar.readchar()

    if direction == 'w':
        my_position[POS_Y] -=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 's':
        my_position[POS_Y] +=1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == 'a':
        my_position[POS_X] -=1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'd':
        my_position[POS_X] +=1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == 'q':
        break

    os.system('cls')