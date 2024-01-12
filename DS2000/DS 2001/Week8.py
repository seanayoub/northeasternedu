"""
    DS 2001 Weekly Exercise 8
    Sean Ayoub 

"""

def main():
# Q1
    beverage_category = []
    beverage = []
    beverage_prep = []
    calorie = []
    
    f = open("starbucks_menu.csv", "r")
    f.readline()
    
    for line in f:
        vals = line.strip().split(",")
        beverage_category.append(vals[0])
        beverage.append(vals[1])
        beverage_prep.append(vals[2])
        calorie.append(int(vals[3])) 
    f.close()
    
# Q2
    categorycount = {}
    for item in beverage_category:
        if item not in categorycount:
            categorycount[item] = 1
        else:
            categorycount[item] = categorycount[item] + 1
    print(categorycount)
    
# Q3
    calorie_total = {}
    for i in range(len(beverage_category)):
        if beverage_category[i] in calorie_total:
            calorie_total[beverage_category[i]] += calorie[i]
        else:
            calorie_total[beverage_category[i]] = calorie[i]
            
    average = {x : round(calorie_total[x] / 
                         categorycount[x], 2) for x in categorycount}
    print()
    print(average)
main()