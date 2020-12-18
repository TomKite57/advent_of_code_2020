# -*- coding: utf-8 -*-
"""
Day 6 of Advent of Code 2020


Tom Kite - 03/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def get_groups(filename):
    with open(filename, 'r') as file:
        data = file.read().split('\n\n')
    return [[set(x) for x in line.split()] for line in data]


def part1(filename):
    print("The total sum of answers is {}.".format
          (sum([len(set.union(*g)) for g in get_groups(filename)])))
    return


def part2(filename):
    print("The total sum of answers is {}.".format
          (sum([len(set.intersection(*g)) for g in get_groups(filename)])))
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day6.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day6.dat")
    timer.checkpoint_hit()

    timer.end_hit()
