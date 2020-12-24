# -*- coding: utf-8 -*-
"""
Day 23 of Advent of Code 2020


Tom Kite - 23/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        line = file.read().strip()
    return [int(x) for x in line]


class cup_game:
    def __init__(self, cups_in):
        self.minval = min(cups_in)
        self.maxval = max(cups_in)
        self.cups = list(range(self.maxval+1))
        for i, cup in enumerate(self.cups):
            if i == 0:
                self.cups[i] = cups_in[i]
                continue
            cup_loc = cups_in.index(i)
            if cup_loc == self.maxval-1:
                self.cups[i] = self.cups[0]
            else:
                self.cups[i] = cups_in[cup_loc+1]

    def evolve_game_step(self):
        current_cup = self.cups[0]
        head = self.cups[current_cup]
        body = self.cups[head]
        tail = self.cups[body]
        next_cup = self.cups[tail]

        destination = current_cup-1

        while True:
            if destination < self.minval:
                destination = self.maxval
                continue
            if destination not in [head, body, tail]:
                break
            destination -= 1

        self.cups[self.cups[0]] = next_cup
        self.cups[0] = next_cup
        self.cups[tail] = self.cups[destination]
        self.cups[destination] = head
        return 1

    def evolve_N_times(self, N):
        counter = 0
        while counter < N:
            counter += self.evolve_game_step()

    def get_output_string(self):
        prev_cup = 1
        str_out = ''
        for _ in range(len(self.cups[1:-1])):
            prev_cup = self.cups[prev_cup]
            str_out += str(prev_cup)
        return str_out

    def get_two_star_cups(self):
        answer = 1
        prev_cup = 1
        for _ in range(2):
            prev_cup = self.cups[prev_cup]
            answer *= prev_cup
        return answer

    def show(self):
        prev_cup = self.cups[0]
        str_out = '({})'.format(prev_cup)
        for _ in range(len(self.cups[1:-1])):
            prev_cup = self.cups[prev_cup]
            str_out += ' {}'.format(prev_cup)
        print(str_out)


def part1(filename):
    full_steps = 100
    data = readfile(filename)
    my_game = cup_game(data)

    my_game.evolve_N_times(full_steps)

    print("Final cup ordering is {}.".format(my_game.get_output_string()))


def part2(filename):
    full_len = 1000000
    full_steps = 10000000
    data = readfile(filename)

    my_game = cup_game(data)
    my_game.cups[7] = max(data)+1
    my_game.cups += list(range(max(data)+2, full_len+1))
    my_game.cups.append(my_game.cups[0])
    my_game.maxval = len(my_game.cups)-1

    my_game.evolve_N_times(full_steps)

    print("Star cups multiplied gives {}.".format(my_game.get_two_star_cups()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day23.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day23.dat")
    timer.checkpoint_hit()

    timer.end_hit()
