# -*- coding: utf-8 -*-
"""
Day 16 of Advent of Code 2020


Tom Kite - 16/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        data = file.read()
    rules, my_tic, other_tics = data.split('\n\n')
    return rules.split('\n'), my_tic.split('\n'), other_tics.split('\n')


def process_rules(rule_in):
    output = {}
    for line in rule_in:
        rule_class, ranges = line.split(':')
        ranges = ranges.split(' or ')
        for i in range(len(ranges)):
            ranges[i] = ranges[i].split('-')
            ranges[i] = [int(x) for x in ranges[i]]
        output[rule_class] = ranges
    return output


def num_in_range(num, rang):
    return rang[0] <= num <= rang[1]


def process_tics(tic_in):
    output = []
    for line in tic_in[1:]:
        output.append([int(x) for x in line.split(',')])
    return output


def invalid_tic_nums(tic, ranges):
    outputs = []
    for num in tic:
        if not any(num_in_range(num, rang[0]) or
                   num_in_range(num, rang[1])
                   for rang in ranges):
            outputs.append(num)
    return outputs


def filter_possibilities(pos, valid_tic, rules):
    for col, num in enumerate(valid_tic):
        to_remove = []
        for rule_class in pos[col]:
            if not any(num_in_range(num, rang) for rang in rules[rule_class]):
                to_remove.append(rule_class)
        for rem in to_remove:
            pos[col].remove(rem)
    return pos


def filter_single_possibilities(pos):
    while True:
        orig_len = [len(p) for p in pos]
        for p1 in pos:
            if len(p1) == 1:
                for p2 in pos:
                    if p2 != p1:
                        p2.discard(*p1)
        if [len(p) for p in pos] == orig_len:
            return pos


def part1(filename):
    rules, my_tic, other_tics = readfile(filename)

    rules = process_rules(rules)
    other_tics = process_tics(other_tics)

    total_sum = sum([sum(invalid_tic_nums(tic, rules.values()))
                     for tic in other_tics])
    print("Total bad ticket number sum is {}.".format(total_sum))


def part2(filename):
    rules, my_tic, other_tics = readfile(filename)

    rules = process_rules(rules)
    my_tic = process_tics(my_tic)[0]
    other_tics = process_tics(other_tics)
    other_tics = [tic for tic in other_tics
                  if not len(invalid_tic_nums(tic, rules.values()))]

    possibilities = [set([rule for rule in rules.keys()]) for _ in my_tic]
    for tic in other_tics:
        possibilities = filter_possibilities(possibilities, tic, rules)
    possibilities = filter_single_possibilities(possibilities)

    answer = 1
    for i, pos in enumerate(possibilities):
        if ('departure' in list(pos)[0]):
            answer *= my_tic[i]

    print("The multiplication of 'departure' numbers is {}".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day16.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day16.dat")
    timer.checkpoint_hit()

    timer.end_hit()
