"""
    Sean Ayoub
    DS 2000
    Homework 2
    September 21, 2022
"""

def readdata(file):
    """
    Reads in donut data.

    Parameters
    ----------
    file : a txt with donut data

    Returns
    -------
    x : donut price
    y : donut cost
    
    """
    with open(file) as f:
        x = float(f.readline())
        y = float(f.readline())
    return x, y

def calculate(n, p, c):
    """
    Performs calculations using donut data.

    Parameters
    ----------
    n : number of donuts
    p : donut price
    c : donut cost

    Returns
    -------
    tp : total price of the order
    pft : company's total profit from the transaction

    """
    tp = p * n
    tc = c * n
    pft = round(tp - tc, 2)
    return tp, pft

def main():
    donut = input("Which donuts would you like [glazed, chocolate, sprinkled]? ")
    n = int(input("How many donuts would you like? "))
    
    if donut == "glazed":
        p, c = readdata("glazed.txt")
        tprice, profit = calculate(n, p, c)
    
    elif donut == "chocolate":
        p, c = readdata("chocolate.txt")
        tprice, profit = calculate(n, p, c)
        
    elif donut == "sprinkled":
        p, c = readdata("sprinkled.txt")
        tprice, profit = calculate(n, p, c)
    
    print()
    print("Please pay: ${0}". format(tprice))
    print("This sale made us ${0}!". format(profit))
    print("Enjoy your donuts!")
main()