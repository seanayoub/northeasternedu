"""
    Sean Ayoub
    DS 2000
    Homework 4
    October 7, 2022
"""

import matplotlib.pyplot as plt

def main():
    unique = []
    nbd = []
    lat = []
    long = []
    
    with open("rodents_311_2021.csv") as f:
        f.readline()
        for line in f:
            row = line.split(",")
            if row[0] not in nbd:
                unique.append(row[0])
            nbd.append(row[0])
            lat.append(float(row[1]))
            long.append(float(row[2])) 
    unique.sort()
    
    print("Total number of reports: {0}". format(len(nbd)))
    print("Neighborhoods: ")
    for i in range(len(unique)):
        print(unique[i])
    print("Average number of reports: {0}". format(len(nbd)/len(unique)))
    
    plt.plot(-71.0875, 42.3367, "*", color = "r", 
             markersize = 12.0, label = "Northeastern")
    plt.plot(long, lat, ".", color = "gray", label = "Rodent Reports")
    plt.title("Map of Rodent Reports in Boston")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.xlim(min(long) - .04, max(long) + .04)
    plt.legend()
    plt.show()
    
    plt.figure()
    reportcount = []
    for item in unique:
        n = nbd.count(item)
        reportcount.append(n)
    plt.bar(unique, reportcount)
    plt.title("Rodent Report Comparison for Neighborhoods")
    plt.xlabel("Neighborhoods")
    plt.ylabel("Rodent Report Count")
    plt.ylim(0, max(reportcount) + 15)
    plt.xticks(rotation = 90)
    plt.show()
main()