# -*- coding: utf-8 -*-
"""
Day 18 of Advent of Code 2020


Tom Kite - 18/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        lines = file.read()
    rules, codes = lines.split('\n\n')

    rule_dict = {}
    for rule in rules.split('\n'):
        lhs, rhs = process_data(rule)
        rule_dict[lhs] = rhs

    return rule_dict, codes.split('\n')


def process_data(rule):
    lhs, rhs = rule.split(': ')
    rhs = [x.split(' ') for x in rhs.split(' | ')]
    new_rhs = []
    for sec in rhs:
        temp = []
        for elem in sec:
            if elem in ['"a"', '"b"']:
                temp.append(elem.strip('"'))
            else:
                temp.append(int(elem))
        new_rhs.append(temp)
    return int(lhs), new_rhs


def approx_complexity(key, rules):
    if key in ['a', 'b']:
        return 1
    total = 1
    for val in rules[key]:
        for x in val:
            total *= (1+approx_complexity(x, rules))
    return total


class data_checker:
    def __init__(self, rules_in, start_rule, codes_in):
        self.rules = rules_in
        self.chains = [[start_rule, ], ]
        self.codes = codes_in
        self.cull = not bool(start_rule)

    def cull_bad_chain(self, chain_ind):
        search = self.chains[chain_ind][0]
        if type(search) == int:
            return False
        for code in self.codes:
            if code[:len(search)] == search:
                return False
        self.chains.pop(chain_ind)
        return True

    def concat_letters(self, chain_ind):
        str_sum = ''
        for j, elem in enumerate(self.chains[chain_ind]):
            if type(elem) != int:
                str_sum += elem
                if j == len(self.chains[chain_ind])-1:
                    self.chains[chain_ind] = [str_sum]
            else:
                if str_sum != '':
                    self.chains[chain_ind] = [str_sum] + \
                        self.chains[chain_ind][j:]
                break

    def evolve_chain(self, chain_ind):
        if len(self.chains[chain_ind]) == 1 and \
           type(self.chains[chain_ind][0]) != int:
            return True
        chain = self.chains.pop(chain_ind)
        for i, elem in enumerate(chain):
            if type(elem) != int:
                continue
            new_rules = self.rules[elem]
            new_chains = []
            for rule in new_rules:
                new_chains.append(chain[:i] + rule + chain[i+1:])
            self.chains += new_chains
            return False

    def fully_evolved(self, chain_ind):
        if len(self.chains[chain_ind]) != 1:
            return False
        if type(self.chains[chain_ind][0]) == int:
            return False
        return True

    def full_evolve(self):
        while not all([self.fully_evolved(x)
                       for x in range(len(self.chains))]):
            i = 0
            while i < len(self.chains):
                if not self.fully_evolved(i):
                    self.concat_letters(i)
                    removed = False
                    if self.cull:
                        removed = self.cull_bad_chain(i)
                    if not removed:
                        self.evolve_chain(i)
                i += 1


def part1(filename):
    rules, codes = readfile(filename)

    machine = data_checker(rules, 0, codes)
    machine.full_evolve()

    total = sum([1 for x in machine.chains if x[0] in codes])
    print("Total valid codes: {}.".format(total))


def part2(filename):
    rules, codes = readfile(filename)

    for line in ["8: 42 | 42 8", "11: 42 31 | 42 11 31"]:
        lhs, rhs = process_data(line)
        rules[lhs] = rhs

    machine = data_checker(rules, 0, codes)
    machine.full_evolve()

    total = sum([1 for x in machine.chains if x[0] in codes])
    print("Total valid codes: {}.".format(total))
    return


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day19.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day19.dat")
    timer.checkpoint_hit()

    timer.end_hit()
