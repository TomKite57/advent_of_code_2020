# -*- coding: utf-8 -*-
"""
Day 24 of Advent of Code 2020


Tom Kite - 24/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


direc_dict = {'e':  (2, 0),
              'ne': (1, 1),
              'nw': (-1, 1),
              'w':  (-2, 0),
              'sw': (-1, -1),
              'se': (1, -1)}


def readfile(filename):
    with open(filename, 'r') as file:
        data = [process_line(x.strip()) for x in file]
    return data


def process_line(line):
    coord = (0, 0)
    letters = ''
    for char in line:
        letters += char
        if letters in direc_dict:
            coord = add(coord, direc_dict[letters])
            letters = ''
    return coord


def add(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])


def tile_colour(coord, coord_list):
    if coord_list.count(coord) % 2 != 0:
        return 'black'
    return 'white'


class tile:
    def __init__(self, coord, colour):
        self.coord = coord
        self.colour = colour
        self.neighbours = set([add(coord, x) for x in direc_dict.values()])

    def evolve(self, black_list):
        count = sum([1 for c in self.neighbours if c in black_list])
        if self.colour == 'black':
            if count in [0, 3, 4, 5, 6]:
                self.colour = 'white'
        else:
            if count == 2:
                self.colour = 'black'


def get_black_list(tile_list):
    return set([t.coord for t in tile_list if t.colour == 'black'])


def trim_tile_list(tiles):
    new_tiles = set([t for t in tiles if t.colour == 'black'])
    current_coords = set([t.coord for t in tiles if t.colour == 'black'])
    for c in current_coords:
        for direc in direc_dict.values():
            new_c = add(c, direc)
            if new_c not in current_coords:
                new_tiles.add(tile(new_c, 'white'))
    return new_tiles


def part1(filename):
    data = readfile(filename)
    answer = sum([1 for x in data if tile_colour(x, data) == 'black'])
    print("There are {} black tiles in total.".format(answer))


def part2(filename):
    data = readfile(filename)
    unique_coords = set(data)
    tiles = set([tile(c, tile_colour(c, data)) for c in unique_coords])

    for i in range(100):
        tiles = trim_tile_list(tiles)
        black_list = get_black_list(tiles)
        for t in tiles:
            t.evolve(black_list)

    answer = len(get_black_list(tiles))
    print("There are {} black tiles in total.".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day24.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day24.dat")
    timer.checkpoint_hit()

    timer.end_hit()
