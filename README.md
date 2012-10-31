Text Comparer
=============

Uses cosine similarity to give a numerical evaluation of the similarity of two
texts (0 to 1).

Sample Usage
------------
```python
In [1]: from vectorizer import compare_texts

In [2]: compare_texts('Mary had a little shotgun.', 'Mary loves her shotgun')
Out[2]: 0.66666666666666663

In [3]: compare_texts('John loves Mary.', 'But Mary has a shotgun.')
Out[3]: 0.33333333333333331
```

The higher score in `2` implies that the first two sentences are more similar
than the second two.  A classic tale of the love-linked-list.
