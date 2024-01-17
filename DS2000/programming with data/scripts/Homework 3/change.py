"""
    Sean Ayoub
    DS 2000
    Homework 3
    September 30, 2022
"""

def main():
    price = int(input("Enter price in cents [0 - 100]: "))
    
    if price < 0 or price > 100:
        print("Please enter a value between [0 - 100]")
    
    else:
        change = 100 - price
        print("Change to be given {0}". format(change))
        
        if change >= 25:
            q = change // 25
            change = change - (q * 25)
            print("Quarters: {0}". format(q))
            
        if change >= 10:
            d = change // 10
            change = change - (d * 10)
            print("Dimes: {0}". format(d))
        
        if change >= 5:
            n = change // 5
            change = change - (n * 5)
            print("Nickels: {0}". format(n))
            
        if change >= 1:
            print("Pennies: {0}". format(change))        
main()