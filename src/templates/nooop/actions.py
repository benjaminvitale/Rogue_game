from typing import List, Tuple

import config
import human


def move(level: List[List[int]], character: dict, direction: str):
    """
    Moves an entity from a given location to the appropriate location based on the game level and equipment for the
    character.

    :param level: Game floor in which the character is moving.
    :param character: Dictionary representing the character.
    :param direction: UP, DOWN, LEFT or RIGHT command (configured in characters.py)

    :return: Tuple with coordinates where the character would move in the given direction
    without accounting enemies or hazards.
    Still, moving towards walls make characters without a PICK stand and not move.
    """
    # completar
    if character == config.UP:
        move_up()
    raise NotImplementedError


def move_to(level: List[List[int]], entity: dict, location: Tuple[int, int]):
    # entity = {'location: (r,c) , 'face': 'X'}
    raise NotImplementedError


def move_up(level: List[List[int]], entity: dict):
    '''
    Moves an entity a step up

    :param level: dungeon level map
    :param entity: entity to move {'location': (int,int), 'face': "X"}

    :returns: No return value, map is modified in-place
    '''
    #Completar
    row_before = entity['location'][0]
    row_after = entity['location'][0] -1
    col = entity['location'][1]
    
    level[row_before][col] = config.SPACE
    entity['location'] = (row_after,col)
    level[row_after][col] = entity['face']


def move_left(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_down(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError


def move_right(level: List[List[int]], entity: dict):
    # completar
    raise NotImplementedError

def is_walkable ():
    #completar
    raise NotImplementedError
