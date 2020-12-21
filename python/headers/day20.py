# -*- coding: utf-8 -*-
"""
Day 20 of Advent of Code 2020


Tom Kite - 20/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer
import numpy as np


op_side = {1: 3,
           2: 4,
           3: 1,
           4: 2}

operations = ['None',
              'r1', 'r1', 'r1',
              'r1f1', 'r1', 'r1', 'r1',
              'r1f-1f1', 'r1', 'r1', 'r1',
              'r1f1', 'r1', 'r1', 'r1',
              'END']

monster_mask = np.array(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]],
    dtype='int8')


def readfile(filename):
    with open(filename, 'r') as file:
        tiles = file.read().split('\n\n')
    return [tile.strip().split('\n') for tile in tiles]


def tile_to_np(tile_in):
    rval = np.zeros(shape=(len(tile_in), len(tile_in[1])),
                    dtype='int8')
    for i, row in enumerate(tile_in):
        for j, elem in enumerate(row):
            if elem == '#':
                rval[i, j] = 1
    return rval


class photo:
    def __init__(self, tile_in):
        self.ID = int(tile_in[0].strip("Tile ").strip(":"))
        self.tile = tile_to_np(tile_in[1:])
        self.neighbours = {1: [],
                           2: [],
                           3: [],
                           4: []}

    def rotate(self, turns):
        self.tile = np.rot90(self.tile, turns)
        new_neighbours = {}
        for key in self.neighbours:
            new_key = (key+turns) % 4
            if new_key == 0:
                new_key = 4
            new_neighbours[new_key] = self.neighbours[key]
        self.neighbours = new_neighbours

    def flip(self, axis):
        # 0 = horizontal, 1 = vertical
        self.tile = np.flip(self.tile, axis)
        new_neighbours = {}
        if axis == 0:
            new_neighbours[1] = self.neighbours[1]
            new_neighbours[2] = self.neighbours[4]
            new_neighbours[3] = self.neighbours[3]
            new_neighbours[4] = self.neighbours[2]
        elif axis == 1:
            new_neighbours[1] = self.neighbours[3]
            new_neighbours[2] = self.neighbours[2]
            new_neighbours[3] = self.neighbours[1]
            new_neighbours[4] = self.neighbours[4]
        self.neighbours = new_neighbours

    def apply_op(self, op):
        if op == 'r1':
            self.rotate(1)
        elif op == 'r1f1':
            self.rotate(1)
            self.flip(0)
        elif op == 'r1f-1f1':
            self.rotate(1)
            self.flip(0)
            self.flip(1)
        return

    def get_boundary(self, side):
        # 1 = right, 2 = top, 3 = left, 4 = bottom
        if side == 1:
            return self.tile[:, -1]
        if side == 2:
            return self.tile[0, :]
        if side == 3:
            return self.tile[:, 0]
        if side == 4:
            return self.tile[-1, :]

    def compare_boundary(self, other):
        rval = []
        for i in [1, 2, 3, 4]:
            if all(self.get_boundary(i) == other.get_boundary(op_side[i])):
                rval.append(i)
        return rval

    def match_to_neighbour(self, other):
        # Only ever rotate others if no neighbours
        for op in operations:
            other.apply_op(op)
            if op == 'END':
                return
            rval = self.compare_boundary(other)
            for val in rval:
                self.neighbours[val].append(other)
                other.neighbours[op_side[val]].append(self)

    def num_unmatched(self):
        count = 0
        for val in self.neighbours.values():
            if val == []:
                count += 1
        return count

    def get_borderless_tile(self):
        return self.tile[1:-1, 1:-1]

    def full_mask(self):
        for y in range(len(self.tile)-len(monster_mask)):
            for x in range(len(self.tile[0])-len(monster_mask[0])):
                self.mask_monsters(x, y)

    def mask_monsters(self, start_x, start_y):
        found_one = False
        zone = self.tile[start_y:start_y+len(monster_mask),
                         start_x:start_x+len(monster_mask[0])]
        new_zone, suc = mask_zone(zone)
        if suc:
            self.tile[start_y:start_y+len(monster_mask),
                      start_x:start_x+len(monster_mask[0])] = new_zone
            found_one = True
        return found_one

    def wave_count(self):
        count = 0
        for row in self.tile:
            for elem in row:
                if elem == 1:
                    count += 1
        return count

    def __repr__(self):
        str_out = ''
        for row in self.tile:
            for elem in row:
                if elem == 0:
                    str_out += '.'
                if elem == 1:
                    str_out += '#'
                if elem == 2:
                    str_out += 'O'
            str_out += '\n'
        return str_out


def get_photo(ID, all_photos):
    return [pho for pho in all_photos if pho.ID == ID][0]


def mask_zone(search_zone):
    for y in range(len(search_zone)):
        for x in range(len(search_zone[0])):
            if search_zone[y, x] == 0 and monster_mask[y, x] == 1:
                return search_zone, False
    for y in range(len(search_zone)):
        for x in range(len(search_zone[0])):
            if monster_mask[y, x] == 1:
                search_zone[y, x] = 2
    return search_zone, True


def count_monster_waves(search_zone):
    count = 0
    for y in range(len(search_zone)):
        for x in range(len(search_zone[0])):
            if search_zone[y, x] == 1 and monster_mask[y, x] == 0:
                count += 1
            elif search_zone[y, x] == 0 and monster_mask[y, x] == 1:
                return 0
    return count


def part1(filename):
    data = readfile(filename)
    all_photos = [photo(tile) for tile in data]
    for i, phoi in enumerate(all_photos):
        for j, phoj in enumerate(all_photos[i+1:]):
            phoi.match_to_neighbour(phoj)

    answer = 1
    for pho in all_photos:
        if pho.num_unmatched() == 2:
            answer *= pho.ID
    print("The corner IDs multiply to {}.".format(answer))


def part2(filename):
    data = readfile(filename)
    all_photos = [photo(tile) for tile in data]
    for i, phoi in enumerate(all_photos):
        for j, phoj in enumerate(all_photos[i+1:]):
            phoi.match_to_neighbour(phoj)

    # Fudge factor
    for pho in all_photos:
        for key in pho.neighbours.keys():
            if len(pho.neighbours[key]) == 2:
                pho.neighbours[key] = [pho.neighbours[key][0]]

    full_photo_ID = np.zeros(shape=(12, 12), dtype='int')
    corners = [pho for pho in all_photos if pho.num_unmatched() == 2]
    top_left = corners[0]
    for op in operations:
        top_left.apply_op(op)
        if top_left.neighbours[2] == [] and top_left.neighbours[3] == []:
            break
    full_photo_ID[0, 0] = top_left.ID

    for i in range(len(full_photo_ID)):
        for j in range(len(full_photo_ID[i])):
            pho = get_photo(full_photo_ID[i, j], all_photos)
            # Right
            if j < len(full_photo_ID[i]) - 1:
                full_photo_ID[i, j+1] = pho.neighbours[1][0].ID
                phoR = get_photo(full_photo_ID[i, j+1], all_photos)
                for op in operations:
                    phoR.apply_op(op)
                    if pho.compare_boundary(phoR) == [1]:
                        break
            # Down
            if i < len(full_photo_ID) - 1:
                full_photo_ID[i+1, j] = pho.neighbours[4][0].ID
                phoD = get_photo(full_photo_ID[i+1, j], all_photos)
                for op in operations:
                    phoD.apply_op(op)
                    if pho.compare_boundary(phoD) == [4]:
                        break

    full_photo_tile = np.zeros(shape=(10*8+2*9, 10*8+2*9), dtype='int8')
    prev_i = 0
    prev_j = 0
    for i in range(len(full_photo_ID)):
        for j in range(len(full_photo_ID[i])):
            pho = get_photo(full_photo_ID[i, j], all_photos)
            rval = pho.get_borderless_tile()
            full_photo_tile[prev_i:prev_i+len(rval),
                            prev_j:prev_j+len(rval[0])] = rval
            prev_j = prev_j+len(rval[0])
            if j == len(full_photo_ID[i])-1:
                prev_i = prev_i+len(rval)
                prev_j = 0

    full_photo = photo(data[0])
    full_photo.ID = 0
    full_photo.tile = full_photo_tile
    for op in operations:
        full_photo.apply_op(op)
        found_monster = full_photo.full_mask()
        answer = full_photo.wave_count()
        if found_monster:
            break
    print("Total waves around monsters {}".format(answer))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day20.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day20.dat")
    timer.checkpoint_hit()

    timer.end_hit()
