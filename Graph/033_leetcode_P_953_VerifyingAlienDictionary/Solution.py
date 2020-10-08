#
# Time  : O(NS)
# Space : O(1)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 953: Verifying an Alien Dictionary
#
# Description:
#
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
#
# **************************************************************************
# Source: https://leetcode.com/problems/verifying-an-alien-dictionary/ (LeetCode - Problem 953 - Verifying an Alien Dictionary)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# Explanation
# **************************************************************************
# Build a transform mapping from order,
# Find all alien words with letters in normal order.
#
# For example, if we have order = "xyz..."
# We can map the word "xyz" to "abc" or "123"
#
# Then we check if all words are in sorted order.
#
# Complexity
# **************************************************************************
# Time O(NS)
# Space O(1)
#
#
from typing import List

import unittest


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

    # Python : one-liner ( slower solution )
    def isAlienSortedOneLiner(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: list(map(order.index, w)))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isAlienDictionarySorted(self) -> None:
        sol = Solution()
        for words, order, solution in (
            [["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True],
            [["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False],
        ):
            self.assertEqual(
                solution,
                sol.isAlienSorted(words, order),
                "Should determine if the given words are sorted lexicographicaly in this alien language",
            )
            self.assertEqual(
                solution,
                sol.isAlienSortedOneLiner(words, order),
                "Should determine if the given words are sorted lexicographicaly in this alien language",
            )


# main
if __name__ == "__main__":
    unittest.main()
