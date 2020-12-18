# -*- coding: utf-8 -*-
"""
Day 3 of Advent of Code 2020

This script looks at moviing through a map counting the trees (#) as it does.
The psoition increases by an amount (grad) each time.

Tom Kite - 03/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(name):
    with open(name) as file:
        data = [line.strip() for line in file]
    return data


def slide_down(pos, grad):
    return [pos[i] + grad[i] for i in range(len(pos))]


def check_tree(tree_map, pos):
    pos_x_eff = pos[0] % len(tree_map[0])
    return tree_map[pos[1]][pos_x_eff] == '#'


def full_slide(tree_map, grad, pos=[0, 0]):
    tree_count = 0
    while pos[1] < len(tree_map):
        if check_tree(tree_map, pos):
            tree_count += 1
        pos = slide_down(pos, grad)
    return tree_count


def part1(filename):
    data = readfile(filename)
    count = full_slide(data, [3, 1])
    print("On the way down you will hit {} trees.".format(count))


def part2(filename):
    data = readfile(filename)
    grads = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    mult_count = 1
    for grad in grads:
        mult_count *= full_slide(data, grad)
    print("The multiplication of trees encountered on each path is {}."
          .format(mult_count))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day3.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day3.dat")
    timer.checkpoint_hit()

    timer.end_hit()
