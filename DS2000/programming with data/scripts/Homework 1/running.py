"""
    Sean Ayoub
    DS 2000
    Homework 1
    September 16, 2022
"""

def main():
    distance = float(input("Enter your running distance in kilometers: "))
    minutes = float(input("Enter your running time - minutes: "))
    seconds = float(input("Enter your running time - seconds: "))

    m = distance / 1.61
    s = ((minutes * 60) + seconds) / m
    x = round(s / 60)
    y = round(s % 60, 1)

    print()
    print("Your average pace was {0} minutes and {1} seconds per mile.". 
          format(x, y)) 
main()