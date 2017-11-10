import json
import csv


def dice_coefficient(a, b):
    """
    Taken directly from
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Dice%27s_coefficient#Python
    """
    if not len(a) or not len(b):
        return 0.0
    """ quick case for true duplicates """
    if a == b:
        return 1.0
    """
    if a != b, and a or b are single chars, then
    they can't possibly match
    """
    if len(a) == 1 or len(b) == 1:
        return 0.0

    """ use python list comprehension, preferred over list.append() """
    a_bigram_list = [a[i:i + 2] for i in range(len(a) - 1)]
    b_bigram_list = [b[i:i + 2] for i in range(len(b) - 1)]

    a_bigram_list.sort()
    b_bigram_list.sort()

    # assignments to save function calls
    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1

    score = float(matches) / float(lena + lenb)
    return score


def dicePairs():
    with open('data/stem-words-doc-ids.json') as f, \
            open('data/dice.csv', 'w') as out:
        data = json.load(f)
        writer = csv.writer(out)
        for stem, words in data.items():
            if len(words) > 1:
                # check bigrams of all stem words
                temp = set()
                for word in words:
                    for w2 in words:
                        if word != w2 and (word, w2) not in temp and \
                                (w2, word) not in temp:
                            dc = dice_coefficient(word, w2)
                            temp.add((word, w2))
                            writer.writerow([stem, word, w2, dc])
                # print(temp)


def docs(search_word, stems):
    for stem, words in stems.items():
        for word, vals in words.items():
            if word == search_word:
                return vals["doc_ids"]


def diceCluster(wa, wb, stems):
    # document association
    # print(wa, wb)
    docs_wa = docs(wa, stems)
    wa_len = len(docs_wa)

    docs_wb = docs(wb, stems)
    wb_len = len(docs_wb)

    wab_docs = set(docs_wa).intersection(docs_wb)
    wab_len = len(wab_docs)
    score = (2 * wab_len) / (wa_len + wb_len)
    return score


if __name__ == "__main__":
    dicePairs()
    threshold = 0.1
    with open('data/stem-words-doc-ids.json') as f, \
            open('data/dice.csv') as f2, \
            open('data/dice-clusters.csv', 'w') as out:
        stems = json.load(f)
        reader = csv.reader(f2)
        writer = csv.writer(out)
        for row in reader:
            wa = row[1]
            wb = row[2]
            dc = diceCluster(wa, wb, stems)
            if dc > threshold:
                writer.writerow([row[0], wa, wb, dc])
