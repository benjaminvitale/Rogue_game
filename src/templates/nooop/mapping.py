from operator import ne
import random
from typing import List, Tuple, Set
from copy import copy


import config


def render(tiles: List[List[int]],
           player: dict, gnome: dict):
    """
    Draw the map onto the terminal, including player, items and gnome.

    :param tiles: dungeon level, created with level(). Is a list of lists of ints.
    :param player: player location in the map (dict).
    :param gnome: gnome location in the map (dict).

    :return: None, map is rendered on screen.
    """
    print("-" + "-" * len(tiles[0]) + "-")
    for i, row in enumerate(tiles):
        print("|", end="")
        for j, cell in enumerate(row):
            if (i, j) == player["location"]:
                print(player["face"], end='')
            elif gnome and (i, j) == gnome["location"]:
                print(gnome["face"], end='')
            elif cell == 0:
                print(config.SPACE, end='')
            elif cell == 1:
                print(config.WALL_ROCK, end='')
            else:
                print(cell, end='')
        print("|")
    print("-" + "-" * len(tiles[0]) + "-")

def level(rows: int,
          columns: int) -> List[List[int]]:
    """
    Creates a dungeon level

    :param rows: is the number of rows for the level (int).
    :param columns: is the number of columns for the level (int).

    :return: level map
    """
    tiles = [[1] * 12 + [0] * (columns - 24) + [1] * 12]  # 0=air 1=rocks
    for row in range(1, rows):
        local = tiles[row - 1][:]
        for i in range(2, columns - 2):
            vecindad = local[i - 1] + local[i] + local[i + 1]
            local[i] = random.choice([0]*100+[1]*(vecindad**3*40+1))
        tiles.append(local)

    return tiles

def dungeon(rows: int, columns: int, levels: int = 3) -> List[List[List[int]]]:
    """
    Creates a dungeon

    :param rows: is the number of rows for each level (int).
    :param columns: is the number of columns for each level (int).
    :param levels: the number of levels that the dungeon should have (int).

    :return: dungeon
    """
    dungeon_levels = [level(rows, columns) for _ in range(levels)]

    up = []
    down = []
    for i in range(levels - 1):
        # Up stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        up.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_UP

        # Down stairs
        x = random.randint(0, rows - 1)
        y = random.randint(0, columns - 1)
        down.append((x, y))
        dungeon_levels[i][x][y] = config.LADDER_DOWN

    # Last Up stair
    x = random.randint(0, rows - 1)
    y = random.randint(0, columns - 1)
    up.append((x, y))
    dungeon_levels[-1][x][y] = config.LADDER_UP

    return dungeon_levels


def add_item(dungeon: List[List[List[int]]], item: dict, level: int):
    """
    Places items on a newly generated map. Unreachability of positions is not checked by the function.

    :param dungeon: dungeon to be modified.
    :param item: item to add
    :param level: floor number

    :return: No return value, map is modified in-place.
    """
    x, y = item["location"]
    dungeon[level][x][y] = item["face"]


def is_tile(level: List[List[int]],
            location: Tuple[int, int],
            tile: str) -> bool:
    """
    Checks if a given location of the level map is of a give tile type, por example, a stair up '<'.

    :param level: dungeon level map (list of lists of ints)
    :param location: coordinates of the tile to check (tuple of ints)
    :param tile: type of tile to see (all tiles are 1 character---strings of lenth 1)

    :return: True if it is, False otherwise.
    """
    x, y = location
    return level[x][y] == tile


def set_tile(level: List[List[int]],
             location: Tuple[int, int],
             tile: str):
    """
    Set a given location of a level map with the specified tile.

    :param level: dungeon level map (list of lists of ints)
    :param location: coordinates of the tile to check (tuple of ints)
    :param tile: type of tile to see (all tiles are 1 character---strings of lenth 1)

    :return: No return value, map is modified in-place.
    """
    x, y = location
    level[x][y] = tile


def is_free(level: List[List[int]],
            xy: Tuple[int, int],
            visited: Set) -> bool:
    """
    Check if a given location is free of other entities and if it is usable.
    
    :param level: dungeon level map (list of lists of ints)
    :param xy: location in the map (tuple of ints (row, column))
    :param visited: locations already used (set)
    
    :returns: True if it is, False otherwise
    """
    if xy in visited:
        return False
    if level[xy[0]][xy[1]] != 0:
        return False
    return True


def are_connected(level: List[List[int]],
                  initial: Tuple[int, int],
                  end: Tuple[int, int]) -> bool:
    """
    Check if there is walkable path between initial location and end location.
    
    :param level: dungeon level map (list of lists of ints)
    :param initial: starting location (tuple of ints)
    :param end: ending location (tuple of ints)

    :return: True if there is, False otherwise
    """
    
    return search_path (level, initial, end, set())

def search_path (level: List[List[int]], initial: Tuple[int,int], end: Tuple[int,int], visited: Set)-> bool:
    '''
    Checks if there is a walkable path between inital location and end location

    :param level: dungeon level map (list of lists of ints)
    :param initial: starting location (tuple of ints)
    :param end: ending location (tuple of ints)
    :param visited: locations already visited (set)

    :returns: True if there is, False otherwise
    '''
    if initial == end:
        return True

    path = False
    for loc in get_neighbours (level, initial):
        if is_free (level, loc, visited):
            visited.add (loc)
            copy_visited = copy(visited)
            path = search_path (level, initial, end, copy_visited)
        if path:
            break

    return path

def get_neighbours (level: List[List[int]], xy: Tuple[int,int]) ->List[Tuple[int,int]]:
    '''
    Given a map, it searchs for all the possible points an object could move

    :param level: dungeon level map (List of lists of ints)
    :param xy: point in the map (tuple (row, column))

    :returns neighbours: List with all the neighbours of the point (only includes 4, not diagonals)
    '''

    directions = {'d': (0,1) , 'a': (0,-1), 'w': (1,0), 's': (-1,0)}
    rows = len(level)
    col = len(level[0])
    neighbours = []
    for deltas in directions.values():
        possible = (xy[0]+deltas[0], xy[1] + deltas[1])
        if is_in_map(rows, col, possible):
            neighbours.append (possible)

    return neighbours

def is_in_map (rows: int, cols: int, point: Tuple[int,int]) -> bool:
    '''
    Given a specific location, it checks if the point is inside the parameters

    :param rows: rows of a map
    :param cols: columns of a map
    :param point: point in the form of Tuple(row,col)

    :returns: True if it is inside, False if it is not
    '''

    if point[0] < 0 or point[0] >= rows:
        return False
    if point[1] < 0 or point[1] >= cols:
        return False

    return True


def get_path(level: List[List[int]],
             initial: Tuple[int, int],
             end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Return a sequence of locations between initial location and end location, if it exits."""
    # completar
    raise NotImplementedError

# Estas lineas son para ir viendo en la terminal que pasa
d = dungeon(config.ROWS , config.COLUMNS)
add_item(d, {'location': (9,5), 'face': config.SWORD}, 1)
set_tile(d[1], (9,7), '(')
r = render (d[1], {'location': (10,20), 'face': config.JUGADOR} , {'location' : (20 , 40), 'face': config.GNOME})

'''
mapa = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]]
print(are_connected (mapa,(0,0),(3,4)))
'''
#las funcion de are_connected no funciona bien, despues voy a chequiar xq esta dando mal
