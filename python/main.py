# -*- coding: utf-8 -*-
"""
Advent of Code 2020

This script will serve as a main menu which calls other days solutions

Tom Kite - 25/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer
from headers import day1, day2, day3, day4, day5, day6, day7, day8, day9,\
                    day10, day11, day12, day13, day14, day15, day16, day17,\
                    day18, day19, day20, day21, day22, day23, day24


menu_options = {1: day1, 2: day2, 3: day3, 4: day4, 5: day5,
                6: day6, 7: day7, 8: day8, 9: day9, 10: day10,
                11: day11, 12: day12, 13: day13, 14: day14, 15: day15,
                16: day16, 17: day17, 18: day18, 19: day19, 20: day20,
                21: day21, 22: day22, 23: day23, 24: day24}


def all_days():
    timer = Advent_Timer()
    for day in menu_options:
        menu_options[day].part1("../data/day{}.dat".format(day))
        timer.checkpoint_hit()
        menu_options[day].part2("../data/day{}.dat".format(day))
        timer.checkpoint_hit()
    timer.end_hit()


def int_input(entry):
    try:
        entry = int(entry)
        return True, entry
    except ValueError:
        return False, entry


if __name__ == "__main__":
    print("Welcome to my Advent of Code 2020 solutions!")

    while True:
        # Take day input
        valid, day_num = int_input(input("Which day would you like to solve? "
                                         "(Enter -1 to exit)\n"))
        # Check valid
        if not valid:
            print("Sorry, I didn't understand that input!")
            continue
        # Check for exit
        if day_num == -1:
            break
        # Run all days
        if day_num == 2020:
            all_days()
            continue
        # Check day exists
        if day_num not in menu_options.keys():
            print("I haven't solved that day yet!")
            continue

        # Take part input
        valid, part_num = int_input(input("Part 1 or part 2?\n"))
        # Check valid
        if not valid:
            print("Sorry, I didn't understand that input!")
            continue

        # Check it is part1 or part2 and solve
        if part_num == 1:
            menu_options[day_num].part1("../data/day{}.dat".format(day_num))
        elif part_num == 2:
            menu_options[day_num].part2("../data/day{}.dat".format(day_num))
        else:
            print("Only part 1 and 2 exist!")

    print("Exiting!")
