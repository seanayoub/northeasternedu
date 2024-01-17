"""
    Sean Ayoub
    DS 2000
    Homework 8
    November 18, 2022
    
    Reads Stars Wars script. Calculates sentiment scores for each line, and 
    determines the most positive / negative line. Displays sentiment scores
    for certain characters. Models the data using a histogram, line chart,
    and a scatterplot.
"""

import matplotlib.pyplot as plt

PUNC = ["!", '"', "#", "$", "%", "&", "'", "(", ")",
        "*", "+", ",", "-", ".", "/", ":", ";",
        "<", "=", ">", "?", "@", "[", "]", "^", "_",
        "`", "{", "}", "|", "~"]

def read(file, typd = {}):
    """
    Reads data from a file and stores it in a list of dictionaries
    
    Parameters
    ----------
    filename : name of file.
    typd : type cast dict. optional. 
                    default is {} (all values are strings)
    
    Returns
    -------
    data : A list of dictionaries for lines in file.
    
    """
    with open(file) as f:
        data = []
        h = f.readline().strip().split("|")
        for line in f:
            p = line.strip().split("|")
            row = {}
            for i in range(len(p)):
                if h[i] in typd:
                    c = typd[h[i]]
                    row[h[i]] = c(p[i])
                else:
                    row[h[i]] = p[i]     
            data.append(row)
    return data

def readword(txt):
    """
    Reads words from a file into a set.

    Parameters
    ----------
    txt : a .txt file of words.

    Returns
    -------
    A set of words.

    """
    words = []
    with open(txt) as t:
        for line in t:
            words.append(line.strip())
    return set(words)

def sentiment(ls, lst1, lst2):
    """
    Computes a sentiment score for each line and adds this key/value pair to
    the dictionary.

    Parameters
    ----------
    ls : a list of dictionaries
    lst1 : a set of positive elements
    lst2 : a set of negative elements

    Returns
    -------
    None.

    """
    for item in ls:
        p = 0
        n = 0
        d = item['dialogue'].translate(str.maketrans('', '', ''.join(PUNC))).lower()
        for word in d.split():
            if word in lst1:
                p += 1
            elif word in lst2:
                n += 1
        item['sentiment'] = p - n

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

def plusminus(dt):
    """
    Reports the most positive and the most negative line.

    Parameters
    ----------
    dt : a list of dictionaries.

    Returns
    -------
    None.

    """
    ch = extract(dt, 'character')
    dg = extract(dt, 'dialogue')
    sc = extract(dt, 'sentiment')
    
    h = sc.index(max(sc))
    l = sc.index(min(sc))
    
    print("Most positive line:")
    print("Character: {0}". format(ch[h]))
    print("Dialogue:\n {0}". format(dg[h]))
    print("Score: {0}". format(sc[h]))
    print()
    print("Most negative line:")
    print("Character: {0}". format(ch[l]))
    print("Dialogue:\n {0}". format(dg[l]))
    print("Score: {0}". format(sc[l]))

def avg(L):
    """ Compute the numerical average of a list of numbers.
    If list is empty, return 0.0 """
    if len(L) > 0:
        return sum(L) / len(L)
    else:
        return 0.0

def table(dt):
    """
    Prints a table displaying the minimum, average, and maximum sentiment 
    scores for six specific characters.

    Parameters
    ----------
    dt : a list of dictionaries.

    Returns
    -------
    None.

    """
    chars = ['DARTH VADER', 'LEIA', 'C3PO', 'LUKE', 'OBIWAN', 'HAN SOLO']
    scoremap = {}
    for i in chars:
        scores = []
        for row in dt:
            if i == row['character']:
                scores.append(row['sentiment'])
                scoremap[i] = scores
    for key in scoremap:
        scores = []
        scores.append(min(scoremap[key]))
        scores.append(avg(scoremap[key]))
        scores.append(max(scoremap[key]))
        scoremap[key] = scores 
    print()
    print("Min ", "Average ", "Max ", "Character")
    for key in scoremap:
        m, a, x = scoremap[key]
        print(f"{m}  {round(a, 5)}   {x}    {key}")

def lukeleia(dt):
    """
    Creates a histogram depicting the frequencies of the sentiment scores for
    both Luke and Leia.

    Parameters
    ----------
    dt : a list of dictionaries.

    Returns
    -------
    None.

    """
    luke = []
    leia = []
    for row in dt:
        if row['character'] == 'LUKE':
            luke.append(row['sentiment'])
        elif row['character'] == 'LEIA':
            leia.append(row['sentiment'])
            
    plt.hist(luke, bins = 10, alpha = 0.5, color = "blue", label = "Luke")
    plt.hist(leia, bins = 10, alpha = 0.5, color = "red", label = "Leia")
    plt.xlim(-6, 6)
    plt.title("Frequency of Sentiment Scores")
    plt.legend()
    plt.show()

def get_window(L, idx, window_size=1):
    """ Extract a window of values of specified size centered on the specified 
    index
        L: List of values
        idx: Center index
        window_size: window size
    """
    minrange = max(idx - window_size // 2, 0)
    maxrange = idx + window_size // 2 + (window_size % 2)
    return L[minrange:maxrange]

def moving_average(L, window_size=1):
    """ Compute a moving average over the list L using the specified window size
        L: List of values
        window_size - The window size (default=1)
        return - A new list with smoothed values
    """
    mavg = []
    for i in range(len(L)):
        window = get_window(L, i, window_size)
        mavg.append(avg(window))
    return mavg

def arc(dt):
    """
    Creates a visualization of the movie's story arc 
    using the sentiment scores.

    Parameters
    ----------
    dt : a list of dictionaries.

    Returns
    -------
    None.

    """
    s = extract(dt, 'sentiment')
    x = extract(dt, 'line_number')
    a = moving_average(s, 20)
    
    plt.plot(x, a, color = "gray")
    plt.text(289, -0.75, "Tarkin's Conference", family = "serif")
    plt.text(835, 0.95, "Attack!!", family = "serif")
    plt.title("Sentiment Score Throughout Movie")
    plt.xlabel("Lines of Dialogue")
    plt.ylabel("Story Arc")
    plt.show()

def characterscores(dt):
    """
    Creates a scatterplot depicted the relationship between each character's
    positive and negative lines

    Parameters
    ----------
    dt : A list of dictionaries.

    Returns
    -------
    None.

    """
    c = {}
    characters = extract(dt, 'character')
    for person in characters:
        count = [0, 0]
        for line in dt:
            if person == line['character']:
                if line['sentiment'] > 0:
                    count[1] += 1
                elif line['sentiment'] < 0:
                    count[0] += 1
        if count[0] + count[1] > 10:
            c[person] = count
    
    plt.figure(figsize = (6, 6), dpi = 200)
    plt.plot((0, 70), (0, 70), "--", color = "black")
    for key, value in c.items():
        plt.scatter(value[0], value[1], label = key)

    plt.title("Positive / Negative Characters in Star Wars")
    plt.xlabel("Negative Lines")
    plt.ylabel("Positive Lines")
    plt.xlim(0, 70)
    plt.ylim(0, 70)
    plt.grid()
    plt.legend()
    plt.show()

def main():
    typd = {"line_number": int}
    script = read("starwars.txt", typd)
    p = readword("positive-words.txt")
    n = readword("negative-words.txt")
    
    sentiment(script, p, n)
    plusminus(script)
    table(script)
    
    lukeleia(script)
    arc(script)
    characterscores(script)
main()