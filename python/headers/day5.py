# -*- coding: utf-8 -*-
"""
Day 5 of Advent of Code 2020


Tom Kite - 05/12/2020
"""


def readfile(name):
    with open(name) as file:
        data = [line.strip() for line in file]
    return data


def bin_to_num(bin_in, zero='0', one='1'):
    total = 0
    for i, char in enumerate(bin_in):
        if char == zero:
            continue
        elif char == one:
            total += pow(2, len(bin_in) - i - 1)
        else:
            print("Unknown character found: {}.".format(char))
            return None
    return total


def get_seat_ID(code):
    row = bin_to_num(code[:-3], 'F', 'B')
    aisle = bin_to_num(code[-3:], 'L', 'R')
    return 8*row + aisle


def part1(filename):
    data = readfile(filename)
    max_ID = max([get_seat_ID(line) for line in data])
    print("Maximum seat ID is {}.".format(max_ID))
    return


def part2(filename):
    data = readfile(filename)
    largest_ID = get_seat_ID('B'*7+'R'*3)
    all_IDs = [x for x in range(largest_ID+1)]
    for line in data:
        all_IDs.pop(all_IDs.index(get_seat_ID(line)))

    my_seat_ID = [x for x in all_IDs if
                  (x+1 not in all_IDs and x-1 not in all_IDs)][0]

    print("My seat has ID {}.".format(my_seat_ID))


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day5.dat")
    print("\nPart 2:")
    part2("../../data/day5.dat")
