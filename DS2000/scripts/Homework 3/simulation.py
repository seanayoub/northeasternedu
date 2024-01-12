"""
    Sean Ayoub
    DS 2000
    Homework 3
    September 30, 2022
"""

import random as rnd

def main():
    simcount = 1
    while simcount < 5:
        count = 0
        diff = 0
        while count < (10 ** simcount):
            r1 = rnd.randint(1, 6)
            r2 = rnd.randint(1, 6)
            r3 = rnd.randint(1, 6)
            if not r1 == r2 or r1 == r3 or r2 == r3:
                diff += 1
            count += 1
        p = diff / count
        print("Rolling dice {0} times". format(10 ** simcount))
        print("Number of mis-matched rolls: {0}". format(diff))
        print("Experimental Probability: ", round(p, 4))
        print()
        simcount += 1
main()