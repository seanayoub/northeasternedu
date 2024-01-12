"""
    Sean Ayoub
    DS 2000
    Homework 1
    September 16, 2022
"""

def main():
    d = int(input("Enter distance [miles]: "))

    km = d * 1.61
    m = km* 1000

    sec = m / 299792458
    sec = sec % (24 * 3600)
    hours = sec // 3600
    sec %= 3600
    mins = sec // 60
    sec %= 60

    print("Light travel time: {0}h {1}m {2}s". 
          format(int(hours), int(mins), round(sec, 1)))
main()