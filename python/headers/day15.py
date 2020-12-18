# -*- coding: utf-8 -*-
"""
Day 15 of Advent of Code 2020


Tom Kite - 15/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        nums = [line.split(',') for line in file][0]
    return [int(x) for x in nums]


class memory_game():
    def __init__(self, start_nums):
        self.last_turn_dict = {}
        self.initial_nums = start_nums
        for i, num in enumerate(self.initial_nums):
            self.last_turn_dict[num] = i
        self.prev_num = self.initial_nums[-1]

    def evolve_till(self, N):
        for i in range(len(self.initial_nums), N):
            turns = self.last_turn_dict.get(self.prev_num, i-1)
            self.last_turn_dict[self.prev_num] = i-1
            self.prev_num = i - 1 - turns
        return self.prev_num


def part1(filename):
    data = readfile(filename)
    game = memory_game(data)
    final_num = game.evolve_till(2020)
    print("Final number spoken is {}.".format(final_num))


def part2(filename):
    data = readfile(filename)
    game = memory_game(data)
    final_num = game.evolve_till(30000000)
    print("Final number spoken is {}.".format(final_num))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day15.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day15.dat")
    timer.checkpoint_hit()

    timer.end_hit()
