"""
    Sean Ayoub
    Professor Lou
    DS 2001
    1 December 2022
    ---
    Cleans, analyzes, and visualizes payroll data from the City of Los Angeles. 
"""

"""
    Problem Statement and Background
    ---
        This project explores payroll data to investigate topics relating to 
        diversity in the workplace: gender and ethnic pay gaps, for example. 
        These problems are of interest to the human resources department, 
        which issues and records the payroll, and employers looking to 
        increase the level of equity and inclusion in their workplace. 
        Researching the data with this focus will reveal how a company is 
        currently faring in treating its employees with respect to fair 
        compensation and show how the company can take steps to encourage 
        fair pay.
"""

"""   
    The Dataset
    ---
        The dataset used for this analysis is "Employees' Payroll in Los
        Angeles" located on Kaggle. This dataset features over 685,000 records
        dated from 2013 to 2022, where each record includes information about 
        an employee such as their department, title, and total pay.
        
        Variables of Interest:
        ---
            Record Number - unique id for each employee
            Pay Year - tax year the employee was paid
            Department
            Job Title
            Regular Pay
            Overtime Pay
            Total Pay
            Gender
            Ethnicity
            
        www.kaggle.com/datasets/dsfelix/employees-payroll-in-los-angeles
"""

import matplotlib.pyplot as plt
from statistics import mean, median
from math import log10

FONT = {"family": "serif",
        "color":  "black",
        "size": 16}

def clean(ls):
    """
    Obtains relevant variables from a list of data.

    Parameters
    ----------
    ls : a list of data, representing each row in the csv file

    Returns
    -------
    new_ls : updated list with variables of interest

    """
    year = ls[1]
    dept = ls[3]
    title = ls[5]
    reg_pay = ls[10]
    ovt_pay = ls[11]
    total_pay = ls[13]
    gender = ls[16]
    ethnicity = ls[17]
    new_ls = [year, dept, title, reg_pay, ovt_pay, 
              total_pay, gender, ethnicity]
    return new_ls

def read(csv, type_dict = {}):
    """
    Reads data from a csv file into a list of dictionaries.

    Parameters
    ----------
    csv : name of a csv file
    typd : a type dictionary. default is {} (all strings)

    Returns
    -------
    data : a list of data where each row is stored as a dictionary
            (list of dictionaries)
            
    """
    with open(csv) as f:
        data = []
        header = f.readline().strip().split(",")
        
        for line in f:
            columns = line.strip().split(",")
            if columns[7] == "NOT_ACTIVE":
                continue
           
            if len(columns) == len(header):
                newheader = clean(header)
                newcolumns = clean(columns)
                if '' in newcolumns:
                    continue
            else:
                continue
            
            row = {}
            for i in range(len(newcolumns)):
                if newheader[i] in type_dict:
                    cast = type_dict[newheader[i]]
                    row[newheader[i]] = cast(newcolumns[i])
                else:
                    row[newheader[i]] = newcolumns[i]     
            data.append(row)
    return data

"""
    Methods
    Part One - Gender
    ---
        Using this data, aiming to visualize a comparison between the male and
        female pay gaps. In 2022, the pay gap is 17%, or 83 cents for every 
        dollar a man makes. Visualizing the cumulative disribution will test 
        the accuracy of this statement in regards to the City of Los Angeles. 
        Furthermore, calculating the value allows for a time series of the 
        fluctuation of the pay gap throughout the range of the data. This 
        reveals past and current performance, and paves the way for further 
        research in how the company can encourage equity and equality.
"""

def extract(ls, key):
    """
    Extracts a column from a given list of data.

    Parameters
    ----------
    ls : a list of dictionaries.
    key : key of values to extract.

    Returns
    -------
    column : a list of values with the given key.

    """
    column = []
    for item in ls:
        column.append(item[key])
    return column

