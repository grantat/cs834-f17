# Papers Selected:

[Patricia Correia Saraiva, Edleno Silva de Moura, Nivio Ziviani, Wagner Meira, Rodrigo Fonseca, and Berthier Ribeiro-Neto. 2001. Rank-preserving two-level caching for scalable search engines. In Proceedings of the 24th annual international ACM SIGIR conference on Research and development in information retrieval (SIGIR '01). ACM, New York, NY, USA, 51-58.](https://doi-org.proxy.lib.odu.edu/10.1145/383952.383959)

[Jiangong Zhang, Xiaohui Long, and Torsten Suel. 2008. Performance of compressed inverted list caching in search engines. In Proceedings of the 17th international conference on World Wide Web(WWW '08). ACM, New York, NY, USA, 387-396.](https://doi-org.proxy.lib.odu.edu/10.1145/1367497.1367550)

## Notes

### Notes from textbook

"If the Knuth book is too daunting, any standard algorithms
textbook should be able to give you more detail about how merging works."

### Notes from Rank-preserving two-level caching for scalable search engines

Context is from **2001**.

The problem: Search engines receive millions of queries daily, or 3.5 billion if you're google in 2017, a load never experienced by an IR system in 2001.

> Our work is distinct from previous ones because it presents
experimental results on the effectiveness of different caching
strategies implemented on a real case search engine.

A set of log queries are used to measure and
compare the performance and the scalability of:
- the search engine with no cache
- with the cache for query results
- with the cache for inverted lists
- with the two-level cache

Experimental results show that the two-level cache is superior, and that it allows increasing the maximum number
of queries processed per second by a factor of three, while preserving the response time.

Caching is one of the techniques for improving performance andB scalability in IR.
Caching depends on:
- the presence of reference locality in the access stream
- the frequency at which the database being cached is updated

A hit in the cache of query results avoids
query processing, while a hit in the cache of inverted lists reduces
the amount of I/O associated with answering a query, but does not avoid the query processing costs

On the other hand, the hit ratio associated with inverted lists is usually
higher than the hit ratio for whole queries, which may pay
off the query processing cost.

Two-level cache is a combination of an implementation of a cache of query results,
allowing the search engine
to answer recently repeated queries at a very low cost, since
it is not necessary to process those queries, and
it is also combined with a inverted list of query terms, thus improving
query processing time for the new queries that include at least one term.

This paper uses another paper's early recognition algorithm for document ranking in search engine.

### Notes from Performance of compressed inverted list caching in search engines



### Presentation notes

Link to Google presentation [here](https://docs.google.com/presentation/d/1DVG0fxRekgfrtf18ZsAU1rYtGo5Y5jEqXB-z3J17yA4/edit?usp=sharing).

### Feedback after presenting
