import enchant
import csv


def spellcheck():
    with open('./data/dump-keys.csv', 'r') as f, \
            open('./data/spell-checked-keys.csv', 'w') as out:
        reader = csv.reader(f)
        writer = csv.writer(out)
        d = enchant.Dict("en_US")
        for row in reader:
            word = row[0]
            if d.check(word):
                writer.writerow([word])


if __name__ == "__main__":
    spellcheck()