def gender(ls):
    """
    Sorts the list of data into two lists based on gender.

    Parameters
    ----------
    ls : a list of dictionaries

    Returns
    -------
    male : a list of records, male
    female : a list of records, female

    """
    male = []
    female = []
    for row in ls:
        if row["GENDER"] == "MALE":
            male.append(row)
        elif row["GENDER"] == "FEMALE":
            female.append(row)
    return male, female

def medianpay(male, female):
    """
    Calculates and prints the median pay for both men and women.

    Parameters
    ----------
    male : list of male records
    female : list of female records

    Returns
    -------
    separate_pay : list of lists. index zero: male pay, index one: female pay

    """
    male_pay = extract(male, "TOTAL_PAY")
    female_pay = extract(female, "TOTAL_PAY")
    
    print("\nWoman's Median Pay (Cumulative): ${0}". 
          format(round(median(female_pay), 2)))
    print("Man's Median Pay (Cumulative): ${0}". 
          format(round(median(male_pay), 2)))
    
    separate_pay = [male_pay, female_pay]
    return separate_pay

def calculate_paygap(totalpay_male, totalpay_female):
    """
    Calculates the unadjusted (average) paygap.

    Parameters
    ----------
    totalpay_male : list of male records, total pay extracted
    totalpay_female : list of female records, total pay extracted

    Returns
    -------
    figure : average pay gap

    """
    m_avg = mean(totalpay_male)
    f_avg = mean(totalpay_female)
    delta = m_avg - f_avg
    if delta <= 0:
        return "Error"
    gap = log10((delta / m_avg) * 100)
    figure = 10 ** gap
    return figure

def years(ls, value):
    """
    Compiles all records from a given year into a list.

    Parameters
    ----------
    ls : a list of dictionaries
    value : year of interest, between 2013 and 2022

    Returns
    -------
    year : a list of dictionaries

    """
    year = []
    for row in ls:
        if row["PAY_YEAR"] == value:
            year.append(row)
    return year

def paygapreport(ls):
    """
    Creates a report detailing the average male and female pay as well as the
    average pay gap for every year in the time span.

    Parameters
    ----------
    ls : a list of dictionaries

    Returns
    -------
    average_paygap : list containing the average pay gap for each year

    """
    print("Pay Gap Report -")
    average_paygap = []
    for i in range(2013, 2023):
        year = years(ls, i)
        m, f = gender(year)
        male = extract(m, "TOTAL_PAY")
        female = extract(f, "TOTAL_PAY")
        figure = calculate_paygap(male, female)
        average_paygap.append(figure)
        print("Average Pay Gap in {0}: ${1}". format(i, round(figure, 2)))
    return average_paygap

def boxplot(separate_pay):
    """
    Creates a boxplot modeling the distribution of total pay for both men and
    women throughout the time range, 2013 - 2022. Prints the median pay for 
    both groups.

    Parameters
    ----------
    separate_pay : list of lists. index zero: male pay, index one: female pay

    Returns
    -------
    None.

    """
    plt.figure(figsize = (10, 4), dpi = 200)
    plt.boxplot(separate_pay, vert = False, showfliers = False)
    plt.text(0, 0.75, "Male", fontdict = FONT,
             bbox = dict(facecolor = "green", alpha = 0.5))
    plt.text(0, 1.75, "Female", fontdict = FONT,
             bbox = dict(facecolor = "red", alpha = 0.5))
    plt.title("Gendered Distribution of Pay Throughout Time", 
              fontdict = FONT, fontweight = "bold")

def linegraph(average_paygap):
    """
    Creates a line graph to visualize the change in average pay gap for 
    each year.

    Parameters
    ----------
    average_paygap : list of average pay gaps for each year

    Returns
    -------
    None.

    """
    x = [i for i in range(2013, 2023)]
    plt.figure(figsize = (8, 4), dpi = 200)
    plt.plot(x, average_paygap, "-", marker = "8", 
             color = "r", alpha = 0.7)
    plt.grid()
    plt.xticks(x, x)
    plt.text(2012.8, 34.5, f"Minimum: ${round(average_paygap[0], 2)}",
             bbox = dict(facecolor = "red", alpha = 0.3), fontsize = 11)
    plt.text(2019.8, 38.5, f"Maximum: ${round(average_paygap[6], 2)}",
             bbox = dict(facecolor = "red", alpha = 0.3), fontsize = 11)
    plt.xlabel("Tax Year", fontdict = FONT)
    plt.ylabel("Average Gap", fontdict = FONT)
    plt.title("Pay Gap Throughout Time", 
              fontdict = FONT, fontweight = "bold")

