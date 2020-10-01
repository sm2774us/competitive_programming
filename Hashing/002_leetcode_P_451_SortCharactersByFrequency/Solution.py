#
# Time : O(N); Space: O(k) where k is the number of unique characters , worst case O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 451: Sort Characters By Frequency
#
# Description:
#
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
# **************************************************************************
# Source: https://leetcode.com/problems/sort-characters-by-frequency/ (Leetcode - Problem 451 - Sort Characters By Frequency)
#         https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0 (GeeksForGeeks - Sorting Elements of an Array by Frequency)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# 1) Frequency of a character can vary from 0 to len(s).
# 2) Create a hashmap H1 of character to character frequency for the input string.
# 3) Iterate H1 to create hashmap H2 with key as frequency and value as substrings of repeated strings with length as the frequency.
# 4) Finally lookup all potential frequencies in decreasing order in H2 and produce the final result.
# **************************************************************************
#
from collections import Counter

import unittest


class Solution:
    # Python O(N) solution using Hash-Map.
    def frequencySort(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = Counter(s), {}
        for k, v in c1.items():
            c2.setdefault(v, []).append(k * v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])

    # Time: O(n), one pass
    # Space: O(k), where k is the number of unique characters... worst case O(n)
    def frequencySortFasterSolutionUsing_Counter_most_common(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        return "".join(c * x for x, c in Counter(s).most_common())


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_frequencySort(self) -> None:
        sol = Solution()
        # NOTE: For - Example 1 (as explained above) both "eert" and "eetr" are valid answers.
        # for s, solution in (["tree", "eert"], ["cccaaa", "cccaaa"], ["Aabb", "bbAa"]):
        for s, solution in (["tree", "eetr"], ["cccaaa", "cccaaa"], ["Aabb", "bbAa"]):
            self.assertEqual(solution, sol.frequencySort(s))
            self.assertEqual(
                solution, sol.frequencySortFasterSolutionUsing_Counter_most_common(s)
            )


if __name__ == "__main__":
    unittest.main()
