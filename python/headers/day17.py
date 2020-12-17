# -*- coding: utf-8 -*-
"""
Day 17 of Advent of Code 2020


Tom Kite - 17/12/2020
"""


def readfile(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


def process_initial_layer_3D(layer):
    cube_locs = []
    counts_dict = {}
    for j, row in enumerate(layer):
        for i, col in enumerate(row):
            if col == '#':
                cube_locs.append((i, j, 0))
                counts_dict = add_to_counts_dict_3D((i, j, 0), counts_dict)
    return cube_locs, counts_dict


def add_to_counts_dict_3D(coords, counts_dict):
    x, y, z = coords
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if i == x and j == y and k == z:
                    continue
                if (i, j, k) not in counts_dict.keys():
                    counts_dict[(i, j, k)] = 1
                else:
                    counts_dict[(i, j, k)] += 1
    return counts_dict


def evolve_pocket_dim_3D(cube_locs, counts_dict):
    new_cube_locs = []
    new_counts_dict = {}
    xmin = min(cube_locs, key=lambda c: c[0])[0]
    xmax = max(cube_locs, key=lambda c: c[0])[0]
    ymin = min(cube_locs, key=lambda c: c[1])[1]
    ymax = max(cube_locs, key=lambda c: c[1])[1]
    zmin = min(cube_locs, key=lambda c: c[2])[2]
    zmax = max(cube_locs, key=lambda c: c[2])[2]

    for i in range(xmin-1, xmax+2):
        for j in range(ymin-1, ymax+2):
            for k in range(zmin-1, zmax+2):
                if (i, j, k) in counts_dict.keys():
                    count = counts_dict[(i, j, k)]
                else:
                    count = 0
                if (i, j, k) in cube_locs:
                    if count == 2 or count == 3:
                        new_cube_locs.append((i, j, k))
                        new_counts_dict = \
                            add_to_counts_dict_3D((i, j, k), new_counts_dict)
                elif count == 3:
                    new_cube_locs.append((i, j, k))
                    new_counts_dict = \
                        add_to_counts_dict_3D((i, j, k), new_counts_dict)
    return new_cube_locs, new_counts_dict


def process_initial_layer_4D(layer):
    cube_locs = []
    counts_dict = {}
    for j, row in enumerate(layer):
        for i, col in enumerate(row):
            if col == '#':
                cube_locs.append((i, j, 0, 0))
                counts_dict = add_to_counts_dict_4D((i, j, 0, 0), counts_dict)
    return cube_locs, counts_dict


def add_to_counts_dict_4D(coords, counts_dict):
    x, y, z, w = coords
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for e in range(w-1, w+2):
                    if i == x and j == y and k == z and e == w:
                        continue
                    if (i, j, k, e) not in counts_dict.keys():
                        counts_dict[(i, j, k, e)] = 1
                    else:
                        counts_dict[(i, j, k, e)] += 1
    return counts_dict


def evolve_pocket_dim_4D(cube_locs, counts_dict):
    new_cube_locs = []
    new_counts_dict = {}
    xmin = min(cube_locs, key=lambda c: c[0])[0]
    xmax = max(cube_locs, key=lambda c: c[0])[0]
    ymin = min(cube_locs, key=lambda c: c[1])[1]
    ymax = max(cube_locs, key=lambda c: c[1])[1]
    zmin = min(cube_locs, key=lambda c: c[2])[2]
    zmax = max(cube_locs, key=lambda c: c[2])[2]
    wmin = min(cube_locs, key=lambda c: c[3])[3]
    wmax = max(cube_locs, key=lambda c: c[3])[3]

    for i in range(xmin-1, xmax+2):
        for j in range(ymin-1, ymax+2):
            for k in range(zmin-1, zmax+2):
                for e in range(wmin-1, wmax+2):
                    if (i, j, k, e) in counts_dict.keys():
                        count = counts_dict[(i, j, k, e)]
                    else:
                        count = 0
                    if (i, j, k, e) in cube_locs:
                        if count == 2 or count == 3:
                            new_cube_locs.append((i, j, k, e))
                            new_counts_dict = \
                                add_to_counts_dict_4D((i, j, k, e),
                                                      new_counts_dict)
                    elif count == 3:
                        new_cube_locs.append((i, j, k, e))
                        new_counts_dict = \
                            add_to_counts_dict_4D((i, j, k, e),
                                                  new_counts_dict)
    return new_cube_locs, new_counts_dict


def part1(filename):
    data = readfile(filename)
    cube_locs, counts_dict = process_initial_layer_3D(data)
    for _ in range(6):
        cube_locs, counts_dict = evolve_pocket_dim_3D(cube_locs, counts_dict)
    print("After 6 cycles there are {} active cubes."
          .format(len(cube_locs)))
    return


def part2(filename):
    data = readfile(filename)
    cube_locs, counts_dict = process_initial_layer_4D(data)
    for i in range(6):
        print(i, '/', '6')
        cube_locs, counts_dict = evolve_pocket_dim_4D(cube_locs, counts_dict)
    print("After 6 cycles there are {} active cubes."
          .format(len(cube_locs)))
    return


if __name__ == "__main__":
    print("Part 1:")
    part1("../../data/day17.dat")
    print("\nPart 2:")
    part2("../../data/day17.dat")
