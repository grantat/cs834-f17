#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import nltk
import csv


def unpackFiles():
    file_list = []
    for root, dirs, files in os.walk(os.path.dirname("./data/en/articles")):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                file_list.append(path)

    return file_list


def tokenizeFiles(file_list):
    tokens = []
    for i, f in enumerate(file_list):
        html = open(f, 'r')
        soup = BeautifulSoup(html.read(), 'html.parser')
        text = soup.get_text()

        for word in text.split():
            if word.isalpha():
                tokens.append(word)

    return tokens


def tokenCounts(tokens):
    bigrams = list(nltk.bigrams(tokens))
    token_counts = {}
    bigram_counts = {}

    for t in tokens:
        token_counts.setdefault(t, 0)
        token_counts[t] += 1

    for t in bigrams:
        bigram_counts.setdefault(t, 0)
        bigram_counts[t] += 1

    return token_counts, bigram_counts


def calcProbC(token_list):
    new_list = []
    for i, row in enumerate(token_list):
        # prob = token count / num tokens
        prob = float(row[1]) / len(token_list)
        # c = pos of freq in list * prob
        c = (i + 1) * prob
        new_list.append(row + [prob, c])

    return new_list


def write_csv(filename, token_type, tokens):
    with open("./data/" + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([token_type, "frequency", "prob", "c"])
        writer.writerows(tokens)


def convertDimensions(token_counts):
    '''Make 2D format to write to csv'''
    d = []

    for t in token_counts:
        d.append([t, token_counts[t]])

    d = sorted(d, key=lambda x: x[1], reverse=True)
    return d


if __name__ == "__main__":
    # get all html files
    file_list = unpackFiles()
    # get list of all tokens
    tokens = tokenizeFiles(file_list)
    # count tokens. returns unigram and bigram list
    tc, bc = tokenCounts(tokens)
    # convert to sorted list based on frequeny
    t1 = convertDimensions(tc)
    t2 = convertDimensions(bc)
    # add calculations to each token(s)
    t1 = calcProbC(t1)
    t2 = calcProbC(t2)

    write_csv("rankFreqUnigram.csv", "unigram", t1)
    write_csv("rankFreqBigram.csv", "bigram", t2)
