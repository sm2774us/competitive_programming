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
        self.child = collections.defaultdict(TrieNode)
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            node = node.child[ch]
        node.word = word


class Solution:

    # Solution 1: Using Heap
    def topKFrequent_solution_1_using_Heap(self, words: List[str], k: int) -> List[str]:
        mapping = collections.Counter(words)
        heap = []
        for word, freq in mapping.items():
            heapq.heappush(heap, (-freq, word))

        res = []
        for i in range(k):
            freq, word = heapq.heappop(heap)
            res.append(word)
        return res

    # Solution 2: Bucket Sort
    def topKFrequent_solution_2_using_BucketSort(
        self, words: List[str], k: int
    ) -> List[str]:
        mapping = collections.Counter(words)
        buckets = [[] for i in range(len(words) + 1)]
        for word, freq in mapping.items():
            buckets[freq].append(word)

        res = []
        for i in range(len(words), 0, -1):
            if buckets[i]:
                for word in sorted(buckets[i]):
                    res.append(word)
                    if len(res) == k:
                        return res
        return res

    # Solution 3: Trie and DFS
    def topKFrequent_solution_3_using_Trie_And_DFS(
        self, words: List[str], k: int
    ) -> List[str]:
        mapping = collections.Counter(words)
        buckets = [Trie() for i in range(len(words) + 1)]
        for word, freq in mapping.items():
            buckets[freq].add(word)

        res = []
        for i in range(len(words), 0, -1):
            if buckets[i]:
                self.dfs(buckets[i].root, res, k)
        return res

    def dfs(self, node, res, k):
        if not node:
            return

        if node.word:
            res.append(node.word)

        if len(res) == k:
            return

        for i in range(26):
            ch = chr(ord("a") + i)
            if ch in node.child:
                self.dfs(node.child[ch], res, k)


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
            self.assertEqual(solution, sol.topKFrequent_solution_1_using_Heap(words, k))
            self.assertEqual(
                solution, sol.topKFrequent_solution_2_using_BucketSort(words, k)
            )
            self.assertEqual(
                solution, sol.topKFrequent_solution_3_using_Trie_And_DFS(words, k)
            )


if __name__ == "__main__":
    unittest.main()
