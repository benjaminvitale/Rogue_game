from typing import Union
import random

import mapping
import player
from magic import read_single_keypress as keypress
from mapping import AIR


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


def move_up(dungeon: mapping.Dungeon, player: player.Player):
    loc = player.loc()
    new_loc = (loc[0],loc[1]-1)
    if dungeon.is_walkable(new_loc):
        player.move_to(new_loc)
    

def move_down(dungeon: mapping.Dungeon, player: player.Player):
    loc = player.loc()
    new_loc = (loc[0],loc[1]+1)
    if dungeon.is_walkable(new_loc):
        player.move_to(new_loc)


def move_left(dungeon: mapping.Dungeon, player: player.Player):
    loc = player.loc()
    new_loc = (loc[0]-1,loc[1])
    if dungeon.is_walkable(new_loc):
        player.move_to(new_loc)


def move_right(dungeon: mapping.Dungeon, player: player.Player):
    loc = player.loc()
    new_loc = (loc[0]+1,loc[1])
    if dungeon.is_walkable(new_loc):
        player.move_to(new_loc)


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError

loc = [20,9]
d = mapping.Dungeon(25,80)
p = player.Player('sere', loc)
p.face = "@"

d.render(p)
direction = keypress()
while direction[0] == 'w' or direction[0] == 'a' or direction[0] == 's' or direction[0] == 'd':
    if direction[0] == 'w':
        move_up(d, p)
    if direction[0] == 'a':
        move_left(d,p)
    if direction[0] == 's':
        move_down(d,p)
    if direction[0] == 'd':
        move_right(d,p)
    
    p.face = "@"
    d.render(p)
    direction = keypress()

