# -*- coding: utf-8 -*-
"""
Day 13 of Advent of Code 2020


Tom Kite - 13/12/2020
"""

import numpy as np


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def process_v1(data):
    return int(data[0]), [int(x) for x in data[1].split(',') if x != 'x']


def process_v2(data):
    return [int(x) if x != 'x' else x for x in data[1].split(',')]


def wait_time(arriv_time, bus_time):
    delay = (arriv_time % bus_time)
    if delay != 0:
        return bus_time - (arriv_time % bus_time)
    return 0


def sync_to_bus(bus_time, bus_delay, current_time, delta_time):
    while wait_time(current_time, bus_time) != (bus_delay % bus_time):
        current_time += delta_time
    return current_time


def sync_all_busses(bus_data):
    current_time = np.array([0], dtype='uint64')
    lcm = np.array([1], dtype='uint64')
    for i, bus in enumerate(bus_data):
        if bus == 'x':
            continue
        current_time = sync_to_bus(bus, i, current_time, lcm)
        lcm = np.lcm(lcm, bus)
    return current_time[0]


def part1(filename):
    arrival_time, bus_times = process_v1(readfile(filename))
    best_bus_time = min(bus_times, key=lambda x: wait_time(arrival_time, x))
    print("Bus ID * wait time is {}."
          .format(best_bus_time*wait_time(arrival_time, best_bus_time)))
    return


def part2(filename):
    bus_data = process_v2(readfile(filename))
    time = sync_all_busses(bus_data)
    print("First time stamp is {}.".format(time))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day13.dat")
    print("\nPart 2:")
    part2("../../data/day13.dat")
