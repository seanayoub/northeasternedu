"""
    DS2001 Weekly Exercise 9 & 10
    Sean Ayoub
"""

import matplotlib.pyplot as plt
import csv

# Q1
def read_data(filename):
    """ name: read_data
        input: filename (string)
        returns: header is a list
                 data is list of lists
    """
    
    data = []
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data.append(row)
        header = data.pop(0)
    return header, data

# Q2
def viewership(data):
    """
    Returns a dictionary depicting the number of ratings each top 100 movie has.

    Parameters
    ----------
    data : A data set as a list of lists.

    Returns
    -------
    views : A dictionary of the movie id mapped to the number of reviews it has.

    """
    views = {}
    for item in data:
        if item[1] not in views:
            views[item[1]] = 1
        else:
            views[item[1]] += 1
    return views

# Q3
def plotgenres(moviedata, ratingcount):
    """
    Plots a bar graph of the frequencies of the genres in the data.

    Parameters
    ----------
    moviedata : movie data, a list of lists
    ratingcount : rating counts, a dictionary

    Returns
    -------
    genredict : a dictionary that was used to plot the data.

    """
    genredict = {}
    for row in moviedata:
        if row[0] in ratingcount.keys():
            genres = row[2].split("|")
            for item in genres:
                if item not in genredict.keys():
                    genredict[item] = 1
                else:
                    genredict[item] += 1
    genredict = dict(sorted(genredict.items(), key = lambda item: item[1], 
                            reverse = True))
    
    plt.title("Frequency of Genres")
    plt.xlabel("Genres")
    plt.ylabel("Frequency")
    plt.bar(genredict.keys(), genredict.values())
    plt.xticks(rotation = 90)
    plt.show()
    
    return genredict

# Q4
def plot_rating_dist(rd):
    """
    Creates a graph of the frequencies of ratings for the movies.

    Parameters
    ----------
    rd : rating data.

    Returns
    -------
    None.

    """
    rtd = {}
    for row in rd:
        if row[2] not in rtd.keys():
            rtd[row[2]] = 1
        else:
            rtd[row[2]] += 1
    rtd = dict(sorted(rtd.items(), reverse = True))
    
    plt.bar(rtd.keys(), rtd.values(), color = "gray", width = 0.6)
    plt.title("Frequency of Movie Ratings for Top 100")
    plt.xlabel("Ratings")
    plt.ylabel("Frequency")
    plt.show()
    
# Q5
def highest_rating(moviedata, ratingdata, ratingcount):
    """
    Finds the movie with the highest average rating

    Parameters
    ----------
    moviedata : movie data.
    ratingdata : rating data.
    ratingcount : list of viewership frequencies.

    Returns
    -------
    h : top movie's id.
    topmovie : name of the top movie.
    hscore : average rating for top movie.

    """
    rt = {}
    for row in ratingdata:
        if row[1] in rt.keys():
            rt[row[1]] += float(row[2])
        else:
            rt[row[1]] = float(row[2])
    avg = {x : round(rt[x] / ratingcount[x], 2) for x in ratingcount}
    h = max(avg, key = avg.get)
    hscore = avg[h]
    for row in moviedata:
        if row[0] == h:
            topmovie = row[1]
    return h, topmovie, hscore

def main():
    ratingheader, ratingdata = read_data("rating_short.csv")
    movieheader, moviedata = read_data("movie.csv")
    
    v = viewership(ratingdata)
    plotgenres(moviedata, v)
    plot_rating_dist(ratingdata)
    print(highest_rating(moviedata, ratingdata, v))

if __name__ == "__main__":
    main()