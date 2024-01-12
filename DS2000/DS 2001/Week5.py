"""
    DS 2001 Weekly Exercise 5
    Sean Ayoub
"""

import matplotlib.pyplot as plt

def main():
# Q1
    category = []
    uniquecategory = []
    name = []
    prep = []
    calories = []
    
    starbucks = open("starbucks_menu.csv", "r")
    starbucks.readline()
    for line in starbucks:
        columns = line.split(",")
        if columns[0] not in category:
            uniquecategory.append(columns[0])
        category.append(columns[0])
        name.append(columns[1])
        prep.append(columns[2])
        calories.append(int(columns[3]))
    starbucks.close()

# Q2
    print("There are", len(uniquecategory), "categories in total.")
    print(uniquecategory)
    
# Q3
    number = [] # number drinks of each type
    for line in uniquecategory:
        x = category.count(line)
        number.append(x)
    print()
    print(number)
    
# Q4
    x = 0 # moves through calorie list
    y = 0 # moves through index in number list
    averagecalories = []
    for line in uniquecategory:
        z = 0 # iterations of loop
        values = []
        while z < number[y]:
            c = calories[x]
            values.append(c)
            x += 1 
            z += 1
        a = sum(values)/number[y]
        averagecalories.append(a)
        y += 1

# Q5
    plt.title("Average Calories per Drink")
    plt.xlabel("Category")
    plt.ylabel("Calories")
    plt.ylim(0, max(averagecalories) + 5)
    plt.bar(uniquecategory, averagecalories)
    plt.xticks(rotation = 90)
    plt.show()
main()