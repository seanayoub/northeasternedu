"""
    Sean Ayoub
    DS 2000
    Homework 6
    October 28, 2022
    
    Reads in data about heart disease. Runs calculations to answer questions
    about the data. Makes a scatterplot.
"""

import matplotlib.pyplot as plt

def read_data(filename):
    """
    Reads in data from a file.

    Parameters
    ----------
    filename : name of file as a string

    Returns
    -------
    data : a lists of lists with the data.

    """
    with open(filename) as f:
        f.readline()
        data = []
        for line in f:
            line = line.split(",")
            row = [item for item in line]
            age = int(row[0])
            sex = row[1]
            paintype = row[2]
            restingbp = int(row[3])
            cholesterol = int(row[4])
            maxhr = int(row[5])
            heartdiseases = int(row[6])
            row = [age, sex, paintype, restingbp, cholesterol, 
               maxhr, heartdiseases]
            data.append(row)
    return data

def total_patients(ls):
    """
    Prints the total number of patients in the data.

    Parameters
    ----------
    ls : a list of data

    Returns
    -------
    Prints the number of patients.

    """
    print("Number of patients:", len(ls))

def heart_disease(ls):
    """
    Finds the total number of patientst who have heart disease

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Prints the number of patients with heart disease.

    """
    heart_disease = []
    for item in ls:
        if item[6] == 1:
            heart_disease.append(item[6])
        else:
            continue
    print("Number of patients with heart disease:", len(heart_disease))

def average_age(ls):
    """
    Finds the average age for all the patients.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Prints the average age for the patients.

    """
    ages = [item[0] for item in ls]
    average = sum(ages) / len(ages)
    print("Average age:", round(average))

def heart_average(ls):
    """
    Finds the average age of the patients who have heart disease.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Prints the average age.

    """
    ages = [item[0] for item in ls if item[6] == 1]
    average = sum(ages) / len(ages)
    print("Average age of patients with heart disease:", round(average))

def average_bp(ls):
    """
    Finds the average resting blood pressure for the patients.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Prints the average resting blood pressure.

    """
    bp = [item[3] for item in ls]
    average = sum(bp) / len(bp)
    print("Average resting blood pressure:", round(average))
    
def heart_bp(ls):
    """
    Finds the average resting blood pressure for the patients who
    have heart disease.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Prints the average resting blood pressure.

    """
    bp = [item[3] for item in ls if item[6] == 1]
    average = sum(bp) / len(bp)
    print("Average resting blood pressure of patients with heart disease:", 
          round(average))

def plot_data(ls):
    """
    Creates a scatterplot using the data for maximun heart rates 
    and cholesterol.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    Scatterplot.

    """
    maxhr = [float(item[5]) for item in ls]
    cholesterol = [float(item[4]) for item in ls]
    colors = []
    for item in ls:
        if item[6] == 1:
            colors.append("r")
        elif item[6] == 0:
            colors.append("b")
    plt.title("Patient Max. Heart Rate to Cholesterol Level")
    plt.xlabel("Maximum Heart Rate")
    plt.ylabel("Cholesterol")
    plt.scatter(maxhr, cholesterol, marker = ".", color = colors)
    plt.show()

def main():
    data = read_data("heart.csv")
    
    total_patients(data)
    heart_disease(data)
    average_age(data)
    heart_average(data)
    average_bp(data)
    heart_bp(data)
    
    plot_data(data)
main()