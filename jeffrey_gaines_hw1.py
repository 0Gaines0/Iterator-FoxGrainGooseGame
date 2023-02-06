#!/usr/bin/env python3
"""
    Script for homework 1
    fox goose grain
"""
__author__ = 'Jeffrey Gaines'
__version__ = 'Fall/Spring 2023'
__pylint__ = '2.14.5'

import itertools as itr


#(1, 1, 1, 1) = (Farmer, Fox, Goose, Grain)
def fox_goose_grain_outcomes():
    """Generates and stores all possible states of (0,0,0,0) to (1,1,1,1)

    Returns:
        list: all possible outcomes of farmer/fox/goose/grain game
    """
    outcomes = list(tuple(itr.product([0,1], repeat=4)))
    all_outcomes = []
    for combination in outcomes:
        all_outcomes.append(combination)
    return list(all_outcomes)

def sliding_puzzle_game():
    """Generates and stores all possible states of the 8 puzzle game
      Returns:
        list: all possible out comes of 8 puzzle game
    """
    outcomes = list(tuple(itr.permutations(range(9), 9)))

    all_outcomes = []
    for combination in outcomes:
        all_outcomes.append(combination)
    return list(all_outcomes)

if __name__ == '__main__':
    fox_goose_grain_outcomes()
    sliding_puzzle_game()
