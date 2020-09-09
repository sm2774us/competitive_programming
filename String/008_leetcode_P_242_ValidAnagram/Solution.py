# Time : O(N); Space: O(N)
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 242: Valid Anagram
#
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#
# **************************************************************************
# Source    : https://leetcode.com/problems/valid-anagram/ (Leetcode - Problem 242 - Valid Anagram)
#             https://practice.geeksforgeeks.org/problems/anagram/0 (GeeksForGeeks - Anagram)
#
import collections

import unittest


class Solution:
    # A different approach in Python - EAFP :
    #   Easier to ask for forgiveness than permission (https://docs.python.org/3.5/glossary.html#term-eafp)
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(int)
        str1 = s + t
        for i in range(len(s) + len(t)):
            if i < len(s):
                d[str1[i]] += 1
            else:
                d[str1[i]] -= 1
        return all(x == 0 for x in d.values())

    def isAnagramOneLiner(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isAnagram(self) -> None:
        sol = Solution()
        for s, t, solution in (["anagram", "nagaram", True], ["rat", "car", False]):
            self.assertEqual(
                solution,
                sol.isAnagram(s, t),
                "Should return whether t is an anagram of s",
            )
            self.assertEqual(
                solution,
                sol.isAnagramOneLiner(s, t),
                "Should return whether t is an anagram of s",
            )


if __name__ == "__main__":
    unittest.main()
