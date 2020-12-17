# -*- coding: utf-8 -*-
"""
Day 17 of Advent of Code 2020


Tom Kite - 17/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer
from itertools import product


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def get_iteration_ranges(cube_locs):
    ranges = []
    for elem in cube_locs:
        break
    for i in range(len(elem)):
        ranges.append(range(min(cube_locs, key=lambda c: c[i])[i]-1,
                            max(cube_locs, key=lambda c: c[i])[i]+2))
    return ranges


def process_initial_layer(layer, dimensions):
    cube_locs = set()
    counts_dict = {}
    for j, row in enumerate(layer):
        for i, col in enumerate(row):
            if col == '#':
                coord = tuple([i, j] + [0]*(dimensions-2))
                cube_locs.add(coord)
                counts_dict = add_to_counts_dict(coord, counts_dict)
    return cube_locs, counts_dict


def add_to_counts_dict(coords_in, counts_dict):
    for coord in product(*get_iteration_ranges([coords_in])):
        if coords_in == coord:
            continue
        if coord not in counts_dict.keys():
            counts_dict[coord] = 1
        else:
            counts_dict[coord] += 1
    return counts_dict


def evolve_pocket_dim(cube_locs, counts_dict):
    new_cube_locs = set()
    new_counts_dict = {}
    ranges = get_iteration_ranges(cube_locs)

    for coord in product(*ranges):
        if coord in counts_dict.keys():
            count = counts_dict[coord]
        else:
            count = 0
        if coord in cube_locs:
            if count == 2 or count == 3:
                new_cube_locs.add(coord)
                new_counts_dict = \
                    add_to_counts_dict(coord, new_counts_dict)
        elif count == 3:
            new_cube_locs.add(coord)
            new_counts_dict = \
                add_to_counts_dict(coord, new_counts_dict)
    return new_cube_locs, new_counts_dict


def part1(filename):
    data = readfile(filename)
    cube_locs, counts_dict = process_initial_layer(data, 3)
    for _ in range(6):
        cube_locs, counts_dict = evolve_pocket_dim(cube_locs, counts_dict)
    print("After 6 cycles there are {} active cubes."
          .format(len(cube_locs)))
    return


def part2(filename):
    data = readfile(filename)
    cube_locs, counts_dict = process_initial_layer(data, 4)
    for i in range(6):
        cube_locs, counts_dict = evolve_pocket_dim(cube_locs, counts_dict)
    print("After 6 cycles there are {} active cubes."
          .format(len(cube_locs)))
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day17.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day17.dat")
    timer.checkpoint_hit()

    timer.end_hit()
