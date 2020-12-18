# -*- coding: utf-8 -*-
"""
Day 14 of Advent of Code 2020


Tom Kite - 14/12/2020
"""


from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def process_line(line):
    if line[:4] == 'mask':
        return 'mask', line[7:], None
    if line[:3] == 'mem':
        substr = line.split('[')
        substr = substr[1].split(']')
        return 'mem', int(substr[0]), int(substr[1][3:])


def dec_to_bin(x):
    return bin(x)[2:]


def bin_to_dec(x):
    return int(x, 2)


def swap_first_X(line):
    ind = line.index('X')
    return line[:ind] + '0' + line[ind+1:], line[:ind] + '1' + line[ind+1:]


class mask_emulator_v1:
    def __init__(self):
        self.memory = {}
        self.mask = 'X'*36

    def add_to_mem(self, mem_add, num):
        self.memory[mem_add] = self.apply_mask(num)

    def set_mask(self, mask):
        self.mask = mask

    def apply_mask(self, num):
        num_str = dec_to_bin(num)
        num_str = '0'*(len(self.mask)-len(num_str)) + num_str
        rval = ''
        for i in range(len(self.mask)):
            if self.mask[i] == 'X':
                rval += num_str[i]
            else:
                rval += self.mask[i]
        return bin_to_dec(rval)

    def get_mem_sum(self):
        return sum([x for x in self.memory.values()])


class mask_emulator_v2:
    def __init__(self):
        self.memory = {}
        self.mask = 'X'*36

    def add_to_mem(self, mem_add, num):
        mem_add = self.apply_mask(mem_add)
        mem_add = ['0'*(36-len(mem_add)) + mem_add]
        while any(['X' in x for x in mem_add]):
            new_mem_add = []
            for line in mem_add:
                if 'X' not in line:
                    new_mem_add.append(line)
                else:
                    to_app = swap_first_X(line)
                    new_mem_add.append(to_app[0])
                    new_mem_add.append(to_app[1])
            mem_add = new_mem_add
        for mem in mem_add:
            self.memory[mem] = num

    def set_mask(self, mask):
        self.mask = mask

    def apply_mask(self, num):
        num_str = dec_to_bin(num)
        num_str = '0'*(len(self.mask)-len(num_str)) + num_str
        rval = ''
        for i in range(len(self.mask)):
            if self.mask[i] == 'X':
                rval += 'X'
            elif self.mask[i] == '1':
                rval += '1'
            elif self.mask[i] == '0':
                rval += num_str[i]
        return rval

    def get_mem_val(self, mem_str):
        lines = [mem_str]
        total = 0
        while len(lines):
            new_lines = []
            for line in lines:
                if 'X' not in line:
                    total += bin_to_dec(line)
                else:
                    to_app = swap_first_X(line)
                    new_lines.append(to_app[0])
                    new_lines.append(to_app[1])
            lines = new_lines
        return total

    def get_mem_sum(self):
        return sum(self.memory.values())


def part1(filename):
    data = readfile(filename)
    my_emulator = mask_emulator_v1()
    for line in data:
        action, input1, input2 = process_line(line)
        if action == 'mask':
            my_emulator.set_mask(input1)
        elif action == 'mem':
            my_emulator.add_to_mem(input1, input2)
        else:
            raise Exception("Did not understand command {}".format(action))
    print("Total memory sum is {}".format(my_emulator.get_mem_sum()))


def part2(filename):
    data = readfile(filename)
    my_emulator = mask_emulator_v2()
    for line in data:
        action, input1, input2 = process_line(line)
        if action == 'mask':
            my_emulator.set_mask(input1)
        elif action == 'mem':
            my_emulator.add_to_mem(input1, input2)
        else:
            raise Exception("Did not understand command {}".format(action))
    print("Total memory sum is {}".format(my_emulator.get_mem_sum()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day14.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day14.dat")
    timer.checkpoint_hit()

    timer.end_hit()
