"""
    Sean Ayoub
    DS 2000
    Homework 2
    September 21, 2022
"""

def main():
    file = input("Which donut rating file? ")
    
    with open(file) as f:
        data = f.readlines()
        data = data[1:8:2]
        data = [item.replace("\n", " ") for item in data]
        data = [float(item) for item in data]
        high = max(data)
        low = min(data)
    
    print()
    print("Best donut rating: ", high)
    print("Worst donut rating: ", low)
main()