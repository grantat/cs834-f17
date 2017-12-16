from bs4 import BeautifulSoup
import os
import json


def parse_scholar():
    directory = "./data/html/"
    titles = []
    for filename in os.listdir(directory):
        with open(directory + filename) as f:
            print(filename)
            text = f.read()
            soup = BeautifulSoup(text, 'html.parser')
            # citations
            sections = soup.select("div.gs_ri")
            for s in sections:
                temp = {"title": "", "citations": "", "authors": ""}
                title = s.select_one("h3.gs_rt")
                # titles.append(title.text.strip())
                authors = s.select_one("div.gs_a")
                temp["title"] = title.text.strip()
                temp["authors"] = authors.text.strip()

                cite_count = s.select("div.gs_fl a")[2].text
                if not cite_count.startswith("Cited by"):
                    cite_count = "Cited by 0"
                cite_count = cite_count.split()[2]
                temp["citations"] = cite_count
                titles.append(temp)

    with open("./data/articles.json", 'w') as out:
        json.dump(titles, out, indent=4)

    format_latex(titles)


def format_latex(titles):
    for t in titles:
        print(t["title"].replace("&", "\\&") + " & " +
              t["citations"] + " \\\\ \\hline")


if __name__ == "__main__":
    parse_scholar()
