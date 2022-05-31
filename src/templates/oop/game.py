#!/usr/bin/env python3
import time
import mapping
import magic
from gnome import Gnome
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
    player = Human (name, level.find_free_tile())
    pickaxe = PickAxe ('pickaxe', ')')

    # initial locations may be random generated
    gnome = Gnome ('gnome',level.find_free_tile())

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    dungeon.add_item(pickaxe, 1)

    turns = 0
    key = ''
    pickaxe_tool = False
    while dungeon.level >= 0 and key != 'q':
        turns += 1
        # render map
        dungeon.render(player)

        # read key
        key = magic.read_single_keypress()[0]
        if key == 'p':
            item_list = actions.pickup(dungeon, player)
            for it in item_list:
                if isinstance(it, PickAxe):
                    pickaxe_tool = True
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            actions.move(dungeon, player, key, pickaxe_tool)
        
        #no funciona
        if dungeon.get_items(player.loc()) == mapping.STAIR_UP:
            actions.climb_stair(dungeon, player)
        if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
            actions.descend_stair(dungeon, player)

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
