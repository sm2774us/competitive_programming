# Time  :
# Space :
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 692: Top K Frequent Words
#
# Description:
#
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/top-k-frequent-words/ (LeetCode - Problem 692 - Top K Frequent Words)
#
#

from typing import List
import collections
import heapq

import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
        self.freq = 0

    def __lt__(self, other):
        return (
            self.freq > other.freq
            if self.freq != other.freq
            else self.word < other.word
        )


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.is_word = True
        root.word = word
        root.freq += 1

    def topK(self, k):
        q, pq = collections.deque([self.root]), []
        while q:
            node = q.popleft()
            if node.is_word:
                heapq.heappush(pq, node)
            for _, nxt in node.children.items():
                q.append(nxt)
        return heapq.nsmallest(k, pq)


class Solution:

    # Solution 1: Using Sorting
    #
    # Complexity: Time O(NlogN), N is the length of words. Space O(N)
    def topKFrequent_solution_1_using_sorting(
        self, words: List[str], k: int
    ) -> List[str]:
        counts = collections.Counter(words)
        res = []
        for w in sorted(counts, key=lambda w: (-counts[w], w)):
            res.append(w)
            if len(res) == k:
                break
        return res

    # Solution 2: Heap
    #
    # Complexity: Time O(N + klogN), N is the length of words, heapq.heapify is O(N),
    # and for each k, heapq.heappop is O(logN).
    # Space O(N)
    def topKFrequent_soluton_2_using_heap(self, words: List[str], k: int) -> List[str]:
        pq = [(-t, w) for w, t in collections.Counter(words).items()]
        heapq.heapify(pq)
        return [heapq.heappop(pq)[1] for _ in range(k)]

    # Soluton 3: Trie + BFS
    #
    # Complexity: Time O(N + klogN), N is the length of words, k is k. Space O(N)
    #
    def topKFrequent_solution_3_Trie_and_BFS(
        self, words: List[str], k: int
    ) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return [node.word for node in trie.topK(k)]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_topKFrequent(self) -> None:
        sol = Solution()
        for words, k, solution in (
            [["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]],
            [
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4,
                ["the", "is", "sunny", "day"],
            ],
        ):
            self.assertEqual(
                solution, sol.topKFrequent_solution_1_using_sorting(words, k)
            )
            self.assertEqual(solution, sol.topKFrequent_soluton_2_using_heap(words, k))
            self.assertEqual(
                solution, sol.topKFrequent_solution_3_Trie_and_BFS(words, k)
            )


if __name__ == "__main__":
    unittest.main()
