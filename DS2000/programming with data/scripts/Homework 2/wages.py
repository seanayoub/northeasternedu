"""
    Sean Ayoub
    DS 2000
    Homework 2
    September 21, 2022
"""

def readfile(filename):
    """
    Reads data from a file into a list

    Parameters
    ----------
    filename : name of file

    Returns
    -------
    data : a list of the data

    """
    with open(filename) as f:
        data = [float(item) for item in f]
    return data

def calculate(lsa, lsb):
    """
    Does a set of calculations on two lists.

    Parameters
    ----------
    lsa : list one.
    lsb : list two.

    Returns
    -------
    tpft : total profit for the day.
    hrs : number of hours the employees worked.
    wage : how much the employees should receive per hour.

    """
    tpft = lsa[0] + lsa[1] + lsa[2]
    hrs = lsb[0] * lsb[1]
    wage = round(tpft / hrs, 2)
    return tpft, hrs, wage

def main():
    day = input("What day should we analyze? ")
    profit = readfile("profits_" + day + ".txt")
    employees = readfile("employees_" + day + ".txt")
    tpft, hrs, wage = calculate(profit, employees)
    
    print()
    print("On {0}, you made ${1}". format(day, tpft))
    print("{0} employees worked for {1} hours each, totaling {2} hours.". 
          format(int(employees[0]), int(employees[1]), int(hrs)))
    print("You should pay your employees ${0} per hour". format(wage))  
main()