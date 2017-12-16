# Assignment #4

### Written report due 2017-12-15:

Chose 5 of:

10.2, 10.3, 10.5, 10.6, 10.8, 10.9, 10.11, 10.12, 11.5, 11.9, 11.11

Extra Credit: SVMlight, 10 points extra credit:
see: http://www.cs.cornell.edu/People/tj/svm_light/
- 1 point:
    - work through the "Inductive SVM" example, discuss in detail the steps and resulting output
- 9 points:
    - create your own example modeled after the "Inductive SVM" example
    - pick a topic (e.g., "Australia") and provide 100 positive and 100 negative examples for training data:
      -- using the Reuters-21578 collection (linked from the SVMlight page)
      -- or, create your own collection with crawled web pages
    - pick 30 documents not in the training set for your test data
    - stem the words in the collection, using TFIDF as the features (compute for the 230 documents)
    - train, classify, and discuss the results

Extra Credit: Wiki Small collection, 8 points extra credit:
* download the wikipedia.org page URIs from the live web.  
* summarize the HTTP status codes returned -- all 200?  Redirections? 404s?  do we still have 6043 documents?  or have their been splits &  merges (see also: wikipedia disambiguation pages)?  (1 pt)
* compare and contrast the in- and out-links from this collection. the number, the domains linked to, the HTTP status of the non-wikipedia links in the article (i.e., are they 200, 404, or something else?). (1 pt)
* compare the least and most popular articles (in terms of in-links) in the 2008 snapshot vs. the least and most popular articles in your 2017 snapshot. (1 pt)
* compare and contrast the anchor text for the articles in the collection: are we gaining or losing terms? (1 pt)
* compare and contrast the sizes of the same pages (i.e., 2008 vs. 2017) in: (2 pts)
    - bytes
    - total terms
    - total unique terms
* for all of the pages (i.e., treat each collection as a single unit), compare the 2008 vs. 2017 snapshots in: (2 pts)
    - bytes
    - total terms
    - total unique terms

### Chosen questions:

> 10.5. Find a community-based question answering site on the Web and ask two
questions, one that is low-quality and one that is high-quality. Describe the answer
quality of each question.

> 10.6. Find two examples of document filtering systems on the Web. How do they
build a profile for your information need? Is the system static or adaptive?

> 10.11. Suggest how the maximum and minimum resource ranking scores, Rmax
and Rmin, could be estimated for a given query

> 11.5. How many papers dealing with term dependency can you find in the SIGIR
proceedings since 2000? List their citations.

> 11.11. Look at a sample of images or videos that have been tagged by users and
separate the tags into three groups: those you think could eventually be done automatically
by image processing and object recognition, those you think would
not be possible to derive by image processing, and spam. Also decide which of the
tags should be most useful for queries related to those images. Summarize your
findings.

### Presentation due 2017-12-14:

Any research paper in "references and further reading" from chapters
9, 10, 11 not already covered by someone else in the class (check
the email list)
