Text Comparer
=============

Uses cosine similarity to give a numerical evaluation of the similarity of two
texts (0 to 1).

This code has a companion blog-post here:
http://engineering.aweber.com/cosine-similarity/

Sample Usage
------------
```python
In [1]: from vectorizer import compare_texts

In [2]: compare_texts('Two identical sentences', 'Two identical sentences')
Out[2]: 1.0

In [3]: compare_texts('Two similar sentences', 'Two non-identical sentences')
Out[3]: 0.6666666666666666

In [4]: compare_texts('Two radically different sentences',
                      'This statement shares no words with the previous one')
Out[4]: 0.0
```

The higher the output of `compare_texts`, the higher the percentage of shared
words between sentences.  That description is a simplification of the actual
algorithm, but it's pretty close to truth.
