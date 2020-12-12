# -*- coding: utf-8 -*-
"""
Day 11 of Advent of Code 2020


Tom Kite - 03/12/2020
"""


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


class seating:
    def __init__(self, seat_in):
        self.grid = seat_in
        self.iterations = 0
        self.los_dict = self._get_los_dict()

    def _in_grid(self, x, y):
        return (0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]))

    def _get_los_dict(self):
        los_dict = {}
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] == '.':
                    continue
                else:
                    los_dict[(i, j)] = self._find_los(i, j)
        return los_dict

    def _find_los(self, x, y):
        directions = [[i, j] for i in range(-1, 2) for j in range(-1, 2)
                      if ([i, j] != [0, 0])]
        los_coords = []
        for direc in directions:
            temp_x = x + direc[0]
            temp_y = y + direc[1]
            while True:
                if not self._in_grid(temp_x, temp_y):
                    break
                if self.grid[temp_y][temp_x] != '.':
                    los_coords.append([temp_x, temp_y])
                    break
                temp_x += direc[0]
                temp_y += direc[1]
        return los_coords

    def _count_adjacent(self, x, y, check):
        count = 0
        for j in range(max(0, y-1), min(len(self.grid), y+2)):
            for i in range(max(0, x-1), min(len(self.grid[j]), x+2)):
                if (i == x and j == y):
                    continue
                if self.grid[j][i] == check:
                    count += 1
        return count

    def _evolve_seat_adj(self, x, y):
        if self.grid[y][x] == '.':
            return '.'
        if self.grid[y][x] == '#':
            if self._count_adjacent(x, y, '#') >= 4:
                return 'L'
            else:
                return '#'
        if self.grid[y][x] == 'L':
            if self._count_adjacent(x, y, '#') == 0:
                return '#'
            else:
                return 'L'
        else:
            raise Exception("Seat type {} not understood"
                            .format(self.grid[y][x]))

    def _count_los(self, x, y, check):
        count = 0
        for coords in self.los_dict[(x, y)]:
            if self.grid[coords[1]][coords[0]] == check:
                count += 1
        return count

    def _evolve_seat_los(self, x, y):
        if self.grid[y][x] == '.':
            return '.'
        if self.grid[y][x] == '#':
            if self._count_los(x, y, '#') >= 5:
                return 'L'
            else:
                return '#'
        if self.grid[y][x] == 'L':
            if self._count_los(x, y, '#') == 0:
                return '#'
            else:
                return 'L'
        else:
            raise Exception("Seat type {} not understood"
                            .format(self.grid[y][x]))

    def _evolve_grid(self, check_func):
        changed = False
        new_grid = []
        for j in range(len(self.grid)):
            new_line = ''
            for i in range(len(self.grid[j])):
                new_state = check_func(i, j)
                new_line += new_state
                if self.grid[j][i] != new_state:
                    changed = True
            new_grid.append(new_line)
        if changed:
            self.iterations += 1
            self.grid = new_grid
        return changed

    def show_grid(self):
        for line in self.grid:
            print(line)
        print()
        return

    def evolve_till_stable_adj(self):
        changed = True
        while changed:
            changed = self._evolve_grid(self._evolve_seat_adj)
        return self.iterations

    def evolve_till_stable_los(self):
        changed = True
        while changed:
            changed = self._evolve_grid(self._evolve_seat_los)
        return self.iterations

    def count_occupied(self):
        seats = 0
        for line in self.grid:
            seats += line.count('#')
        return seats


def part1(filename):
    data = readfile(filename)
    my_seats = seating(data)
    my_seats.evolve_till_stable_adj()
    total_occupied = my_seats.count_occupied()
    print("There are {} seats occupied in the end.".format(total_occupied))
    return


def part2(filename):
    data = readfile(filename)
    my_seats = seating(data)
    my_seats.evolve_till_stable_los()
    total_occupied = my_seats.count_occupied()
    print("There are {} seats occupied in the end.".format(total_occupied))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day11.dat")
    print("\nPart 2:")
    part2("../../data/day11.dat")
