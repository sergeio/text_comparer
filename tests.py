from unittest import TestCase, main

from similarity import dot_product, magnitude, similarity
from vectorizer import (
    compare_texts,
    compare_vectors,
    vectorize_text,
    word_frequencies,
)


####
##
## Math
##
####

class TestMathFunctions(TestCase):

    def test_dot_product(self):
        returned = dot_product([1, 2], [3, 4])
        self.assertEqual(returned, 11)

    def test_magnitude(self):
        returned = magnitude([3, 4])
        self.assertEqual(returned, 5)

    def test_similarity(self):
        self.assertAlmostEqual(similarity([1, 1], [-1, -1]), -1)
        self.assertAlmostEqual(similarity([1, 1], [1, 1]), 1)
        self.assertAlmostEqual(similarity([0, 1], [1, 0]), 0)


####
##
## Words
##
####

class TestWordFunctions(TestCase):

    def test_word_frequencies(self):
        returned = word_frequencies(['this', 'is', 'sparta', 'sparta'])
        self.assertEqual(returned, {'this': .25, 'is': .25, 'sparta': .5})

    def test_phrase_similarity_same_word(self):
        returned = compare_vectors(['cats'], ['cats'])
        self.assertEqual(returned, 1)

    def test_phrase_similarity_totally_different_vectors(self):
        returned = compare_vectors(['dogs'], ['cats'])
        self.assertEqual(returned, 0)

    def test_phrase_similarity_similar_vectors(self):
        returned = compare_vectors(['cats', 'great'], ['cats', 'evil'])
        self.assertAlmostEqual(returned, .5)

    def test_text_vectorizer(self):
        returned = vectorize_text('The EVIL man likes cats.')
        self.assertEqual(returned, ['evil', 'man', 'likes', 'cats'])

    def test_text_comparison(self):
        t1 = "Crispy chicken sandwich."
        t2 = "You are a \n chicken!"
        t3 = "You are an apple?"
        self.assertTrue(compare_texts(t1, t2) > compare_texts(t1, t3))


if __name__ == '__main__':
    main()
