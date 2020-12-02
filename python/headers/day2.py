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


def process_line_input(line):
    line = line.strip()
    nums, letter, password = line.split(' ')
    num_a, num_b = nums.split('-')
    letter = letter.strip(':')
    return [int(num_a), int(num_b), letter, password]


def readfile(filename):
    with open(filename) as file:
        lines = file.readlines()
    data = [process_line_input(x) for x in lines]
    return data


def valid_password_part1(code):
    num1, num2, letter, password = code
    count = password.count(letter)
    return num1 <= count <= num2


def valid_password_part2(code):
    num1, num2, letter, password = code
    letters = password[num1-1] + password[num2-1]
    return letters.count(letter) == 1


def part1(filename):
    data = readfile(filename)
    valid = [valid_password_part1(x) for x in data]
    print("There are {} valid passwords, and {} invalid."
          .format(valid.count(1), valid.count(0)))


def part2(filename):
    data = readfile(filename)
    valid = [valid_password_part2(x) for x in data]
    print("There are {} valid passwords, and {} invalid."
          .format(valid.count(1), valid.count(0)))


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day2.dat")
    print("\nPart 2:")
    part2("../../data/day2.dat")
