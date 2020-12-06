# -*- coding: utf-8 -*-
"""
Day 6 of Advent of Code 2020


Tom Kite - 03/12/2020
"""


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
    print("Part 1:")
    part1("../../data/day6.dat")
    print("\nPart 2:")
    part2("../../data/day6.dat")
