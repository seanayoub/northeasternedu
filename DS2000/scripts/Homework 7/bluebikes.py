"""
    Sean Ayoub
    DS 2000
    Homework 7
    November 4, 2022
    
    Reads blue bike data trip and station data. Calculates and plots the 
    distance and speed for each trip in a histogram. Prints day report.
"""

import math
import matplotlib.pyplot as plt

EARTH_RADIUS = 3959

def readtolist(filename, type_cast_dict = {}):
    """
    Reads data from a file and stores it in a list of dictionaries

    Parameters
    ----------
    filename : name of file.
    type_cast_dict : optional. default is {} (all values are strings)

    Returns
    -------
    data : A list of dictionaries for lines in file.

    """
    with open(filename) as f:
        data = []
        header = f.readline().strip().split(",")
        for line in f:
            pieces = line.strip().split(",")
            row_dict = {}
            for i in range(len(pieces)):
                if header[i] in type_cast_dict:
                    cast_func = type_cast_dict[header[i]]
                    row_dict[header[i]] = cast_func(pieces[i])
                else:
                    row_dict[header[i]] = pieces[i]     
            data.append(row_dict)
    return data

def readtodict(filename):
    """
    Reads data from a file into a dictionary.

    Parameters
    ----------
    filename : name of file.

    Returns
    -------
    stations : a dictionary. coordinate points are stored in a list. 
        maps station name to coordinates.

    """
    with open(filename) as f:
        f.readline()
        stations = {}
        for line in f:
            row = line.strip().split(",")
            coordinates = [float(row[1]), float(row[2])]
            stations[row[0]] = coordinates
    return stations

def haversine(s, e):
    """
    Calculates the distance in miles between two points on the earth's surface
    described by latitude and longitude.

    Parameters
    ----------
    start : list of two floats, latitude and longitude
    end : list of two floats, latitude and longitude

    Returns
    -------
    A float value. Distance in miles between two points.

    """
    lat1 = s[0]
    long1 = s[1]
    lat2 = e[0]
    long2 = e[1]
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    dlat = lat2 - lat1
    dlong = long2 - long1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2)**2
    haversine = EARTH_RADIUS * 2 * math.asin(math.sqrt(a))
    return haversine

def updatedict(ls, dt):
    """
    Calculates the distances between start/end stations for every trip.
    Adds the distance and the rate in mph to the existing list.

    Parameters
    ----------
    ls : list of dictionaries (trips)
    dt : a dictionary (stations)

    Returns
    -------
    None.

    """
    for item in ls:
        if item['start_station'] not in dt:
            item['distance'] = "None"
            item['mph'] = "None"
            
        elif item['end_station'] not in dt:
            item['distance'] = "None"
            item['mph'] = "None"
            
        else:
            d = haversine(dt[item['start_station']], dt[item['end_station']])
            item['distance'] = d
            rate = (d / item['duration']) * 3600
            item['mph'] = rate

def getcolumn(ls, key):
    """
    Extracts a column from a given list of data.

    Parameters
    ----------
    ls : a list of dictionaries
    key : the key of the values to extract

    Returns
    -------
    column : a list of values with the given key

    """
    column = []
    for item in ls:
        column.append(item[key])
    return column

def plotdistances(ls):
    """
    Creates a histogram depicting the frequency of distances for the data.

    Parameters
    ----------
    ls : the list of trip data.

    Returns
    -------
    None.

    """
    distances = getcolumn(ls, 'distance')
    distances.remove("None")
    
    plt.title("Frequency of Distances")
    plt.xlabel("Distances")
    plt.ylabel("Frequency")
    plt.hist(distances, bins = 100)
    plt.show()

def plotspeed(ls):
    """
    Creates a histogram depicting the frequency of speeds for the data.

    Parameters
    ----------
    ls : the list of trip data.

    Returns
    -------
    None.

    """
    speed = getcolumn(ls, 'mph')
    speed.remove("None")
    
    plt.figure()
    plt.title("Frequency of Speeds")
    plt.xlabel("Speed in Miles per Hour")
    plt.ylabel("Frequency")
    plt.hist(speed, bins = 100)
    plt.show()

def report(ls):
    """
    Prints a report displaying the number of trips ending at Forsyth St at
    Huntington Ave for each day in the week.

    Parameters
    ----------
    ls : the list of trip data.

    Returns
    -------
    None.

    """
    daycount = {}
    for item in ls:
        if item['end_station'] == 'Forsyth St at Huntington Ave':
            if item['start_day_name'] not in daycount:
                daycount[item['start_day_name']] = 1
            else:
                daycount[item['start_day_name']] = daycount[item['start_day_name']] + 1
        
    print("Number of trips ending at Forsyth St at Huntington Ave:")
    for key in daycount:
        print(key, daycount[key])

def findbike(ls):
    """
    Creates a dictionary of a bike id mapped to its number of trips in the
    given time window. Returns the bike id that has the most number of trips.

    Parameters
    ----------
    ls : list of trip data.

    Returns
    -------
    The first value in the list of bike ids

    """
    bikecount = {}
    for dct in ls:
        if dct.get('bike_id') not in bikecount:
            bikecount[dct.get('bike_id')] = 1
        else:
            bikecount[dct.get('bike_id')] += 1
    c = list(bikecount)
    return c[0]

def plotbike(b, ls, dt):
    """
    Creates a line graph depicting the travels of a particular bike.

    Parameters
    ----------
    b : bike id number
    ls : list of trip data
    dt : station data

    Returns
    -------
    None.

    """
    xlist = []
    ylist = []
    for item in ls:
        if item.get('bike_id') == b:
            start = item.get('start_station')
            end = item.get('end_station')
            st = dt.get(start)
            ed = dt.get(end)
            ylist.append(st[0])
            ylist.append(ed[0])
            xlist.append(st[1])
            xlist.append(st[1])
            
    plt.figure()
    plt.title("September Trips for Bike {0}". format(b))
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.xlim(min(xlist) - .01, max(xlist) + .01)
    plt.ylim(min(ylist) - .01, max(ylist) + .01)
    plt.plot(-71.0875, 42.3367, "*", label = "Northeastern", markersize = 17.0)
    plt.plot(-71.078369, 42.349396, "*", 
             label = "Boston Public Library", markersize = 17.0)
    plt.plot(-71.092003, 42.360001, "*", label = "MIT", markersize = 17.0)
    plt.plot(xlist, ylist, ":", color = "grey")
    plt.legend()
    plt.show()

def main():
    types = {"duration": int, "start_day": int, "bike_id": int}
    t = readtolist("trips.csv", types)
    s = readtodict("stations.csv")   
    
    updatedict(t, s)
    plotdistances(t)
    plotspeed(t)
    report(t)
    
    n = findbike(t)
    plotbike(n, t, s)
main()