# -*- coding: utf-8 -*-
"""
Day 22 of Advent of Code 2020


Tom Kite - 22/12/2020
"""

from aoc_tools.advent_timer import Advent_Timer


def readfile(filename):
    with open(filename, 'r') as file:
        players = file.read().split('\n\n')
    return [[int(x) for x in cards.strip().split('\n')[1:]]
            for cards in players]


class combat:
    def __init__(self, player1_in, player2_in):
        self.player1 = player1_in
        self.player2 = player2_in

    def _evolve_game_step(self):
        cards = [self.player1.pop(0), self.player2.pop(0)]
        if cards[0] > cards[1]:
            self.player1 += cards
        else:
            cards.reverse()
            self.player2 += cards

    def finish_game(self):
        while len(self.player1) and len(self.player2):
            self._evolve_game_step()

    def get_winning_score(self):
        total = [0, 0]
        for i, player in enumerate([self.player1, self.player2]):
            for j, card in enumerate(player):
                total[i] += (len(player)-j)*card
        return max(total)


class recursive_combat:
    def __init__(self, player1_in, player2_in):
        self.player1 = player1_in
        self.player2 = player2_in
        self.prev_states = set()
        self.winner = None

    def _evolve_game_step(self):
        # Check for game end
        if self.winner is not None:
            return

        # Extract cards
        cards = [self.player1.pop(0), self.player2.pop(0)]
        round_win = None

        if cards[0] <= len(self.player1) and cards[1] <= len(self.player2):
            # Recursive game
            sub_game = recursive_combat(self.player1[:cards[0]],
                                        self.player2[:cards[1]])
            sub_game.finish_game()
            round_win = sub_game.winner
        else:
            # Regular game
            if cards[0] > cards[1]:
                round_win = 1
            else:
                round_win = 2

        # Apply winner
        if round_win == 1:
            self.player1 += cards
        else:
            cards.reverse()
            self.player2 += cards

        # Check for other conditions
        if not len(self.player1):
            self.winner = 2
            return
        if not len(self.player2):
            self.winner = 1
            return
        game_state = (tuple(self.player1), tuple(self.player2))
        if game_state in self.prev_states:
            self.winner = 1
        else:
            self.prev_states.add(game_state)
        return

    def finish_game(self):
        while self.winner is None:
            self._evolve_game_step()

    def get_winning_score(self):
        total = [0, 0]
        for i, player in enumerate([self.player1, self.player2]):
            for j, card in enumerate(player):
                total[i] += (len(player)-j)*card
        return max(total)


def part1(filename):
    player1, player2 = readfile(filename)

    my_game = combat(player1, player2)
    my_game.finish_game()

    print("Final winning score is {}.".format(my_game.get_winning_score()))


def part2(filename):
    player1, player2 = readfile(filename)

    my_game = recursive_combat(player1, player2)
    my_game.finish_game()

    print("Final winning score is {}.".format(my_game.get_winning_score()))


if __name__ == "__main__":
    timer = Advent_Timer()

    print("Part 1:")
    part1("../../data/day22.dat")
    timer.checkpoint_hit()

    print("\nPart 2:")
    part2("../../data/day22.dat")
    timer.checkpoint_hit()

    timer.end_hit()
