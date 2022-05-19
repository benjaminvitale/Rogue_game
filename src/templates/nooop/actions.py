from typing import List, Tuple

import config
import human

EMPTY = 0

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
    loc = character['location'] + direction
    if is_walkable (level, loc):
        if direction == config.UP:
            move_up()
        elif direction == config.DOWN:
            move_down
        elif direction == config.LEFT:
            move_left()
        elif direction == config.RIGHT:
            move_right()
        



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
    row= entity['location'][0]
    col_before = entity['location'][1]
    col_after = entity['location'][1]-1
    
    level[row][col_before] = config.SPACE
    entity['location'] = (row,col_after)
    level[row][col_after] = entity['face']


def move_down(level: List[List[int]], entity: dict):
    row_before = entity['location'][0]
    row_after = entity['location'][0] + 1
    col = entity['location'][1]
    
    level[row_before][col] = config.SPACE
    entity['location'] = (row_after,col)
    level[row_after][col] = entity['face']


def move_right(level: List[List[int]], entity: dict):
    row= entity['location'][0]
    col_before = entity['location'][1]
    col_after = entity['location'][1] + 1
    
    level[row][col_before] = config.SPACE
    entity['location'] = (row,col_after)
    level[row][col_after] = entity['face']

def is_walkable (level: List[List[int]], location: Tuple[int,int]):
    if location == EMPTY:
        return True
    return False
    raise NotImplementedError