"""
    Methods
    Part Two - Ethnicity
    ---
        Visualizes the demographic breakdown of average yearly salary.
        Segmenting the records based on their department allows us to see how
        the company is performing compared to itself. The unadjusted pay gap 
        is calculated within each department and graphed to reveal sections 
        that have great disparity.
        Discovers the ways ethnic groups correspond to their average amount 
        made in overtime. Maps this relationship to the average amount made 
        in regular pay for the entire organization. This will show specificly 
        how various ethnic groups are performing compared to each other.
"""

def sortdepartment(ls):
    """
    Finds all departments represented in the dataset. Sorts records into a 
    dictionary with each department mapped to a list of records. Further sorts 
    into male and female categories and retrieves the list of total pay for 
    people in each department.

    Parameters
    ----------
    ls : a list of dictionaries

    Returns
    -------
    department: list of all department titles
    mdept_records: dictionary of male records. 
                    department title -> list of total pay
    fdept_records: dictionary of female records. 
                    department title -> list of total pay

    """
    department = []
    for row in ls:
        if row["DEPARTMENT_TITLE"] not in department:
            department.append(row["DEPARTMENT_TITLE"])
    
    mdept_records = {}
    fdept_records = {}
    for item in department:
        mrec = []
        frec = []
        for row in ls:
            if item == row["DEPARTMENT_TITLE"]:
                if row["GENDER"] == "MALE":
                    mrec.append(row)
                    mdept_records[item] = mrec
                elif row["GENDER"] == "FEMALE":
                    frec.append(row)
                    fdept_records[item] = frec
    
    for key in fdept_records.copy():
        fdept_records[key] = extract(fdept_records.get(key), "TOTAL_PAY")
        if len(fdept_records[key]) < 300:
            fdept_records.pop(key)
    for key in mdept_records.copy():
        mdept_records[key] = extract(mdept_records.get(key), "TOTAL_PAY")
        if key not in fdept_records.keys():
            mdept_records.pop(key, "None")
    dict(sorted(mdept_records.items()))
    dict(sorted(fdept_records.items()))
    return department, mdept_records, fdept_records

def dept_paygap(department, mdept_records, fdept_records):
    """
    Calculates the pay gap for each department, if possible. Finds and reports 
    the department with the highest and lowest pay gap.

    Parameters
    ----------
    department : list of all department titles
    mdept_records : dictionary of male records. department title -> total pay
    fdept_records: dictionary of female records. department title -> total pay

    Returns
    -------
    dept_paygap: a dictionary mapping each department to its pay gap

    """
    dept_gap = {}
    for title in department:
        if title not in mdept_records.keys():
            continue
        paygap = calculate_paygap(mdept_records[title], fdept_records[title])
        if type(paygap) != float:
            continue
        dept_gap[title] = round(paygap, 2)
    
    value = [i for i in dept_gap.values()]
    max_paygap = max(value)
    min_paygap = min(value)
    max_title = [i for i in dept_gap if dept_gap[i] == max_paygap]
    min_title = [i for i in dept_gap if dept_gap[i] == min_paygap]
    
    print(f"\n{max_title[0].strip()} Department")
    print(f"Maximum Average Pay Gap: ${max_paygap} \n")
    print(f"{min_title[0].strip()} Department")
    print(f"Minimum Average Pay Gap: ${min_paygap} \n")
    return dept_gap

