# Papers Selected:

[Henzinger, M. (2006). Finding near-duplicate web pages: A large-scale evaluation of algorithms. In SIGIR ’06: Proceedings of the 29th annual international ACM SIGIR conference on research and development in information retrieval (pp. 284–291). ACM.](https://pdfs.semanticscholar.org/eaa8/389cc836a41d196dc723f9bd836e5897e452.pdf)

[Hsin-Tsang Lee, Derek Leonard, Xiaoming Wang, and Dmitri Loguinov. 2009. IRLbot: Scaling to 6 billion pages and beyond. ACM Trans. Web 3, 3, Article 8 (July 2009), 34 pages.](http://dx.doi.org.proxy.lib.odu.edu/10.1145/1541822.1541823)

## Notes

### Notes from textbook

Quote from readings in chapter 3, page 87:

> Figure 3.15 shows an example of this process for an 8-bit fingerprint. Note
that common words (stopwords) are removed as part of the text processing. In practice, much larger values of b are used. Henzinger (2006) describes a large-scale Web-based evaluation where the  fingerprints had 384 bits. A web page is defined as a near-duplicate of another page if the simhash  fingerprints agree on more than 372 bits.  This study showed significant effectiveness advantages for the simhash approach compared to fingerprints based on n-grams.

Page 94:

> Henzinger (2006) describes a large-scale evaluation of near-duplicate detection on the Web. The two techniques compared were a version of Broder’s “shingling” algorithm (Broder et al., 1997; Fetterly et al., 2003) and simhash (Charikar, 2002). Henzinger’s study, which used 1.6 billion pages, showed that neither method worked well for detecting redundant documents on the same site because of the frequent use of “boilerplate” text that makes different pages look similar. For pages on different sites, the simhash algorithm achieved a precision of 50% (meaning that of those pages that were declared “near-duplicate” based on the similarity threshold, 50% were correct), whereas the Broder algorithm produced a precision of 38%.


### Notes from Finding near-duplicate web pages

For context, Alg. B is shingling and Alg. C is simhash

- Compare's shingling and simhash algorithms on a very large scale, namely on a set of 1.6B distinct web pages.
Then goes on to propose its own algorithm.
- Purpose to find duplicates
    - They increase the space needed to store the index,
    - either slow down or increase the cost of serving results
    - annoy the users.
- Purpose of Henzinger's paper originally to evaluate the two algorithms, shingling and simhash
- Evaluation criteria:
    - precision on a random subset
    - the distribution of the number of term differences per near-duplicate pair
    - the distribution of the number of near-duplicates per page
- Algorithm flow for Alg. B and Alg. C is as follows:
    - Tokenize HTML page.
    - Generate a bit string and use it to determine near-duplicate web pages
- Shingles are a digital 64-bit fingerprint. Alg. B checks unique shingle comparison then creates a set of them
- There are shingles.
Then there are supershingles.
Then there are megashingles...but they didn't even try for this since they don't improve precision/recall.
Basically the subsequent measures of shingles are kind of like a recursive equation of applying fingerprint methods to their parent shingle.
- To determine similarity Alg. B takes the values of the supershingles vector, a vector of the smallest fingerprint values for a page,
and the number of similarities in the supershingle vectors of two pages are their B-similarity. They are near-duplicates if their
B-similarity is at least 2.
- Alg. C, simhash, is based on the similarity their bit string matches. This paper chose 384 bits, 48 bytes, to compare on just so they could match up
- Alg. B ignores frequency of shingles, while Alg. C takes frequency of terms into account.
- Preprocessing step grouped pages with the same token sequence into identity sets and removed for every identity set all but one page.
25% - 30% were removed in that one step.
- Human evaluated random set of B-similar and C-similar pairs. Labeled them correct, incorrect, or undecided.
Terms of evaluation are below:
    - Correct near-duplicates if (1) their text differs only by the following: a session id, a timestamp, an execution time, a message id, a visitor count, a server name, and/or all or part of their URL (which is included in the document text), (2) the difference is invisible to the visitors of the pages, (3) the difference is a combination of the items listed in (1) and (2), or (4) the pages are entry pages to the same site.
    - Incorrect if the main item(s) of the page was (were) different.
    - The remaining near-duplicate pairs were rated undecided.
- Results:
    - Alg. B
        - Alg. B generated 6 supershingles per page, for a total of 10.1B supershingles. They were sorted and for each pair of pages with an identical supershingle we determined its B- similarity. This resulted in 1.8B B-similar pairs, i.e., pairs with B-similarity at least 2
        - We randomly sampled 96556 B-similar pairs. In 91.9% of the cases both pages belonged to the same site.
        - When checking subsampled pairs the overall precision drops to 0.38. However errors mostly were from the same page.
        The reason being, if there is a large amount of boilerplate text, chances are good that the algorithm cannot distinguish the main item from the boilerplate text and classifies the pair as near-duplicate.
        - Precision improves for pairs with larger B-similarity. This is expected as larger B-similarity means more agreement in supershingles.
        - Alg. B for 17 document pairs with term differences greater 200, database data attributed the most to term count differences.
        In something like Alg. C, this is large of enough of a difference that it only recognizes 3 of these 17 as pairs.
    - Alg. C
        - Finding C-similarity is the comparison of of the 48 byte string broken up into 12 pieces. This approach is guaranteed to find all pairs of pages with difference up to 11, i.e., C-similarity 373.
        - Alg. C achieves an overall precision of 0.50 with 27% incorrect pairs and 23% undecided pairs
    - Overall
        - Alg. B found 1,831M ∗0.38 ≈ 696M correct near-duplicates
        - Alg. C found 1,630M ∗ 0.5 = 815M correct near-duplicates
        - Manual evaluation shows Alg. C outperforms Alg. B with a precision of 0.50 versus 0.38 for Alg. B.


### Notes from IRLbot

- Focus more on designing a crawler than detecting near-duplicates

### Presentation notes









Link to Google presentation [here](https://docs.google.com/presentation/d/1eau_8C03Lz_89oHDMq0hZ525wRUfiwwXmBYQxyrGdbw/edit?usp=sharing).
