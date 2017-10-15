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


def findLinks(file_list):
    links = {}
    atexts = {}

    for i, f in enumerate(file_list):
        html = open(f, 'r')
        soup = BeautifulSoup(html.read(), 'html.parser')

        for a in soup.find_all("a", href=True):
            link = a["href"]
            atext = a.string

            if atext is None:
                atext = ""

            # assumption every outside URI has http
            if not link.startswith('http'):
                try:
                    link = os.path.join(os.path.dirname(f), link)
                    link = os.path.abspath(link)
                except:
                    pass

            links.setdefault(f, [])
            atexts.setdefault(f, [])

            if f != link and link not in atexts[f] and os.path.isfile(link):
                links[f].append(link)
                atexts[f].append(atext)

    return links, atexts


def findDestinations(links, atexts):
    inlink_count = {}
    inlink_text = {}
    for l in links:
        outlinks = links[l]
        atext = atexts[l]

        for i, outlink in enumerate(outlinks):
            inlink_count.setdefault(outlink, 0)
            inlink_count[outlink] += 1

            inlink_text.setdefault(outlink, [])
            inlink_text[outlink].append(atext[i])

    d = []
    for l in inlink_count:
        # only get file name, remove path
        filename = l.rsplit("/", 1)[1]
        d.append([filename, inlink_count[l], set(inlink_text[l])])

    d = sorted(d, key=lambda x: x[1], reverse=True)

    return d


def write_csv(filename, inlinks):
    with open("./data/" + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["link", "inlinks", "anchor_text"])
        writer.writerows(inlinks)


if __name__ == "__main__":
    # get all html files
    file_list = unpackFiles()
    # get list of all tokens
    links, atexts = findLinks(file_list)
    inlinks = findDestinations(links, atexts)

    try:
        inlinks = inlinks[:10]
    except:
        print("ERROR: Not enough inlinks")
        exit()

    write_csv("inlinks.csv", inlinks)
