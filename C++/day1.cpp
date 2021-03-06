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

using namespace std;

vector<int> read_data(string filename)
{
    ifstream ifile;
    ifile.open(filename);

    if (!ifile) { throw; }

    vector<int> data{};
    string line;
    while (getline(ifile, line))
    {
        data.push_back(stoi(line));
    }
    ifile.close();
    return data;
}

int find_2_sum(vector<int> data, int total=2020)
{
    for (int i{0}; i<data.size(); i++)
    {
        for (int j{i+1}; j<data.size(); j++)
        {
            if (data[i] + data[j] == total){ return data[i] * data[j]; }
        }
    }
    return -1;
}

int find_3_sum(vector<int> data, int total=2020)
{
    for (int i{0}; i<data.size(); i++)
    {
        for (int j{i+1}; j<data.size(); j++)
        {
            if (data[i] + data[j] >= total) { continue; }
            for (int k{j+1}; k<data.size(); k++)
            {
                if (data[i] + data[j] + data[k] == total)
                {
                    return data[i] * data[j] * data[k];
                }
            }
        }
    }
    return -1;
}

int main()
{
    vector<int> data;
    try { data = read_data("../data/day1.dat"); }
    catch (...) { cout << "Could not open file!" << endl; return 1; }

    cout << find_2_sum(data) << endl;
    cout << find_3_sum(data) << endl;

    return 0;
}
