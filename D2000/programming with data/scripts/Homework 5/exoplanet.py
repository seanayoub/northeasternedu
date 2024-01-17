"""
    Sean Ayoub
    DS 2000
    Homework 5
    October 21, 2022
"""
import matplotlib.pyplot as plt

def convert_orbit(ls):
    """
    Convert the orbital period measured in days to years.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    The list of data with the converted value.
    
    """
    for x in ls:
        days = float(ls[4])
        ls[4] = days / 365
    return ls

def convert_mass(ls):
    """
    Convert the mass from Jupiter masses to Earth masses.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    The list of data with the converted value.

    """
    for x in ls:
        mass = float(ls[2])
        ls[2] = mass * 317.89
    return ls
    
def convert_radius(ls):
    """
    Convert the planet radius from Jupiter radii to Earth radii.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    The list of data with the converted value.

    """
    for x in ls:
        radius = float(ls[3])
        ls[3] = radius * 10.97
    return ls

def read_data(filename):
    planets = []
    with open(filename) as f:
        for line in f:
            if "#" in line:
                continue
            row = line.strip().split(",")
            for i in range(len(row)):
                if row[i] == "":
                    row[i] = 0.0
            name = row[0]
            mass = row[2]
            radius = row[3]
            period = row[4]
            axis = row[5]
            temp = row[11]
            data = [str(name).strip(), float(mass), float(radius), 
                        float(period), float(axis), float(temp)]
            convert_orbit(data)
            convert_mass(data)
            convert_radius(data) 
            planets.append(data)
    return planets
    
def lookup_planet(name, ls):
    """
    Creates a list of attributes for a specific planet.

    Parameters
    ----------
    name : planets[0]. name of planet.
    ls : a list of data.

    Returns
    -------
    Data for a named planet in the form of a list.

    """
    exoplanet = []
    count = 0
    while count < len(ls):
        if name in ls[count]:
            exoplanet = [item for item in ls[count]]
            return exoplanet
        else:
            count +=1
            continue

def euclidean_distance(x, y):
    """
    Determines how different two planets are.

    Parameters
    ----------
    x : list for planet 1
    y : list for planet 2

    Returns
    -------
    Euclidean Difference Score.

    """
    dmass = (x[1] - y[1]) ** 2
    dradius = (x[2] - y[2]) ** 2
    dperiod = (x[3] - y[3]) ** 2
    daxis = (x[4] - y[4]) ** 2
    dtemp = (x[5] - y[5]) ** 2
    
    euclid = float((dmass + dradius + dperiod + daxis + dtemp) ** 0.5)
    return euclid
    
def similar_planet(name, ls):
    """
    Finds the planet with the smallest euclidiean distance to the entered planet.

    Parameters
    ----------
    name : planets[0] or name of planet
    ls : a list of data

    Returns
    -------
    Name of planet which is most similar.

    """
    distances = []
    namedplanet = lookup_planet(name, ls)
    for row in ls:
        if row[0] == name:
            continue
        n = euclidean_distance(namedplanet, row)
        distances.append(n)
    similar = distances.index(min(distances))
    name = ls[similar][0]
    return name

def generate_planet_report(name, ls):
    """
    Prints out attributes of a planet in a readable format

    Parameters
    ----------
    name : name of planet.
    ls : a list of data.

    Returns
    -------
    Prints planet report.

    """
    x = []
    x = lookup_planet(name, ls)
    print("Planet Report for {0}". format(name))
    print()
    print("Mass: {0}". format(x[1]))
    print("Radius: {0}". format(x[2]))
    print("Orbital Period: {0}". format(x[3]))
    print("Semimajor Axis: {0}". format(x[4]))
    print("Surface Temperature: {0}". format(x[5]))
    
def visualize_exoplanets(ls):
    """
    Creates a scatterplot that visualizes the exoplanets.

    Parameters
    ----------
    ls : a list of data.

    Returns
    -------
    A graph.

    """
    earth = lookup_planet("Earth", ls)
    plt.plot(earth[1], earth[4], "o", color = "b", label = "Earth")
    
    mass = [row[1] for row in ls]
    axis = [row[4] for row in ls]
    plt.plot(mass, axis, ".", color = "gray")
    
    plt.title("Exoplanet Visualization")
    plt.xlabel("Mass")
    plt.ylabel("Semimajor Axis")
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()
    
def main():
    planets = []
    planets = read_data("exoplanets.csv")
    x = similar_planet("Earth", planets)
    generate_planet_report(x, planets)
    visualize_exoplanets(planets)
main()