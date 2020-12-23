# Time  :
# Space :
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 1023: Camelcase Matching
#
# Description:
#
# A query word matches a given pattern if we can insert lowercase letters to the pattern word
# so that it equals the query. (We may insert each character at any position,
# and may insert 0 characters.)
#
# Given a list of queries, and a pattern, return an answer list of booleans,
# where answer[i] is true if and only if queries[i] matches the pattern.
#
#
# Example 1:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation:
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# Example 2:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation:
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# Example 3:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation:
# "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
#
#
# Note:
#
#   * 1 <= queries.length <= 100
#   * 1 <= queries[i].length <= 100
#   * 1 <= pattern.length <= 100
#   * All strings consists only of lower and upper case English letters.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/camelcase-matching/ (LeetCode - Problem 1023 - Camelcase Matching)
#             https://practice.geeksforgeeks.org/problems/camelcase-pattern-matching/0 (GeeksForGeeks - CamelCase Pattern Matching)
#
#
from typing import List
import collections
import re

import unittest


class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.is_word = True


class Solution:

    # Soultion 1: Using regex
    def camelMatch_solution_1_using_regex(
        self, queries: List[str], pattern: str
    ) -> List[bool]:
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        return [
            re.match("^[a-z]*" + "[a-z]*".join(pattern) + "[a-z]*$", q) != None
            for q in queries
        ]
        # return [re.fullmatch('[a-z]*' + '[a-z]*'.join(pattern) + '[a-z]*', q) for q in queries]
        # new_pattern = re.compile(r'^[a-z]*' + '[a-z]*'.join(list(pattern)) + '[a-z]*$')
        # return [re.match(new_pattern, q) for q in queries]

    # Solution 2: Two Pointers
    def camelMatch_solution_2_using_two_pointers(
        self, queries: List[str], pattern: str
    ) -> List[bool]:
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        def patternMatch(p: str, q: str) -> bool:
            i = 0
            for j, c in enumerate(q):
                if i < len(p) and p[i] == c:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(p)

        return [patternMatch(pattern, q) for q in queries]

    # Solution 3: Check subsequence
    def camelMatch_solution_3_check_subsequence(
        self, queries: List[str], pattern: str
    ) -> List[bool]:
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)

        return [u(pattern) == u(q) and issup(pattern, q) for q in queries]

    # Soluton 4: Check subsequence - easy-to-understand
    def camelMatch_solution_4_check_subsequence_easy_to_understand(
        self, queries: List[str], pattern: str
    ) -> List[bool]:
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []
        for query in queries:
            res.append(self.isSubsequence(pattern, query))
        return res

    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            return False
        i = j = 0
        ##Difference from [#392](https://leetcode.com/problems/is-subsequence) : We need to exhaust t in order to prevent case like: s="FB",t="ForceFeedBack".
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            ##We can only skip lower case letters.
            elif t[j].isupper():
                return False
            j += 1
        return True if i == len(s) else False

    # Soluton 5: Using Trie data structure
    def camelMatch_solution_5_using_trie_data_structure(
        self, queries: List[str], pattern: str
    ) -> List[bool]:
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """

        def find(node, p_i, pattern, cur_word, table):
            if p_i >= len(pattern):
                if node.is_word:
                    key = "".join(cur_word)
                    table[key] = True
                for k in node.child:
                    if k.islower():
                        find(node.child[k], p_i, pattern, cur_word + [k], table)
            else:
                for k in node.child:
                    if k == pattern[p_i]:
                        find(node.child[k], p_i + 1, pattern, cur_word + [k], table)
                    elif k.islower():
                        find(node.child[k], p_i, pattern, cur_word + [k], table)

        trie = Trie()
        for q in queries:
            trie.insert(q)

        table = collections.defaultdict(lambda: False)
        find(trie.root, 0, pattern, [], table)

        return [table[q] for q in queries]

    # Function that prints the camel
    # case pattern matching
    def camelCase_GFG_Solution(self, words: List[str], pattern: str) -> List[bool]:

        # Map to store the hashing
        # of each words with every
        # uppercase letter found
        map = dict.fromkeys(words, None)

        # Traverse the words array
        # that contains all the
        # string
        for i in range(len(words)):

            # Intialise str as
            # empty
            string = ""

            # length of string words[i]
            l = len(words[i])
            for j in range(l):

                # For every uppercase
                # letter found map
                # that uppercase to
                # original words
                if words[i][j] >= "A" and words[i][j] <= "Z":
                    string += words[i][j]

                    if string not in map:
                        map[string] = [words[i]]

                    elif map[string] is None:
                        map[string] = [words[i]]

                    else:
                        map[string].append(words[i])

        wordFound = False
        # Traverse the map for pattern
        # matching
        for key, value in map.items():

            # If pattern matches then
            # print the corresponding
            # mapped words
            if key == pattern:
                wordFound = True
                # for itt in value:
                #    print(itt)

        # If word not found print
        # "No match found"
        # if (not wordFound):
        #    print("No match found")
        return wordFound


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_camelMatch(self):
        sol = Solution()

        for queries, pattern, solution in (
            [
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FB",
                [True, False, True, True, False],
            ],
            [
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FoBa",
                [True, False, True, False, False],
            ],
            [
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FoBaT",
                [False, True, False, False, False],
            ],
            [["FrameBuffer"], "FaBu", [True]],
        ):
            self.assertEqual(
                sol.camelMatch_solution_1_using_regex(queries, pattern), solution
            )
            self.assertEqual(
                sol.camelMatch_solution_2_using_two_pointers(queries, pattern), solution
            )
            self.assertEqual(
                sol.camelMatch_solution_3_check_subsequence(queries, pattern), solution
            )
            self.assertEqual(
                sol.camelMatch_solution_4_check_subsequence_easy_to_understand(
                    queries, pattern
                ),
                solution,
            )
            self.assertEqual(
                sol.camelMatch_solution_5_using_trie_data_structure(queries, pattern),
                solution,
            )

        for queries, pattern, solution in (
            [
                [
                    "Hi",
                    "Hello",
                    "HelloWorld",
                    "HiTech",
                    "HiGeek",
                    "HiTechWorld",
                    "HiTechCity",
                ],
                "HiTechLab",
                False,
            ],
            [["WelcomeGeek", "WelcomeToGeeksForGeeks", "GeeksForGeeks"], "WTG", True],
        ):
            self.assertEqual(sol.camelCase_GFG_Solution(queries, pattern), solution)


if __name__ == "__main__":
    unittest.main()
