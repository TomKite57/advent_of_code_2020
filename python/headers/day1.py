# -*- coding: utf-8 -*-
"""
Day 1 of Advent of Code 2020

This script will find 2 (3) entries in a list of numbers that add to 2020,
and then return the multiplication of the 2 (3)

Tom Kite - 01/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer
import numpy as np


def part1(filename):
    data = np.genfromtxt(filename, dtype='int')

    for i, num_a in enumerate(data):
        for num_b in data[i+1:]:
            if num_a + num_b == 2020:
                print("The numbers are {} and {}.\n"
                      "Giving a product of {}."
                      .format(num_a, num_b, num_a*num_b))
                return


def part2(filename):
    data = np.genfromtxt(filename, dtype='int')

    for i, num_a in enumerate(data):
        for j, num_b in enumerate(data[i+1:]):
            if num_a + num_b >= 2020:
                continue
            for num_c in data[j+1:]:
                if num_a + num_b + num_c == 2020:
                    print("The numbers are {}, {} and {}.\n"
                          "Giving a product of {}."
                          .format(num_a, num_b, num_c, num_a*num_b*num_c))
                    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day1.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day1.dat")
    timer.checkpoint_hit()

    timer.end_hit()
