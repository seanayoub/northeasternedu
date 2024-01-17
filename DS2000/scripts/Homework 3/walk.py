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
    position = 0
    
    while count < 1000:
        plt.plot(count, position, ",", color = "gray")
        movement = rnd.randint(0, 1)
        if movement == 0:
            position -= 1
        else:
            position += 1
        count += 1
    
    plt.title("Squirrel's Walk")
    plt.xlabel("Time in Seconds")
    plt.ylabel("Position")
    plt.show()
    plt.savefig("walk.png", bbox_inches = "tight")   
main()