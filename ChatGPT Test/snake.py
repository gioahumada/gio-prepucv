import os
from random import randint
import readchar

# CONSTANTS
POS_X = 0
POS_Y = 1

TRAINERS_POSITION = [[25, 5], [4, 10], [25, 15], [4, 17]]
TRAINER_1 = [25, 5]
TRAINER_2 = [4, 10]
TRAINER_3 = [25, 15]
TRAINER_4 = [4, 17]

SUPER_POTIONS = [[14, 7], [14, 12], [14, 17]]

VIDA_INICIAL_PIKACHU = 150
VIDA_INICIAL_DRAGONITE = 100
VIDA_INICIAL_MACHAMP = 100
VIDA_INICIAL_CHARIZARD = 120
VIDA_INICIAL_ALAKAZAM = 120
TAMANO_BARRA_VIDA = 20

vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_dragonite = VIDA_INICIAL_DRAGONITE
vida_actual_machamp = VIDA_INICIAL_MACHAMP
vida_actual_charizard = VIDA_INICIAL_CHARIZARD
vida_actual_alakazam = VIDA_INICIAL_ALAKAZAM

"""
vida_actual_enemy_pokemon = None
VIDA_INICIAL_ENEMY_POKEMON = None
enemy_pokemon_name = None
move_1_name = None
move_1 = 0
move_2_name = None
move_2 = 0
"""

my_position = [2, 2]
end_game = False
died = False

# Map
obstacle_definition = """\
##############################
#                            #
#                            #
#                            #
######################       #
######################       #
#                            #
#                            #
#                            #
#       ######################
#       ######################
#                            #
#                            #
#                            #
######################       #
######################       #
#                            #
#                            #
#                            #
##############################\
"""

# Create obstacles map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGTH = len(obstacle_definition)

