# -*- coding: utf-8 -*-
"""
Day 2 of Advent of Code 2020

This script will read a file formatted as such:
int1-int2 char: string
and will process the code according to two criteria
1) int1 <= string.count(char) <= int2
2) (string[int1-1], string[int2-1]).count(char) == 1

Tom Kite - 01/12/2020
"""


import numpy as np


def process_line_input(line):
    line = line.strip('\n')
    nums, letter, password = line.split(' ')
    num_a, num_b = nums.split('-')
    letter = letter.strip(':')
    return np.array([num_a, num_b, letter, password])


def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
    data = [process_line_input(x) for x in lines]
    return np.array(data)


def valid_password_part1(code):
    count = code[3].count(code[2])
    return int(code[0]) <= count <= int(code[1])


def valid_password_part2(code):
    letters = code[3][int(code[0])-1] + code[3][int(code[1])-1]
    return letters.count(code[2]) == 1


def part1(filename):
    data = readfile(filename)
    valid = [valid_password_part1(x) for x in data]
    print("There are {} valid passwords, and {} invalid"
          .format(valid.count(1), valid.count(0)))


def part2(filename):
    data = readfile(filename)
    valid = [valid_password_part2(x) for x in data]
    print("There are {} valid passwords, and {} invalid"
          .format(valid.count(1), valid.count(0)))


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day2.dat")
    print("\nPart 2:")
    part2("../../data/day2.dat")
