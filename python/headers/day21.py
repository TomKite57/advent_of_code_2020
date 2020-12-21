# -*- coding: utf-8 -*-
"""
Day 21 of Advent of Code 2020


Tom Kite - 21/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer
from copy import deepcopy


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [process_line(line) for line in file]
    return lines


def process_line(line):
    line = line.strip().strip(')')
    line = line.split(' (contains ')
    line[0] = set(line[0].split(' '))
    line[1] = set(line[1].split(', '))
    return line


def find_single_ingredients(pos_dict):
    rval = set()
    for val in pos_dict.values():
        if len(val) == 1:
            rval = rval.union(val)
    return rval


def remove_single_pos(pos_dict):
    new_pos_dict = deepcopy(pos_dict)
    ingredients_to_remove = find_single_ingredients(new_pos_dict)
    if len(ingredients_to_remove):
        for val in new_pos_dict.values():
            if len(val) != 1:
                val -= ingredients_to_remove
    if pos_dict != new_pos_dict:
        return remove_single_pos(new_pos_dict)
    return new_pos_dict


def part1(filename):
    data = readfile(filename)
    allergens = set.union(*[x[1] for x in data])
    ingredients = set.union(*[x[0] for x in data])
    pos_dict = {}
    for al in allergens:
        pos_dict[al] = set.intersection(*[x[0] for x in data if al in x[1]])

    pos_dict = remove_single_pos(pos_dict)

    safe_ingredients = ingredients - set.union(*pos_dict.values())
    answer = 0
    for line in data:
        for ing in safe_ingredients:
            if ing in line[0]:
                answer += 1
    print("Safe ingredients appear {} times.".format(answer))


def part2(filename):
    data = readfile(filename)
    allergens = set.union(*[x[1] for x in data])
    pos_dict = {}
    for al in allergens:
        pos_dict[al] = set.intersection(*[x[0] for x in data if al in x[1]])

    pos_dict = remove_single_pos(pos_dict)
    answer = ''
    for i, key in enumerate(sorted(list(allergens))):
        answer += [x for x in pos_dict[key]][0]
        if i != len(allergens)-1:
            answer += ','
    print("The allergen containing ingredients in order is\n{}."
          .format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day21.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day21.dat")
    timer.checkpoint_hit()

    timer.end_hit()
