from nltk.stem.porter import PorterStemmer
import json
import csv


def createStems():
    stemmer = PorterStemmer()
    d = {}
    with open('data/top-1k-words.csv') as f, \
            open('data/stems.json', 'w') as out:
        reader = csv.reader(f)
        for row in reader:
            word = row[0]
            stem = stemmer.stem(word)
            d.setdefault(stem, {})
            # print(word, 'vs', stem, word == stem)
            if word != stem:
                d[stem].setdefault(word, {})

        json.dump(d, out, sort_keys=True, indent=4)

    return d


def findDocsWithTerm(term):
    # given a term find all document ids with that term from inverted index
    doc_ids = []
    with open('data/dump.csv') as f:
        print("Checking document ids for:", term)
        reader = csv.reader(f)
        found_flag = False
        for row in reader:
            if row[0] == term:
                print("found term", row[0])
                found_flag = True
                i = 1
                while(True):
                    try:
                        d_id = row[i]
                        doc_ids.append(d_id)
                        i += 1
                    except:
                        break
            elif found_flag:
                break

    return doc_ids


def wordDocs(stems):
    # with open('clusters') as f:
    word_docs = {}
    for k, words in stems.items():
        # only care about bigrams from stems
        if len(words) > 1:
            for word in words:
                word_docs.setdefault(word, [])
                word_docs[word] = findDocsWithTerm(word)

    json.dumps(word_docs, sort_keys=True, indent=4)
    return word_docs


def mergeStemIds(stems, word_docs):
    # add document ids to dictionary with word
    with open('data/stem-words-doc-ids.json', 'w') as out:
        for stem, words in stems.items():
            # Skip non bigrams
            if len(words) < 2:
                continue
            for word in words:
                stems[stem][word] = {"doc_ids": word_docs[word]}
        json.dump(stems, out, sort_keys=True, indent=4)


if __name__ == "__main__":
    stems = createStems()
    word_docs = wordDocs(stems)
    mergeStemIds(stems, word_docs)
