#!/usr/bin/env python3

from bs4 import BeautifulSoup
import os
import csv


def unpackFiles():
    file_list = []
    for root, dirs, files in os.walk(os.path.dirname("./data/en/articles")):
        for f in files:
            if f.endswith(".html"):
                path = os.path.join(root, f)
                file_list.append(path)

    return file_list


def getCorpus(file_list):
    # track corpus and vocab growths
    vocab_corpus_counts = []
    # all tokens found
    corpus_count = 0
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

        corpus_count += len(tokens)

        vocab_corpus_counts.append([(i + 1), corpus_count, len(vocab)])

    return vocab_corpus_counts


def write_csv(filename, corpus_growth):
    with open("./data/" + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["doc_number", "corpus_size", "vocab_count"])
        writer.writerows(corpus_growth)


if __name__ == "__main__":
    # get all html files
    file_list = unpackFiles()
    # get list of all tokens
    corpus_growth = getCorpus(file_list)
    write_csv("corpusGrowth.csv", corpus_growth)

    # now traverse documents in reverse order
    file_list.reverse()
    corpus_growth = getCorpus(file_list)
    write_csv("corpusGrowthReverse.csv", corpus_growth)
