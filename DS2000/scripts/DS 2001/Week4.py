"""
    DS 2001 Weekly Exercise 4
    Sean Ayoub
"""

import matplotlib.pyplot as plt
import random as rnd

def main():
# Q1
    date = []
    views = []
    highviews = []
    pusheen = open("pusheen.txt", "r")
    line = pusheen.readline()
    while line.strip() != "":
        if int(line) <= 31:
            date.append(str(line))
        else:
            views.append(int(line))
            if int(line) >= 10000:
                highviews.append(line)
        line = pusheen.readline()
    pusheen.close

    print(len(highviews))

# Q2
    average = sum(views) / len(views)
    print()
    print("The average daily viewership is: ", round(average))

# Q3
    plt.title("Daily Viewership")
    plt.xlabel("Date")
    plt.ylabel("Views")
    x = 0
    while x < 31:
        plt.plot(date[x], views[x], "o-")
        x += 1
    plt.show()    

# Q4
    print()
    print("The lucky fans are: ")
    fandrawing = 0
    while fandrawing < 10:
        fan = rnd.randint(1, 80000)
        print(fan)
        fandrawing += 1

# Q5
    plushietype = 1
    while plushietype < 4:
        print()
        print("The lucky fans for type", plushietype, "are: ")
        fandrawing = 0
        while fandrawing < 10:
            fan = rnd.randint(1, 80000)
            print(fan)
            fandrawing += 1
        plushietype += 1
main()