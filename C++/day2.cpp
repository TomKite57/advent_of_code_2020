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


class password
{
public:
    int num1, num2;
    string letter, pwd;

    password(string str_in)
    {
        int colon_ind = str_in.find(':');
        int dash_ind = str_in.find('-');

        num1 = stoi(str_in.substr(0, dash_ind));
        num2 = stoi(str_in.substr(dash_ind+1, colon_ind-dash_ind-3));
        letter = str_in.substr(colon_ind-1, 1);
        pwd = str_in.substr(colon_ind+2, str_in.size()-colon_ind-2);

        return;
    }

    bool part_1_valid()
    {
        int letter_count{0};
        for (int i{0}; i<pwd.size(); i++)
        {
            if (pwd.substr(i,1) == letter) letter_count++;
        }
        return (num1 <= letter_count && letter_count <= num2);
    }

    bool part_2_valid()
    {
        int letter_count{0};
        if (pwd.substr(num1-1, 1) == letter) letter_count+=1;
        if (pwd.substr(num2-1, 1) == letter) letter_count+=1;
        return letter_count == 1;
    }
};


int main()
{
    vector<string> data;
    try { data = read_data("../data/day2.dat"); }
    catch (...) { cout << "Could not open file!" << endl; return 1; }

    vector<password> passwords;
    for (int i{0}; i<data.size(); i++)
    {
        passwords.push_back(password(data[i]));
    }

    int part_1_ans{0};
    int part_2_ans{0};

    for_each(passwords.begin(),
             passwords.end(),
             [&part_1_ans](password pwd)
                {if (pwd.part_1_valid()) part_1_ans++;}
            );

    for_each(passwords.begin(),
             passwords.end(),
             [&part_2_ans](password pwd)
                {if (pwd.part_2_valid()) part_2_ans++;}
            );

    cout << part_1_ans << " " << part_2_ans << endl;

    return 0;
}
