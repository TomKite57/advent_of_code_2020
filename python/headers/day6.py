# -*- coding: utf-8 -*-
"""
Day 6 of Advent of Code 2020


Tom Kite - 06/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(name):
    with open(name) as file:
        data = [line.strip() for line in file]
    return data


def concatenate_groups(input_data):
    counter = 0
    current_str = ''
    all_groups = []
    while counter < len(input_data):
        if input_data[counter] == '':
            all_groups.append(current_str[:-1])
            current_str = ''
        else:
            current_str += input_data[counter] + ','
        counter += 1
    all_groups.append(current_str[:-1])
    return all_groups


def count_any_answers(group_string):
    char_set = set()
    for substr in group_string.split(','):
        for char in substr:
            char_set.add(char)
    return len(char_set)


def count_matching_answers(group_string):
    substrs = group_string.split(',')
    substrs = sorted(substrs, key=len)
    count = 0
    for char in substrs[0]:
        if all([(char in substr) for substr in substrs[1:]]):
            count += 1
    return count


def part1(filename):
    data = readfile(filename)
    groups = concatenate_groups(data)
    total_sum = sum([count_any_answers(g) for g in groups])

    print("The total sum of answers is {}.".format(total_sum))
    return


def part2(filename):
    data = readfile(filename)
    groups = concatenate_groups(data)
    total_sum = sum([count_matching_answers(g) for g in groups])

    print("The total sum of answers is {}.".format(total_sum))
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
