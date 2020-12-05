# -*- coding: utf-8 -*-
"""
Advent of Code 2020

This script will serve as a main menu which calls other days

Tom Kite - 03/12/2020
"""

from headers import day1, day2, day3, day4, day5


menu_options = {1: day1,
                2: day2,
                3: day3,
                4: day4,
                5: day5}


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
