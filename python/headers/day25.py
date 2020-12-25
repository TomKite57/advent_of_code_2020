# -*- coding: utf-8 -*-
"""
Day 25 of Advent of Code 2020


Tom Kite - 25/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        data = [int(x.strip()) for x in file]
    return data


def encryption_loop(num, subject_number=7, division=20201227):
    num *= subject_number
    num = num % division
    return num


def part1(filename):
    data = readfile(filename)
    loop_dict = {}

    num = 1
    loops = 0
    while len(loop_dict) != len(data):
        num = encryption_loop(num)
        loops += 1
        if num in data:
            loop_dict[num] = loops

    min_data = min(data)
    max_data = max(data)
    num = 1

    for _ in range(loop_dict[min_data]):
        num = encryption_loop(num, max_data)

    print("The encryption key is {}.".format(num))


def part2(filename):
    print("Merry Christmas!")


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day25.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day25.dat")
    timer.checkpoint_hit()

    timer.end_hit()