def sortethnicity(ls):
    """
    Finds all ethinc groups represented in the data. Excludes ambiguous
    categories such as "unknown" or "not applicable".

    Parameters
    ----------
    ls : a list of dictionaries

    Returns
    -------
    ethnicity : a list of ethnicities

    """
    skip = ["NOT APPLICABLE", "UNKNOWN", "FILLIPINO", "NA", "NATIVE_AMERICAN",
            "AMERICAN INDIAN/ALASKAN NATIVE", "TWO OR MORE RACES"]
    ethnicity = []
    for row in ls:
        if row["ETHNICITY"] in skip:
            continue
        elif row["ETHNICITY"] not in ethnicity:
            ethnicity.append(row["ETHNICITY"].strip())
    ethnicity.sort(reverse = True)
    return ethnicity

def overtimepay(ls, ethnicity):
    """
    Finds the ethnic groups that made the most and least in overtime pay, 
    throughout the time range.

    Parameters
    ----------
    ls : a list of dictionaries
    ethnicity : a list of ethnicities

    Returns
    -------
    regular: dictionary mapping ethnicity to average regular earnings
    overtime: dictionary mapping ethnicity to average overtime earnings

    """
    overtime = {}
    regular = {}
    for item in ethnicity:
        line = []
        for row in ls:
            if row["ETHNICITY"] == item:
                line.append(row)
                overtime[item] = line
    for item in overtime.items():
        ovt = extract(item[1], "OVERTIME_PAY")
        ovt = [item for item in ovt if item != 0.0]
        avg = mean(ovt)
        overtime[item[0]] = avg
        
        reg = extract(item[1], "REGULAR_PAY")
        reg = [item for item in reg if item != 0.0]
        aveg = mean(reg)
        regular[item[0]] = aveg
    
    max_value = max(overtime.values())
    min_value = min(overtime.values())
    max_group = [i for i in overtime if overtime[i] == max_value]
    min_group = [i for i in overtime if overtime[i] == min_value]
    
    print(f"Ethnic Group that Made the Most in Overtime: {max_group[0]}")
    print(f"Average Amount Made: ${round(max_value, 2)} \n")
    print(f"Ethnic Group that Made the Least in Overtime: {min_group[0]}")
    print(f"Average Amount Made: ${round(min_value, 2)} \n")
    return regular, overtime

def ethnicity_avgpay(ls, ethnicity):
    """
    Calculates the overall average salary for each ethinc group.

    Parameters
    ----------
    ethnicity : a list of ethnicities

    Returns
    -------
    ethnicity : list of ethnicities
    means : list of average pay earned by each ethnic group

    """
    means = []
    for item in ethnicity:
        pay = []
        for row in ls:
            if item == row["ETHNICITY"]:
                pay.append(row["TOTAL_PAY"])
        means.append(round(mean(pay), 2))
    return ethnicity, means

def barplot(ethnicity, means):
    """
    Creates a barplot depicting the average salary throughout the time period 
    for each ethnic group represented in the data.

    Parameters
    ----------
    ethnicity:
    means:

    Returns
    -------
    None.

    """
    dt = {k:v for (k, v) in zip(ethnicity, means)} 
    avg_dt = dict(sorted(dt.items(), key = lambda x: x[1]))
    ethnicity = [item for item in avg_dt.keys()]
    means = [item for item in avg_dt.values()]
    
    plt.figure(figsize = (10, 7), dpi = 200)
    plt.barh(ethnicity, means, height = 0.6, fill = False, hatch = "///")
    plt.xlabel("Average Salary", fontdict = FONT)
    plt.title("Average Total Pay by Ethnicity", 
              fontdict = FONT, fontweight = "bold")

