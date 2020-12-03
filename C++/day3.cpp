/*
Advent of Code 2020 - Day 1

This code will search through a list of numbers and return the product of
the two or three that add to 2020

Tom Kite - 01/12/20
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


vector<string> read_data(string filename)
{
    ifstream ifile;
    ifile.open(filename);
    if (!ifile) { throw; }

    vector<string> data{};
    string line;
    while (getline(ifile, line))
    {
        data.push_back(line);
    }
    ifile.close();
    return data;
}

class coord
{
public:
    int x,y;

    coord(int x_in, int y_in)
    {
        x = x_in;
        y = y_in;
    }

    coord operator+(coord other)
    {
        return coord(x + other.x, y + other.y);
    }
};

bool check_tree(vector<string> tree_map, coord position)
{
    int x_eff = position.x % tree_map[0].size();
    return tree_map[position.y][x_eff] == '#';
}

bool in_map(vector<string> tree_map, coord position)
{
    return position.y < tree_map.size();
}

int full_slide(vector<string> tree_map, coord grad, coord pos=coord{0,0})
{
    int tree_count{0};
    while (in_map(tree_map, pos))
    {
        if (check_tree(tree_map, pos)) tree_count++;
        pos = pos + grad;
    }
    return tree_count;
}

int main()
{
    vector<string> data;
    try { data = read_data("../data/day3.dat"); }
    catch (...) { cout << "Could not open file!" << endl; return 1; }

    long long int part_1{0};
    long long int part_2{1};

    part_1 = full_slide(data, coord{3, 1});

    vector<coord> grads;
    grads.push_back(coord{1,1});
    grads.push_back(coord{3,1});
    grads.push_back(coord{5,1});
    grads.push_back(coord{7,1});
    grads.push_back(coord{1,2});

    for (int i{0}; i<grads.size(); i++)
    {
        part_2 *= full_slide(data, grads[i]);
    }

    cout << part_1 << " " << part_2 << endl;

    return 0;
}
