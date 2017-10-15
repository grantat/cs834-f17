#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import csv
import sys


def buildIndex(file_list):
    index = {}
    full_vocab = set()
    for i, f in enumerate(file_list):
        html = open(f, 'r')
        soup = BeautifulSoup(html.read(), 'html.parser')
        text = soup.get_text()
        vocab = set()

        for word in text.split():
            if word.isalpha():
                word = word.lower()
                if word not in vocab:
                    vocab.add(word)

        full_vocab = full_vocab.union(vocab)
        fname = f
        # if no path separator leave as is
        try:
            fname = f.rsplit("/", 1)[1]
        except:
            fname = f
        # assign words set of words to filename
        index[fname] = vocab

    return index, full_vocab


def invertIndex(index, full_vocab):
    newIndex = {}
    for w in full_vocab:
        files = []
        for f, words in index.items():
            if w in words:
                files.append(f)

        # pick out unique files
        newIndex[w] = sorted(set(files))

    d = []
    for w in newIndex:
        d.append([w, u', '.join(newIndex[w])])

    return d


def write_csv(filename, index):
    with open("./data/" + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["word", "documents"])
        writer.writerows(index)


if __name__ == "__main__":
    # testing with wiki data
    # python3 invertedIndex.py ./data/en/articles/2/0/0/2006_Purdue_Boilermakers_football_team_41f1.html ./data/en/articles/2/0/0/2007-08_Georgetown_Hoyas_men\'s_basketball_team_a8f4.html
    filenames = []
    for arg in range(1, len(sys.argv)):
        filenames.append(sys.argv[arg])

    # get all html files
    index, full_vocab = buildIndex(filenames)
    invertedIndex = invertIndex(index, full_vocab)

    write_csv("invertedIndex.csv", invertedIndex)
