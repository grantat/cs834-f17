#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import csv
import sys


def buildIndex(file_list):
    index = {}
    vocab = set()
    
    for i, f in enumerate(file_list):
        tokens = []
        html = open(f, 'r')
        soup = BeautifulSoup(html.read(), 'html.parser')
        text = soup.get_text()

        for word in text.split():
            if word.isalpha():
                tokens.append(word)
                if word not in vocab:
                    vocab.add(word)


    return vocab_corpus_counts


def write_csv(filename, corpus_growth):
    with open("./data/" + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["doc_number", "word", "documents"])
        writer.writerows(corpus_growth)


if __name__ == "__main__":
    filenames = []
    for arg in range(1, len(sys.argv)):
        filenames.append(sys.argv[arg])

    # get all html files
    invertedIndex = buildIndex(filenames)

    write_csv("invertedIndex.csv", invertedIndex)
