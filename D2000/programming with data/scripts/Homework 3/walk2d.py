"""
    Sean Ayoub
    DS 2000
    Homework 3
    September 30, 2022
"""

import matplotlib.pyplot as plt
import random as rnd

def main():
    count = 0
    x = 0
    y = 0
    
    while count < 1000:
        plt.plot(x, y, ",", color = "gray")
        mvt = rnd.randint(1, 6)
        if mvt <= 2:
            x -= 1
        elif mvt <= 4:
            x += 1
        elif mvt == 5:
            y -= 1
        else:
            y += 1
        count += 1
    
    plt.title("Squirrel's Walk - Part Two")
    plt.xlabel("West <-> East")
    plt.ylabel("South <-> North")
    plt.show()
    plt.savefig("walk2d.png", bbox_inches = "tight")   
main()