def plotdepartment(dept_gap):
    """
    Creates a bar graph depicting the average pag gap within each department.

    Parameters
    ----------
    dept_gap : a dictionary mapping each department to its pay gap

    Returns
    -------
    None.

    """
    sortdept_gap = dict(sorted(dept_gap.items(), key = lambda x: x[1]))
    
    plt.figure(figsize = (20, 10), dpi = 200)
    plt.bar(sortdept_gap.keys(), sortdept_gap.values(), 
            color = "b", alpha = 0.6)
    plt.xticks(rotation = 90)
    plt.ylabel("Pay Gap", fontdict = FONT)
    plt.title("Average Pay Gap by Department", 
              fontdict = FONT, fontweight = "bold")

def averagetoovertime(regular, overtime):
    """
    Creates a scatterplot that models the relationship between the average 
    regular pay and the average overtime pay for each ethnic group.

    Parameters
    ----------
    regular : dictionary mapping ethnicity to average regular earnings
    overtime: dictionary mapping ethnicity to average overtime earnings

    Returns
    -------
    None.

    """
    labels = sorted(overtime.keys())
    plt.figure(figsize = (9, 9), dpi = 200)
    plt.grid()
    count = 0
    while count < len(overtime.values()):
        plt.scatter(list(regular.values())[count], 
                    list(overtime.values())[count],
                    s = 50, label = labels[count])
        count += 1
    plt.legend()
    plt.xlabel("Regular Pay", fontdict = FONT)
    plt.ylabel("Overtime Pay", fontdict = FONT)
    plt.title("Relationship of Average Regular to Overtime Pay",
              fontdict = FONT, fontweight = "bold")
    
def main():
    # read
    type_dict = {"PAY_YEAR": int, "REGULAR_PAY": float, "OVERTIME_PAY": float, 
                 "TOTAL_PAY": float}
    payroll = read("payroll.csv", type_dict)
    
    # analyze
    average_paygap = paygapreport(payroll)
    male, female = gender(payroll)
    separate_pay = medianpay(male, female)
    
    dept, mdept, fdept = sortdepartment(payroll)
    dept_gap = dept_paygap(dept, mdept, fdept)
    
    ethnicity = sortethnicity(payroll)
    regular, overtime = overtimepay(payroll, ethnicity)
    ethnicity, means = ethnicity_avgpay(payroll, ethnicity)
    
    # visualize
    boxplot(separate_pay)
    
    linegraph(average_paygap)
    
    barplot(ethnicity, means)
    
    plotdepartment(dept_gap)
    
    averagetoovertime(regular, overtime)
main()

"""
Program Output:
    Pay Gap Report -
    Average Pay Gap in 2013: $29.39
    Average Pay Gap in 2014: $29.98
    Average Pay Gap in 2015: $31.9
    Average Pay Gap in 2016: $37.18
    Average Pay Gap in 2017: $36.86
    Average Pay Gap in 2018: $36.67
    Average Pay Gap in 2019: $39.29
    Average Pay Gap in 2020: $34.48
    Average Pay Gap in 2021: $32.57
    Average Pay Gap in 2022: $33.08

    Woman's Median Pay (Cumulative): $60444.88
    Man's Median Pay (Cumulative): $92627.45

    FIRE Department
    Maximum Average Pay Gap: $39.38 

    ANIMAL SERVICES Department
    Minimum Average Pay Gap: $2.36 

    Ethnic Group that Made the Most in Overtime: CAUCASIAN
    Average Amount Made: $25955.05 

    Ethnic Group that Made the Least in Overtime: PACIFIC ISLANDER
    Average Amount Made: $3794.2 
"""

"""
    Results, Conclusions, and Future Work
    ---
        According to these visualizations, the City of Los Angeles has a large
        pay gap that rests well above the national average. It is curious to 
        see the change in pay gap over time as well as the potential influence 
        of the pandemic on diversity in this workspace.
        
        Highlighting the departments that have a larger pay gap reveals where
        the City of Los Angeles can reallocate their resources for progress 
        and social equity in their workplaces. An example would be hiring more 
        women and people of color. 
        
        With more time, it is possible to derive many more actionable insights 
        related to effecting change in Los Angeles' workplaces, as well as 
        continuing broader research and analytics.
"""