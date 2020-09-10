# Time :
#   + building Trie: O(N*len(s)) where N = len(strs) and s is the longest word in strs
#   + finding longest prefix: O(M) where M is the length of LCP (which is in the range of 0 and the length of shortest string)
# Space: O(N)
#
# @tag : String, Trie Data Structure
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 14: Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/longest-common-prefix/ (Leetcode - Problem 14 - Longest Common Prefix)
#             https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array/0 (GeeksForGeeks - Longest Common Prefix in an Array)
#
from typing import List
from itertools import islice

import unittest


class TrieNode:
    def __init__(self, letter=""):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def get_longest_prefix(self) -> str:
        res = []
        cur = self.root
        while cur:
            # return when reaches the end of word or when there are more than 1 branches
            if cur.end or len(cur.children) > 1:
                return "".join(res)
            c = list(cur.children)[0]
            res.append(c)
            cur = cur.children[c]
        return "".join(res)


# class TrieNode(object):
#     """Trie Node with a maximum of 26 links (a-z)"""
#     ALPHABET = 26
#
#     def __init__(self):
#         self._links = {}
#         self.is_end = False
#         self.link_size = 0
#
#     def contains_key(self, char):
#         """Check if charater has a child link in node"""
#         return char in self._links
#
#     def get(self, char):
#         """Get child link for character"""
#         return self._links[char]
#
#     def put(self, char, node):
#         """Set child link for character"""
#         self._links[char] = node
#         self.link_size += 1
#
#
# class Trie(object):
#     """Trie for strings of lower case letter a-z"""
#
#     def __init__(self):
#         self._root = TrieNode()
#
#     def insert(self, word):
#         """Insert word into the Trie"""
#         node = self._root
#         for char in word:
#             if not node.contains_key(char):
#                 node.put(char, TrieNode())
#             node = node.get(char)
#         node.is_end = True
#
#     def _search_prefix(self, word):
#         """Search whole key or prefix in the Trie
#            and return the node where the search ends"""
#         node = self._root
#         for char in word:
#             if not node.contains_key(char):
#                 return None
#             node = node.get(char)
#         return node
#
#     def search(self, word):
#         """Search if a word is in the Trie"""
#         node = self._search_prefix(word)
#         return node is not None and node.is_end
#
#     def startswith(self, prefix):
#         """Search if prefix exist in Trie"""
#         node = self._search_prefix(prefix)
#         return node is not None
#
#     def search_longest_prefix(self, word):
#         """Search longest prefix in Trie"""
#         node = self._root
#         prefix = ""
#         for char in word:
#             if (not node.contains_key(char)
#                     or node.link_size != 1
#                     or node.is_end):
#                 return prefix
#
#             prefix += char
#             node = node.get(char)
#
#         return prefix


class Solution:
    # Solution using Trie Data Structure
    #
    # A trie is a tree-like data structure whose nodes store the letters of an alphabet.
    # By structuring the nodes in a particular way, words and strings can be retrieved from the
    # structure by traversing down a branch path of the tree.
    #
    # Q> Where are tries used? Well, the truth is that they’re rarely used exclusively; usually,
    # they’re used in combination with another structure, or in the context of an algorithm.
    # But perhaps the coolest example of how tries can be leveraged for their form and function is
    # for autocomplete features, like the one used in search engines like Google.
    #
    """
    :type strs: List[str]
    :rtype: str
    """

    def longestCommonPrefixUsingTrieDataStructure(self, strs: List[str]) -> str:
        if not strs:
            return ""
        T = Trie()
        for s in strs:
            T.add_word(s)
        return T.get_longest_prefix()

    # def longestCommonPrefixUsingTrieDataStructure(self, strs: List[str]) -> str:
    #     if not strs:
    #         return ""
    #
    #     if len(strs) == 1:
    #         return strs[0]
    #
    #     trie = Trie()
    #     for s in islice(strs, 1, None):
    #         trie.insert(s)
    #
    #     return trie.search_longest_prefix(strs[0])

    # Solution using Horizontal scanning
    """
    :type strs: List[str]
    :rtype: str
    """

    def longestCommonPrefixUsingHorizontalScanning(self, strs: List[str]) -> str:
        if not strs:
            return ""
        common_prefix = strs[0]
        counter = len(common_prefix)
        for s in strs[1:]:
            i, same_count = 0, 0
            while i < len(common_prefix) and i < len(s):
                if common_prefix[i] == s[i]:
                    same_count += 1
                    i += 1
                else:
                    break
            counter = min(counter, same_count)
        return common_prefix[:counter]

    # Solution using Vertical scanning
    """
    :type strs: List[str]
    :rtype: str
    """

    def longestCommonPrefixUsingVerticalScanning(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or c != strs[j][i]:
                    return strs[0][:i]

        return strs[0]

    # Solution using Python Built-In zip function
    """
    :type strs: List[str]
    :rtype: str
    """

    def longestCommonPrefixUsingPythonBuiltInZipFunction(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestCommonPrefix(self) -> None:
        sol = Solution()
        # TODO =>
        # Fix the TEST CASE FAILURE :
        # ***********************************************
        # s = Solution()
        # strs = ["atcg", "ag", "cg"]
        # self.assertEqual(
        #   "g", sol.longestCommonPrefixUsingTrieDataStructure(strs), "Should find the longest common prefix string amongst an array of strings"
        # )
        #
        # TEST CASE ERROR OUTPUT :
        #
        # AssertionError: 'g' != ''
        # - g
        # +
        #  : Should find the longest common prefix string amongst an array of strings
        #
        for strs, solution in (
            [["flower", "flow", "flight"], "fl"],
            [["dog", "racecar", "car"], ""],
            [["geeksforgeeks", "geeks", "geek", "geezer"], "gee"],
            [["apple", "ape", "april"], "ap"],
        ):
            # for strs, solution in ([["flower","flow","flight"], "fl"], [["dog","racecar","car"], ""], [["atcg", "ag", "cg"], "g"],
            #                         [["geeksforgeeks","geeks","geek","geezer"], "gee"], [["apple","ape","april"], "ap"]):
            self.assertEqual(
                solution,
                sol.longestCommonPrefixUsingTrieDataStructure(strs),
                "Should find the longest common prefix string amongst an array of strings",
            )
            self.assertEqual(
                solution,
                sol.longestCommonPrefixUsingHorizontalScanning(strs),
                "Should find the longest common prefix string amongst an array of strings",
            )
            self.assertEqual(
                solution,
                sol.longestCommonPrefixUsingVerticalScanning(strs),
                "Should find the longest common prefix string amongst an array of strings",
            )
            self.assertEqual(
                solution,
                sol.longestCommonPrefixUsingPythonBuiltInZipFunction(strs),
                "Should find the longest common prefix string amongst an array of strings",
            )


if __name__ == "__main__":
    unittest.main()
