# -*- coding: utf-8 -*-
"""
Day 10 of Advent of Code 2020


Tom Kite - 10/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [int(line.strip()) for line in file]
    return lines


def show_chain(data, chain):
    print([data[i] for i in chain])


def increment_count(data, chain):
    results = [0, 0, 0]
    # Chain start
    results[data[chain[0]]-1] += 1
    for i in range(1, len(chain)):
        diff = data[chain[i]] - data[chain[i-1]]
        results[diff-1] += 1
    # Final device
    results[2] += 1
    return results


def split_chain(data, chain, tolerance=3):
    segments = []
    seg_start = 0
    for i in range(1, len(chain)):
        if data[chain[i]] - data[chain[i-1]] == tolerance:
            segments.append(chain[seg_start:i])
            seg_start = i
    segments.append(chain[seg_start:])
    return segments


def viable_chain(data, chain, check_start, tolerance=3):
    if check_start and data[chain[0]] > tolerance:
        return False
    for i in range(1, len(chain)):
        if data[chain[i]] - data[chain[i-1]] > tolerance:
            return False
    return True


def chain_options(data, chain, index_start=0):
    if not viable_chain(data, chain, index_start == 0):
        return 0
    total = 1
    for i in range(index_start, len(chain)-1):
        total += chain_options(data, chain[:i] + chain[i+1:], i)
    return total


def part1(filename):
    data = readfile(filename)
    chain = sorted(range(len(data)), key=lambda i: data[i])
    ones, _, threes = increment_count(data, chain)
    print("The product of +1 adapters and +3 is {}.".format(ones*threes))
    return


def part2(filename):
    data = readfile(filename)
    chain = sorted(range(len(data)), key=lambda i: data[i])

    segments = split_chain(data, chain)
    combinations = 1
    for i, seg in enumerate(segments):
        if i == 0:
            combinations *= chain_options(data, seg, 0)
        else:
            combinations *= chain_options(data, seg, 1)
    print("Total combinations of adapators is {}.".format(combinations))
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day10.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day10.dat")
    timer.checkpoint_hit()

    timer.end_hit()
