# -*- coding: utf-8 -*-
"""
Day 9 of Advent of Code 2020


Tom Kite - 09/12/2020
"""


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [int(line.strip()) for line in file]
    return lines


def sum_in_list(arr, total):
    rval = [x for x in arr if total-x in arr and x != total/2]
    return bool(len(rval))


def find_first_break(arr, pream_len=25):
    for i, num in enumerate(arr[pream_len:]):
        if not sum_in_list(arr[i: i+pream_len], num):
            return num
    return False


def contiguous_vals(arr, total):
    for size in range(len(arr)):
        for pos in range(len(arr)-size):
            test = arr[pos:pos+size]
            if sum(test) == total:
                return test
    return False


def part1(filename):
    data = readfile(filename)
    answer = find_first_break(data)
    print("First number without a previous sum is {}.".format(answer))
    return


def part2(filename):
    data = readfile(filename)
    num_to_find = find_first_break(data)
    search_arr = [x for x in data if x != num_to_find]
    arr_found = contiguous_vals(search_arr, num_to_find)
    print("The sum of biggest and smallest values in contigous list is {}."
          .format(max(arr_found) + min(arr_found)))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day9.dat")
    print("\nPart 2:")
    part2("../../data/day9.dat")
