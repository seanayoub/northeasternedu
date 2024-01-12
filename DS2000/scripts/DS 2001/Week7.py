"""
    DS 2001 Weekly Exercise 7
    Sean Ayoub
"""

import matplotlib.pyplot as plt

def read_data(filename):
    """
    Reads in data from a file.

    Parameters
    ----------
    filename : name of file.

    Returns
    -------
    List of strings (header)
    List of lists (data)
    
    """
    file = open(filename, "r")
    header = file.readline().split(",")
    header = [str(item) for item in header]
    
    data = []
    for line in file:
        line = line.split(",")
        row = [int(item) for item in line]
        data.append(row)
    file.close()
    return header, data

def plot_median(header, data):
    """
    Creates a line graph of the median household income data.

    Parameters
    ----------
    data : list of data.

    Returns
    -------
    Line graph.

    """
    plt.title("Household Income Over Time")
    plt.xlabel("Year")
    plt.ylabel("Median Household Income")
    x = header.index("50th (median)")
    year = []
    median_income = []
    for row in data:
        year.append(row[0])
        median_income.append(row[x])
    plt.show()

def plot_20_50_ratio(header, data):
    """
    Creates a line graph of how the 20th percentile/50th percentile ratio
    changes over time.

    Parameters
    ----------
    data : a list of data.

    Returns
    -------
    Line graph.

    """
    plt.title("Ratio 20/50")
    plt.xlabel("Year")
    plt.ylabel("Income Percentile")
    x = header.index("20th percentile limit")
    y = header.index("50th (median)")
    year = []
    ratio = []
    for row in data:
        year.append(row[0])
        ratio.append(row[x] / row[y])
    plt.show()
    
def plot_80_50_ratio(header, data):
    """
    Creates a line graph of how the 50th percentile/80th percentile ratio
    changes over time.

    Parameters
    ----------
    data : a list of data.

    Returns
    -------
    Line graph.

    """
    plt.title("Ratio 80/50")
    plt.xlabel("Year")
    plt.ylabel("Income Percentile")
    x = header.index("50th (median)")
    y = header.index("80th percentile limit")
    year = []
    ratio = []
    for row in data:
        year.append(row[0])
        ratio.append(row[x] / row[y])
    plt.show()

def plot_percentiles(header, data):
    """
    Creates a line graph of how each income percentile changes over time.

    Parameters
    ----------
    header : list of headers.
    data : a list of data.

    Returns
    -------
    Line Graph

    """
    plt.title("Income Percentiles and Change Over Time")
    plt.xlabel("Years")
    plt.ylabel("Income Percentage")
    
    count = 0
    while count < len(data):
        row = data[count]
        count2 = 1
        while count2 < 11:
            plt.plot(row[0], row[count2], label = header[count2])
            count2 += 1
        count += 1
    plt.legend()
    plt.show()
    
def main():
# Q1
    header, data = read_data("TableA4.csv")
    
# Q2
    plot_median(header, data)
    
# Q3
    plot_20_50_ratio(header, data)

# Q4
    plot_80_50_ratio(header, data)
    
# Q5
    plot_percentiles(header, data)
main()