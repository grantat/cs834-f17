#!/usr/bin/env python3

import sys
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque
import time


def crawl(uri, q, links_seen):
    """
    Take html string as parameter and parse through links ('a' elements).
    """
    print("Getting links from:", uri)
    try:
        useragent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')

        r = requests.get(uri, headers={'User-Agent': useragent}, verify=False)
        content_type = r.headers.get('content-type').lower()

        if 'text/html' in content_type and r.ok:
            s = BeautifulSoup(r.text, 'html.parser')
            all_a = s.find_all('a', href=True)

            for link in map(lambda a: a['href'], all_a):
                if link not in links_seen:

                    if isAbsolute(link) is False:
                        fulllink = urljoin(r.url, link)
                        if fulllink not in links_seen:
                            q.append(fulllink)
                            links_seen.add(fulllink)
                    else:
                        print("Link found:", link)
                        q.append(link)
                        links_seen.add(link)

    except:
        pass


def isAbsolute(url):
    """
    Taken from stackoverflow post
    """
    try:
        return bool(urlparse(url).netloc)
    except:
        return False


if __name__ == '__main__':
    try:
        baseURL = sys.argv[1]
    except:
        print("Usage: python3 crawler.py {URI-R}")
    q = deque()
    q.append(baseURL)
    hop_count = 1
    links_seen = set()

    uri = q.popleft()
    links_seen.add(uri)

    crawl(uri, q, links_seen)

    qsize = len(q)

    while hop_count > 0:
        time.sleep(5)
        uri = q.popleft()
        qsize -= 1

        crawl(uri, q, links_seen)

        if qsize == 0:
            qsize = len(q)
            hop_count -= 1
            print("Hop completed. With new links queue size is:", qsize)

    while True:
        try:
            uri = q.popleft()
            print("Remaining URI", uri)
        except:
            break
