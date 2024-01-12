"""
    Sean Ayoub
    DS 2000
    Homework 1
    September 16, 2022
"""

def main():
    p = int(input("Principal loan amount: "))
    i = float(input("Annual interest rate: "))
    y = int(input("Loan term (years): "))
    
    r = i / 12
    n = y * 12
    payment = round((p * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1), 2)

    print()
    print("Monthly payment: {0}". format(payment))
main()