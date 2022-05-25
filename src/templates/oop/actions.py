from typing import Union
import random

import mapping
import player
import items


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(dungeon, player): # completar
    # completar
    raise NotImplementedError


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    # completar
    raise NotImplementedError

def move (dungeon: mapping.Dungeon, player: player.Player, key):
    dic = {'s': (0,1), 'w': (0,-1), 'a': (-1,0), 'd': (1,0)}
    loc = player.loc()
    new_loc = (loc[0]+dic[key][0], loc[1]+dic[key][1])
    if (0<=new_loc[0]< dungeon.columns and 0<=new_loc[1]< dungeon.rows):
        if dungeon.is_walkable(new_loc):
            player.move_to(new_loc)
        if is_breakable(dungeon, player, new_loc):
            player.move_to(new_loc)

def is_breakable (dungeon: mapping.Dungeon, player: player.Player, xy)->bool:
    if xy == mapping.WALL and has_pickaxe:
        return True
    return False

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    xy = player.loc()
    item = dungeon.get_items(xy)
    return item
