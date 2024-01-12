"""
    Sean Ayoub
    February 3, 2023
    Professor Higger
    Homework 0
"""

import random as rnd
from pprint import pprint as p
from collections import defaultdict

def draw_value():
    """ draws a random card from a pile, only numbered cards 1 - 10.

    returns
    -------
    card (int): the numeral value of the card drawn

    """
    card = rnd.choices(range(1, 11), weights = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3))
    return int(card[0])

def update_round(jar, frac0, frac1):
    """ runs a round of triple-or-nothing
    
    arguments:
    -------
    jar (float): number of coins in the jar at round start
    frac0 (float): player0's fraction bet
    frac1 (float): player1's fraction bet
            
    returns:
    -------
    jar (float): number of coins in the jar at end of round
    new_coin0 (float): number of coins player0 has earned in this round
    new_coin1 (float): number of coins player1 has earned in this round
    
    """
    # check that both fraction inputs are valid
    assert 0 <= frac0 <= 1, 'invalid input: frac0'
    assert 0 <= frac1 <= 1, 'invalid input: frac1'
    
    # conduct round
    if frac0 == frac1:
        amt = ((2 - frac0) * frac0 * jar)
        new_coin0 = amt / 2
        new_coin1 = new_coin0
        jar -= amt
        
    elif frac0 < frac1:
        new_coin0 = frac0 * jar
        jar = jar - new_coin0
        new_coin1 = frac1 * jar
        jar = jar - new_coin1
        
    else: 
        new_coin1 = frac1 * jar
        jar = jar - new_coin1
        new_coin0 = frac0 * jar
        jar = jar - new_coin0
    
    jar *= 3
    return jar, new_coin0, new_coin1
      
def triple_nothing_player(jar, frac_hist_opp, frac_hist_self):
    """ produces a fraction in a game of triple or nothing
    
    frac_hist objects are lists of previous fraction history in
    the game.  for example, frac_hist = [0, .01, .2] indicates
    a player had fraction 0 in the first round, .01 in the second
    and .2 in the third
    
    args:
    -------
        jar (float): value of the jar in current round
        frac_hist_opp (list): history of all fractions input by opposing player
        frac_hist_self (list): history of all fractions input by self
            
    returns:
    -------
        frac (float): fraction for current round
        name (str): a unique name given to your strategy
    """
    name = "Average Guess?"
    opp = sum(frac_hist_opp) / len(frac_hist_opp)
    user = sum(frac_hist_self) / len(frac_hist_self)
    frac = (user + opp) / 2
    return frac, name

def main():
    # Part 1.2.2
    card_count = defaultdict(int)
    
    for i in range(10000):
        card = draw_value()
        card_count[card] += 1
    
    print(card_count[10] / 10000)
    
    # Part 1.2.3
    num_bust_per_start = defaultdict(int)
    
    for i in range(10, 22):
        for a in range(10000):  
            start = draw_value()
            if i + start > 21:
                num_bust_per_start[i] += 1
    
    # Part 1.2.4
    prob_bust_per_start = defaultdict(int)
    
    for item in num_bust_per_start:
        prob_bust_per_start[item] = round(
            ((num_bust_per_start[item] / 10000) * 100), 2)
    
    p(prob_bust_per_start)
main()