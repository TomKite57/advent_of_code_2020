# -*- coding: utf-8 -*-
"""
Day 18 of Advent of Code 2020


Tom Kite - 18/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return ['(' + line + ')' for line in lines]


def find_all(a_str, sub):
    indices = []
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return indices
        indices.append(start)
        start += len(sub)
    return indices


def inner_most_paren(a_str):
    left_par = find_all(a_str, '(')
    right_par = find_all(a_str, ')')
    if len(left_par) == 0:
        return -1, -1
    if len(left_par) == 1:
        return left_par[0], right_par[0]
    for i in range(len(left_par)):
        if i == len(left_par)-1 or right_par[0] < left_par[i+1]:
            return left_par[i], right_par[0]


def process_expr_ltor(line):
    inda, indb = inner_most_paren(line)
    if inda != -1:
        inner_line = line[inda+1:indb]
        mode = '+'
        total = 0
        for elem in inner_line.split(' '):
            if elem in ['+', '*']:
                mode = elem
            elif mode == '+':
                total += int(elem)
            elif mode == '*':
                total *= int(elem)
        line = line[:inda] + str(total) + line[indb+1:]
        return process_expr_ltor(line)
    return int(line)


def process_expr_addition(line):
    inda, indb = inner_most_paren(line)
    if inda != -1:
        inner_line = line[inda+1:indb].split(' ')
        while '+' in inner_line:
            ind = inner_line.index('+')
            num = int(inner_line[ind-1]) + int(inner_line[ind+1])
            inner_line = inner_line[:ind-1] + [str(num)] + inner_line[ind+2:]
        while '*' in inner_line:
            ind = inner_line.index('*')
            num = int(inner_line[ind-1]) * int(inner_line[ind+1])
            inner_line = inner_line[:ind-1] + [str(num)] + inner_line[ind+2:]
        line = line[:inda] + inner_line[0] + line[indb+1:]
        return process_expr_addition(line)
    return int(line)


def part1(filename):
    data = readfile(filename)
    total = sum([process_expr_ltor(x) for x in data])
    print("Total sum of all lines is {}.".format(total))
    return


def part2(filename):
    data = readfile(filename)
    total = sum([process_expr_addition(x) for x in data])
    print("Total sum of all lines is {}.".format(total))
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day18.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day18.dat")
    timer.checkpoint_hit()

    timer.end_hit()
