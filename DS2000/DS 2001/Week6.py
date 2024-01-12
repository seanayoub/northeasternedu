"""
    DS 2001 Weekly Exercise 6
    Sean Ayoub
"""

import matplotlib.pyplot as plt

def read_data(filename):
    """
    reads data from a file and converts it into a list of floats

    Parameters
    ----------
    filename : name of file that needs to be read, enter as a string

    Returns
    -------
    a list of floats
    
    """
    
    file = open(filename, "r")
    data = file.readline().split(",")
    data = [float(item) for item in data]
    file.close()
    return data

def annual_contribution(salary, employee_contribution, company_contribution):
    """
    will calculate the annual contribution amount

    Parameters
    ----------
    salary : salary amount
    employee_contribution : employee's contribution percentage as a decimal
    company_contribution : company's contribution percentage as a decimal

    Returns
    -------
    annual contribution amount
    
    """

    employee = salary * employee_contribution
    company = salary * company_contribution
    annual = int(employee + company)
    return annual

def calc_balance(ls, annual_interest_rate):
    """
    will return the account balance at the end of each year as a list of floats

    Parameters
    ----------
    ls : a list of data
    annual_interest_rate : annual interest rate, float

    Returns
    -------
    balance_list : a list of the account balances at the end of each year

    """
    salary = ls[0]
    employee_contribution = ls[1]
    company_contribution = ls[2]
    years = ls[3]
    
    yearly_contribution = annual_contribution(salary, employee_contribution, 
                                              company_contribution)
    balance_list = []
    balance = 0
    for x in range(int(years)):
        balance = balance * (1 + annual_interest_rate) + yearly_contribution
        balance_list.append(balance)
    
    return balance_list

def withdrawal(ls, balance_list):
    """
    list[# of months person can withdraw from the acct, remaining balance]

    Parameters
    ----------
    ls : a list of data
    balance_list : the balance list

    Returns
    -------
    list

    """
    monthly_withdrawal = ls[4]
    number_months = balance_list[-1] // monthly_withdrawal
    remaining_balance = balance_list[-1] % monthly_withdrawal
    return [number_months, round(remaining_balance, 2)]
    
def plot_balance(ls):
    """
    creates a bar plot.

    Parameters
    ----------
    ls : a list of data

    Returns
    -------
    None.

    """
    plt.title("Retirement Account Balances")
    plt.xlabel("Interest Rate")
    plt.ylabel("Balance")
    for interest in range(11):
        balance = calc_balance(ls, interest / 100)
        plt.bar(interest, balance[-1],)
    plt.show()
    
def main():
# Q1
    data = read_data("pension.txt")
    print(data)
    
# Q2
    print()
    print(annual_contribution(data[0], data[1], data[2]))
    
# Q3
    balance_list = calc_balance(data, 0.02)
    
# Q4
    print()
    print(withdrawal(data, balance_list))

# Q5
    plot_balance(data)
main()