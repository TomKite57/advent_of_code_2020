# -*- coding: utf-8 -*-
"""
Day 7 of Advent of Code 2020


Tom Kite - 03/12/2020
"""

from copy import deepcopy


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def process_line(line):
    parent_str, children_str = line.split(' bags contain ')
    parent = [1] + [parent_str.split(' ')[0] + ' ' + parent_str.split(' ')[1]]
    children_str = children_str.split(',')
    children = []
    for child in children_str:
        num, adj, col = child.strip().split(' ')[:3]
        if num == 'no':
            children.append([0, None])
        else:
            children.append([int(num), adj + ' ' + col])
    return parent, children


def does_x_contain_y(x, y, recipes):
    bags = deepcopy(recipes[x])
    while len(bags):
        new_bags = []
        for _ in range(len(bags)):
            bag = bags.pop(-1)
            if bag[1] == y:
                return True
            if bag[1] is not None:
                new_bags += recipes[bag[1]]
        bags = new_bags
    return False


def count_children(x, recipes):
    total_count = 0
    bags = deepcopy(recipes[x])
    for i in range(len(bags)-1, -1, -1):
        if bags[i][1] is None:
            bags.pop(i)
        else:
            total_count += bags[i][0]*(count_children(bags[i][1], recipes) + 1)
    return total_count


def part1(filename):
    data = readfile(filename)

    recipe_dict = {}
    for i, line in enumerate(data):
        parent, children = process_line(line)
        recipe_dict[parent[1]] = children

    answer = sum([1 for x in recipe_dict.keys()
                  if does_x_contain_y(x, 'shiny gold', recipe_dict)])

    print("In total {} bags contain a shiny gold bag".format(answer))
    return


def part2(filename):
    data = readfile(filename)

    recipe_dict = {}
    for i, line in enumerate(data):
        parent, children = process_line(line)
        recipe_dict[parent[1]] = children

    answer = count_children('shiny gold', recipe_dict)

    print("In total the shiny gold bag contains {} others".format(answer))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day7.dat")
    print("\nPart 2:")
    part2("../../data/day7.dat")
