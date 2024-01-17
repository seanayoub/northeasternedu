"""
    DS 2001 Weekly Exercise 2
    Sean Ayoub
"""

def main():
# Q1
    salary = float(input("What is your current salary?"))
    contribution = salary * 0.05
    print("You should contribute")
    print(contribution)
    print()
    
# Q2
    company_contribution = salary * 0.1
    print("The company's contribution will be")
    print(company_contribution)
    
# Q3
    salary = int(input("What is your current salary?"))
    employee_contribution = float(input("What percentage of your salary are you contributing?"))
    company_percentage = float(input("What percentage of your salary is your company contributing?"))
    total_amount = salary * (employee_contribution + company_percentage)
    print(total_amount)
    
# Q4
    year2 = total_amount * 1.02 + total_amount
    year3 = year2 * 1.02 + total_amount
    print(round(year3, 2))
    
    balance = total_amount * (1.02 ** 2 + 1.02 + 1)
    print(round(balance, 2))
    
# Q5
    months = balance // 200
    remaining_balance = balance % 200
    print("Number of months is:", months, "Remaining balance is:", round(remaining_balance, 1))
main()
