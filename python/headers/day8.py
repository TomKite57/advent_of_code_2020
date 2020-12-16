# -*- coding: utf-8 -*-
"""
Day 8 of Advent of Code 2020


Tom Kite - 08/12/2020
"""


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip().split(' ') for line in file]
    processed = [[x[0], int(x[1])] for x in lines]
    return processed


class boot_loop:
    def __init__(self, code_in, line_to_swap=None):
        self.code = code_in
        self.index = 0
        self.prev_ind = []
        self.accumulation = 0
        self.rule_dict = {'acc': self._accumulator,
                          'nop': self._no_op,
                          'jmp': self._jump}
        self.swap_dict = {'nop': 'jmp',
                          'jmp': 'nop',
                          'acc': 'acc'}
        self.line_to_swap = line_to_swap
        return

    def _swap_line_instruction(self, i):
        if i is None:
            return
        self.code[i][0] = self.swap_dict[self.code[i][0]]
        return

    def _advance(self):
        line = self.code[self.index]
        self.rule_dict[line[0]](line[1])
        return

    def _accumulator(self, inp):
        self.accumulation += inp
        self.index += 1
        return

    def _no_op(self, _):
        self.index += 1
        return

    def _jump(self, inp):
        self.index += inp
        return

    def advance_till_loop(self):
        self._swap_line_instruction(self.line_to_swap)
        success = False
        while True:
            self._advance()
            if self.index in self.prev_ind:
                break
            if self.index == len(self.code):
                success = True
                break
            self.prev_ind.append(self.index)
        self._swap_line_instruction(self.line_to_swap)
        return success, self.accumulation


def part1(filename):
    data = readfile(filename)
    _, answer = boot_loop(data).advance_till_loop()
    print("The accumulation at first repeat is {}.".format(answer))
    return


def part2(filename):
    data = readfile(filename)

    for i, line in enumerate(data):
        if line[0] != 'acc':
            success, answer = boot_loop(data, i).advance_till_loop()
            if success:
                break

    if success:
        print("Accumulation for fixed loop is {}.".format(answer))
    else:
        print("Something went wrong!")
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day8.dat")
    print("\nPart 2:")
    part2("../../data/day8.dat")
