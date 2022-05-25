#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from items import Item, PickAxe
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    name = input("Enter name: ")
    player = Human (name, (20,9))
    pickaxe = PickAxe ('pickaxe', ')')

    # initial locations may be random generated
    gnomes = ''

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    dungeon.add_item(pickaxe, 1)

    turns = 0
    key = ''
    while dungeon.level >= 0 and key != 'q':
        turns += 1
        # render map
        dungeon.render(player)

        # read key
        key = magic.read_single_keypress()[0]
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            actions.move(dungeon, player, key)

        if key == 'p':
            it = actions.pickup(dungeon, player)
            if it != []:
                pickaxe_tool = True
        

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
