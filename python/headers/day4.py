# -*- coding: utf-8 -*-
"""
Day 4 of Advent of Code 2020


Tom Kite - 04/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(name):
    with open(name) as file:
        data = [line.strip() for line in file]
    return data


def int_in_range(num, low, high):
    try:
        num = int(num)
    except ValueError:
        return False
    except TypeError:
        return False
    return low <= num <= high


def check_int_char_range(inp, intmin=0, intmax=9, charmin='a', charmax='z'):
    try:
        inp = int(inp)
        return intmin <= inp <= intmax
    except ValueError:
        return charmin <= inp <= charmax


class passport():
    def __init__(self, string_in):
        self.data = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None,
                     'hcl': None, 'ecl': None, 'pid': None, 'cid': None}
        substr = string_in.strip().split(' ')
        for line in substr:
            code, data = line.split(':')
            self.data[code] = data

    def is_valid_part1(self):
        for code in self.data.keys():
            if code == 'cid':
                continue
            if self.data[code] is None:
                return False
        return True

    def valid_byr(self):
        return int_in_range(self.data['byr'], 1920, 2002)

    def valid_iyr(self):
        return int_in_range(self.data['iyr'], 2010, 2020)

    def valid_eyr(self):
        return int_in_range(self.data['eyr'], 2020, 2030)

    def valid_hgt(self):
        hgt = self.data['hgt']
        if hgt is None:
            return False
        if hgt[-2:] == 'cm':
            return int_in_range(hgt[:-2], 150, 193)
        if hgt[-2:] == 'in':
            return int_in_range(hgt[:-2], 59, 76)

    def valid_hcl(self):
        hcl = self.data['hcl']
        if hcl is None:
            return False
        if hcl[0] == '#' and len(hcl) == 7:
            for char in hcl[1:]:
                if not check_int_char_range(char, 0, 9, 'a', 'f'):
                    return False
            return True
        return False

    def valid_ecl(self):
        return self.data['ecl'] in ['amb', 'blu', 'brn', 'gry',
                                    'grn', 'hzl', 'oth']

    def valid_pid(self):
        try:
            int(self.data['pid'])
            return len(self.data['pid']) == 9
        except ValueError:
            return False
        except TypeError:
            return False

    def is_valid_part2(self):
        if not self.valid_byr():
            return False
        if not self.valid_iyr():
            return False
        if not self.valid_eyr():
            return False
        if not self.valid_hgt():
            return False
        if not self.valid_hcl():
            return False
        if not self.valid_ecl():
            return False
        if not self.valid_pid():
            return False
        return True


def process_passports(input_data):
    counter = 0
    current_str = ''
    all_passes = []
    while counter < len(input_data):
        if input_data[counter] == '':
            all_passes.append(passport(current_str))
            current_str = ''
        else:
            current_str += ' ' + input_data[counter]
        counter += 1
    all_passes.append(passport(current_str))
    return all_passes


def part1(filename):
    data = readfile(filename)
    all_passports = process_passports(data)
    count = sum([1 for p in all_passports if p.is_valid_part1()])
    print("Total valid passports is {}.".format(count))


def part2(filename):
    data = readfile(filename)
    all_passports = process_passports(data)
    count = sum([1 for p in all_passports if p.is_valid_part2()])
    print("Total valid passports is {}.".format(count))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day4.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day4.dat")
    timer.checkpoint_hit()

    timer.end_hit()
