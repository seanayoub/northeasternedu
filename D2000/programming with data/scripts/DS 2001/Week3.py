"""
    DS 2001 Weekly Exercise 3
    Sean Ayoub
"""

import matplotlib.pyplot as plt

def main():
# Q1
    status = input("open or close? ")
    
    file = open("jan_2022_" + status + ".txt", "r")
    jan_18 = file.readline()
    second = float(file.readline())
    jan_19 = file.readline()
    fourth = float(file.readline())
    jan_20 = file.readline()
    sixth = float(file.readline())
    file.close()

# Q2
    print()
    print("The highest", status, "price was", max(second, fourth, sixth))
    print("The lowest", status, "price was", min(second, fourth, sixth))
    
# Q3
    if fourth > second:
        difference = fourth - second
        print()
        print("Apple's stock price increased by",
              round(difference, 2), "on Jan. 19")
        
    else:
        difference = second - fourth
        print()
        print("Apple's stock price decreased by", 
              round(difference, 2), "on Jan. 19")

# Q4 and Q5
    plt.title("Apple's Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.plot(jan_18, second, "o", color = "green")
    plt.plot(jan_19, fourth, ".", color = "red")
    plt.plot(jan_20, sixth, "s", color = "red")
    plt.show()

main()