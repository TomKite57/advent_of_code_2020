# -*- coding: utf-8 -*-
"""
Day 12 of Advent of Code 2020


Tom Kite - 12/12/2020
"""


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return [[line[0], int(line[1:])] for line in lines]


class ship_v1:
    def __init__(self):
        # Let 0=North, 1=East, 2=South, 3=West
        self.facing = 1
        self.face_dict = {0: 'N',
                          1: 'E',
                          2: 'S',
                          3: 'W'}
        self.x = 0
        self.y = 0

    def manhat_dist(self):
        return abs(self.x) + abs(self.y)

    def move(self, instruction, amount):
        if instruction == 'F':
            instruction = self.face_dict[self.facing]
        if instruction == 'N':
            self.y += amount
            return
        if instruction == 'E':
            self.x += amount
            return
        if instruction == 'S':
            self.y -= amount
            return
        if instruction == 'W':
            self.x -= amount
            return
        if instruction == 'R':
            self.facing = int((self.facing + amount/90) % 4)
            return
        if instruction == 'L':
            self.facing = int((self.facing - amount/90) % 4)
            return


class ship_v2:
    def __init__(self):
        self.face_dict = {0: 'N',
                          1: 'E',
                          2: 'S',
                          3: 'W'}
        self.x = 0
        self.y = 0
        self.wpx = 10
        self.wpy = 1

    def manhat_dist(self):
        return abs(self.x) + abs(self.y)

    def rotate_wp_r(self):
        old_x = self.wpx
        old_y = self.wpy
        self.wpy = -old_x
        self.wpx = old_y

    def rotate_wp_l(self):
        for _ in range(3):
            self.rotate_wp_r()

    def move(self, instruction, amount):
        if instruction == 'F':
            self.x += amount*self.wpx
            self.y += amount*self.wpy
        if instruction == 'N':
            self.wpy += amount
            return
        if instruction == 'E':
            self.wpx += amount
            return
        if instruction == 'S':
            self.wpy -= amount
            return
        if instruction == 'W':
            self.wpx -= amount
            return
        if instruction == 'R':
            for _ in range(int(amount/90)):
                self.rotate_wp_r()
            return
        if instruction == 'L':
            for _ in range(int(amount/90)):
                self.rotate_wp_l()
            return


def part1(filename):
    data = readfile(filename)
    my_ship = ship_v1()
    for line in data:
        my_ship.move(*line)
    print("The final distance is {}.".format(my_ship.manhat_dist()))
    return


def part2(filename):
    data = readfile(filename)
    my_ship = ship_v2()
    for line in data:
        my_ship.move(*line)
    print("The final distance is {}.".format(my_ship.manhat_dist()))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day12.dat")
    print("\nPart 2:")
    part2("../../data/day12.dat")
