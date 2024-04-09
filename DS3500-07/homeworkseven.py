from plotly.subplots import make_subplots
import plotly.graph_objects as go
from collections import Counter
from textblob import TextBlob
import textstat
import re

def clean(line):
    """ remove whitespace, captial letters, and punctuation"""
    line = line.strip()
    line = line.lower()
    line = re.sub(r"[^\w\s]", "", line)
    return line

def stop_words(file, script):
    """ remove predetermined words from file """
    with open(file, "r") as f:
        stop = f.readlines()
    for word in stop:
        word = word.strip()
        word_regex = r"\b" + re.escape(word) + r"\b"
        for i, joke in enumerate(script):
            script[i] = re.sub(word_regex, "", joke)
    script = [joke.strip() for joke in script if joke.strip()]
    return script

def count(text):
    """ calculate total word count of file """
    count = 0
    for line in text:
        count += len(line.split())
    return count

def average(text):
    """ calculate average line length of file """
    total_length = 0
    total_lines = len(text)
    for line in text:
        total_length += len(line.strip())
    if total_lines > 0:
        return total_length / total_lines
    else:
        return 0

def readability(text):
    """ calculate readability score for each line in file """
    scores = []
    for line in text:
        score = textstat.flesch_reading_ease(line)
        scores.append(score)
    return scores

def sentiment(text):
    """ calculate sentiment score for each line in file """
    scores = []
    for line in text:
        blob = TextBlob(line)
        scores.append(blob.sentiment.subjectivity)
    return scores

def frequency(text):
    """Count the frequency of each word in the text"""
    word_counts = {}
    words = re.findall(r"\b\w+\b", text.lower())

    # count frequency
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

class Library:
    """ supports text documents """
    def __init__(self):
        self.data = dict({})
        self.script = dict({})

    def read(self, filename, label = "", parser = None):
        file = []
        data = {"word count": {},
                "average line": {},
                "readability": {},
                "sentiment": {}}

        with open(filename, "r", encoding = "utf-8") as f:
            for line in f:
                line = clean(line)
                file.append(line)

        text = stop_words("nlp_txt/stopwords.txt", file)
        self.script[label] = text

        data["word count"] = count(text)
        data["average line"] = average(text)
        data["readability"] = readability(text)
        data["sentiment"] = sentiment(text)
        self.data[label] = data

    def sankey(self, word_list = None, k = 5):
        """ generate sankey diagram """
        word_frequency = dict({})
        links = []

        for label, script in self.script.items():
            text = ' '.join(script)
            word_counts = frequency(text)
            counter = Counter(word_counts)
            top_words = counter.most_common(k)
            word_frequency[label] = dict(top_words)

            for word, count in top_words:
                links.append({"source": label, "target": word, "value": count})

        nodes = list(set([link["source"] for link in links] + [link["target"] for link in links]))
        node_indices = {node: idx for idx, node in enumerate(nodes)}
        for link in links:
            link["source"] = node_indices[link["source"]]
            link["target"] = node_indices[link["target"]]

        fig = go.Figure(data = [go.Sankey(
            node = dict(
                pad = 15,
                thickness = 20,
                line = dict(color = "black", width = 0.5),
                label = nodes,
                color = "pink"
            ),
            link = dict(
                source = [link["source"] for link in links],
                target = [link["target"] for link in links],
                value = [link["value"] for link in links]
            ))])
        fig.update_layout(title = "text to word sankey diagram")
        fig.show()

    def subplot(self, rows, cols):
        """ generate subplot visualization """
        fig = make_subplots(rows, cols, subplot_titles = list(self.data.keys()))

        row, col = 1, 1
        for label, scores in self.data.items():
            fig.add_trace(go.Scatter(x = scores["readability"], y = scores["sentiment"],
                                     mode = "markers", name = label), row = row, col = col)
            if row == 2:
                fig.update_xaxes(title_text = "readability", row = row, col = col)
            if col == 1:
                fig.update_yaxes(title_text = "sentiment", row = row, col = col)

            col += 1
            if col > cols:
                col = 1
                row += 1

        fig.update_layout(title = "readability vs sentiment score", showlegend = True)
        fig.show()

    def overlay(self):
        """ generate visualization three """
        special = list(self.data.keys())
        score = [sum(scores) / len(scores) for scores in [value.get("sentiment") for value in self.data.values()]]

        fig = go.Figure(data = [go.Bar(x = special, y = score, marker_color = "skyblue")])
        fig.update_layout(title = "sentiment scores for comedy specials",
                          xaxis_title = "comedian", yaxis_title = "sentiment score")
        fig.show()

def main():
    library = Library()

    # read files
    filenames = ["taylortomlinson.txt", "kelseycook.txt", "sethmeyers.txt", "shanegillis.txt", "michellewolf.txt",
                  "marknormand.txt", "natebargatze.txt", "maemartin.txt", "bethstelling.txt", "sammorril.txt"]
    for f in filenames:
        label = f.split(".")[0]
        library.read(f"nlp_txt/{f}", label)

    # visualize
    library.sankey()
    library.subplot(2, 5)
    library.overlay()

if __name__ == "__main__":
    main()