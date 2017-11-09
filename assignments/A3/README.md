# Assignment #3

### Written report due 2017-11-09:

Chose 5 of:
6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 6.9, 7.2, 7.5, 7.6, 7.7, 7.8, 7.9, 7.13

MLN1: using the small wikipedia example, choose 10 words and create
stem classes as per the algorithm on pp. 191-192.

MLN2: using the small wikipedia example, choose 10 words and compute
MIM, EMIM, chi square, dice association measures for full document
& 5 word windows (cf. pp. 203-205)

Extra credit: chose up to 8 of the above, for a maxium score of 16/10

### Chosen questions:

> 6.1. Using theWikipedia collection provided at the book website, create a sample
of stem clusters by the following process:
1. Index the collection without stemming.
2. Identify the first 1,000 words (in alphabetical order) in the index.
3. Create stem classes by stemming these 1,000 words and recording which
words become the same stem.
4. Compute association measures (Dice’s coefficient) between all pairs of stems
in each stem class. Compute co-occurrence at the document level.
5. Create stem clusters by thresholding the association measure. All terms that
are still connected to each other form the clusters.

> Compare the stem clusters to the stem classes in terms of size and the quality (in your opinion) of the groupings.

> 6.4. Assuming you had a gazetteer of place names available, sketch out an algorithm
for detecting place names or locations in queries. Show examples of the
types of queries where your algorithm would succeed and where it would fail.

> 7.7. What is the “bucket” analogy for a bigram language model? Give examples.

> 7.8. Using the Galago implementation of query likelihood, study the impact of
short queries and long queries on effectiveness. Do the parameter settings make a
difference?

### Galago Notes:

To build galago using version 3.12:

```
$ ~/Downloads/galago-3.12-bin/bin/galago build --indexPath=/Users/gatkins/cs834-f17/assignments/A3/src/data/index --inputPath=/Users/gatkins/cs834-f17/assignments/A3/src/data/en/articles/ --filetype=html
```

To start a server for searching:

```
$ galago-3.12-bin/bin/galago search --port=8080 --index="/Users/gatkins/cs834-f17/assignments/A3/src/data/index"
```

The built index can be found in the `src/data/index` folder.

Dumping the unique keys from the inverted index:

```
$ galago-3.12-bin/bin/galago dump-keys /Users/gatkins/cs834-f17/assignments/A3/src/data/index/postings > /Users/gatkins/cs834-f17/assignments/A3/src/data/dump-keys.csv
```

### Presentation due 2017-11-02:

Any research paper in “references and further reading” from chapters 6 or 7