# Main loop
while len(TRAINERS_POSITION) > 0:
    os.system("cls")
    if end_game:
        break
    # Draw map
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            trainer_in_cell = None
            potion_in_cell = None

            # Draw potions
            for potion in SUPER_POTIONS:
                if potion[POS_X] == coordinate_x and potion[POS_Y] == coordinate_y:
                    char_to_draw = "SP"
                    potion_in_cell = potion

            # Draw trainers
            for trainer in TRAINERS_POSITION:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = " ✪"
                    trainer_in_cell = trainer

            # Draw character
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " ☻"

                if potion_in_cell:
                    vida_actual_pikachu += 100
                    if vida_actual_pikachu > VIDA_INICIAL_PIKACHU:
                        vida_actual_pikachu = VIDA_INICIAL_PIKACHU
                    SUPER_POTIONS.remove(potion_in_cell)
                    print("\n")
                    print("Te has encontrado una super pocion, tu pokemon ha recuperado 100ps.")

                    barra_vida_pikachu = int((vida_actual_pikachu / VIDA_INICIAL_PIKACHU) * TAMANO_BARRA_VIDA)
                    print("Pikachu:     [{}{}] ({}/{})".format("*" * barra_vida_pikachu,
                                                               " " * (TAMANO_BARRA_VIDA - barra_vida_pikachu),
                                                               vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                    input("Enter para continuar...")

                if trainer_in_cell:
                    TRAINERS_POSITION.remove(trainer_in_cell)
                    print("\n")
                    print("Te has encontrado con un entrenador pokemon.")
                    input("Enter para continuar...")
                    os.system("cls")

                    # Identify the trainer
                    if my_position[POS_X] == TRAINER_1[POS_X] and my_position[POS_Y] == TRAINER_1[POS_Y]:
                        enemy_pokemon_name = "Dragonite"
                        vida_actual_enemy_pokemon = vida_actual_dragonite
                        VIDA_INICIAL_ENEMY_POKEMON = VIDA_INICIAL_DRAGONITE
                        move_1_name = "garra dragon"
                        move_2_name = "cometa draco"
                        move_1 = 15
                        move_2 = 22
                    elif my_position[POS_X] == TRAINER_2[POS_X] and my_position[POS_Y] == TRAINER_2[POS_Y]:
                        enemy_pokemon_name = "Machamp"
                        vida_actual_enemy_pokemon = vida_actual_dragonite
                        VIDA_INICIAL_ENEMY_POKEMON = VIDA_INICIAL_DRAGONITE
                        move_1_name = "rompe roca"
                        move_2_name = "puño drenaje"
                        move_1 = 10
                        move_2 = 17
                    elif my_position[POS_X] == TRAINER_3[POS_X] and my_position[POS_Y] == TRAINER_3[POS_Y]:
                        enemy_pokemon_name = "Charizar"
                        vida_actual_enemy_pokemon = vida_actual_dragonite
                        VIDA_INICIAL_ENEMY_POKEMON = VIDA_INICIAL_DRAGONITE
                        move_1_name = "lanza llamas"
                        move_2_name = "vuelo"
                        move_1 = 22
                        move_2 = 10
                    else:
                        enemy_pokemon_name = "Alacazam"
                        vida_actual_enemy_pokemon = vida_actual_dragonite
                        VIDA_INICIAL_ENEMY_POKEMON = VIDA_INICIAL_DRAGONITE
                        move_1_name = "psiquico"
                        move_2_name = "confusion"
                        move_1 = 25
                        move_2 = 17

                    # Combat
                    while vida_actual_pikachu > 0 and vida_actual_enemy_pokemon > 0:
                        # Se desenvuelve el combate
                        # Turno de pokemon enemigo
                        print("Turno de {}".format(enemy_pokemon_name))
                        ataque_enemy_pokemon = randint(1, 2)
                        if ataque_enemy_pokemon == 1:
                            print("{} ataca con {}".format(enemy_pokemon_name, move_1_name))
                            vida_actual_pikachu -= move_1
                        else:
                            print("{} ataca con {}".format(enemy_pokemon_name, move_2_name))
                            vida_actual_pikachu -= move_2

                        # Barra de vida
                        if vida_actual_enemy_pokemon < 0:
                            vida_actual_enemy_pokemon = 0

                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0

                        barra_vida_pikachu = int((vida_actual_pikachu / VIDA_INICIAL_PIKACHU) * TAMANO_BARRA_VIDA)
                        print("Pikachu:     [{}{}] ({}/{})".format("*" * barra_vida_pikachu,
                                                                   " " * (TAMANO_BARRA_VIDA - barra_vida_pikachu),
                                                                   vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_vida_enemy_pokemon = int(
                            (vida_actual_enemy_pokemon / VIDA_INICIAL_ENEMY_POKEMON) * TAMANO_BARRA_VIDA)
                        print("{}:    [{}{}] ({}/{})".format(enemy_pokemon_name, "*" * barra_vida_enemy_pokemon,
                                                             " " * (TAMANO_BARRA_VIDA - barra_vida_enemy_pokemon),
                                                             vida_actual_enemy_pokemon, VIDA_INICIAL_ENEMY_POKEMON))

                        input("Enter para continuar...\n\n")
                        os.system("cls")

                        # Turno Pikachu
                        print("Turno de Pikachu")

                        ataque_pikachu = None

                        while ataque_pikachu not in ["B", "T"]:
                            ataque_pikachu = input(
                                "¿Que ataque deseas realizar? [B]ola Voltio, [T]rueno: ")

                        if ataque_pikachu == "B":
                            print("Pikachu ataca con Bola Voltio")
                            vida_actual_enemy_pokemon -= 20
                        elif ataque_pikachu == "T":
                            print("Pikachu ataca con Trueno")
                            vida_actual_enemy_pokemon -= 22

                        # Barra de vida
                        if vida_actual_enemy_pokemon < 0:
                            vida_actual_enemy_pokemon = 0

                        if vida_actual_pikachu < 0:
                            vida_actual_pikachu = 0

                        barra_vida_pikachu = int((vida_actual_pikachu / VIDA_INICIAL_PIKACHU) * TAMANO_BARRA_VIDA)
                        print("Pikachu:     [{}{}] ({}/{})".format("*" * barra_vida_pikachu,
                                                                   " " * (TAMANO_BARRA_VIDA - barra_vida_pikachu),
                                                                   vida_actual_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_vida_enemy_pokemon = int(
                            (vida_actual_enemy_pokemon / VIDA_INICIAL_ENEMY_POKEMON) * TAMANO_BARRA_VIDA)
                        print("{}:    [{}{}] ({}/{})".format(enemy_pokemon_name, "*" * barra_vida_enemy_pokemon,
                                                             " " * (TAMANO_BARRA_VIDA - barra_vida_enemy_pokemon),
                                                             vida_actual_enemy_pokemon, VIDA_INICIAL_ENEMY_POKEMON))

                        input("Enter para continuar...\n\n")
                        os.system("cls")

                    if vida_actual_pikachu > vida_actual_enemy_pokemon:
                        print("Pikachu gana")
                        input("Enter para continuar...\n\n")
                        os.system("cls")
                    else:
                        print("{} gana".format(enemy_pokemon_name))
                        end_game = True
                        died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    if end_game:
        break

    # Ask user where he wants to move
    # direction = input("Donde te quieres mover? [wasd]: ")
    direction = readchar.readchar()
    print(direction)

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGTH]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGTH]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position
if died:
    print("GAME OVER")
else:
    print("Felicidades!!! Has derrotado a todos los entrenadores. Has Ganado.")