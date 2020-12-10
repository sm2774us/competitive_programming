#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 389: Find the Difference
#
# Description:
#
# You are given two strings s and t.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Return the letter that was added to t.
#
#
#
# Example 1:
#
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:
#
# Input: s = "", t = "y"
# Output: "y"
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: "a"
# Example 4:
#
# Input: s = "ae", t = "aea"
# Output: "a"
#
#
# Constraints:
#
#   * 0 <= s.length <= 1000
#   * t.length == s.length + 1
#   * s and t consist of lower-case English letters.
#
# **************************************************************************
# Source:   https://leetcode.com/problems/find-the-difference/ (LeetCode - Problem 389 - Find the Difference)
# **************************************************************************
#
from collections import Counter
from functools import reduce
from operator import xor
import unittest


class Solution(object):

    # Solution 1 :  Use XOR to find a single character
    #
    def findTheDifference_using_XOR(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

    # Solution 2 :  One-Liner - Using XOR to find a single character
    #
    def findTheDifference_oneliner_using_XOR(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # return chr(reduce(xor, map(ord, s + t)))
        return chr(reduce(xor, map(ord, t + s)))

    # Solution 3 :  One-Liner - Using collections.Counter()
    #
    def findTheDifference_oneliner_using_collections_counter(
        self, s: str, t: str
    ) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list((Counter(t) - Counter(s)))[0]

    # Few one-liners using sorted()
    # Solution 4b
    #
    def findTheDifference_oneliner_using_sorted_0(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return next((c for c, d in zip(sorted(t), sorted(s)) if c != d), max(t))

    # Solution 4b
    #
    def findTheDifference_oneliner_using_sorted_1(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return next(c for c, d in zip(sorted(t), sorted(s) + [None]) if c != d)

    # Solution 4c
    # Only works in Python 2.x
    def findTheDifference_oneliner_using_sorted_2(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return next(c for c, d in map(None, sorted(t), sorted(s)) if c != d)

    # Solution 4d
    # Only works in Python 2.x
    def findTheDifference_oneliner_using_sorted_3(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return filter(None, map(lambda c, d: c != d and c, sorted(t), sorted(s)))[0]

    # Solution 5 :  Two-Liner - Using sorted()
    #
    def findTheDifference_twoliner_using_sorted(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = sorted(s), sorted(t)
        return t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTheDifference(self) -> None:
        sol = Solution()
        for s, t, solution in (
            ["abcd", "abcde", "e"],
            ["", "y", "y"],
            ["a", "aa", "a"],
            ["ae", "aea", "a"],
        ):
            self.assertEqual(solution, sol.findTheDifference_using_XOR(s, t))
            self.assertEqual(solution, sol.findTheDifference_oneliner_using_XOR(s, t))
            self.assertEqual(
                solution, sol.findTheDifference_oneliner_using_collections_counter(s, t)
            )
            self.assertEqual(
                solution, sol.findTheDifference_oneliner_using_sorted_0(s, t)
            )
            self.assertEqual(
                solution, sol.findTheDifference_oneliner_using_sorted_1(s, t)
            )
            # self.assertEqual(solution, sol.findTheDifference_oneliner_using_sorted_2(s, t))
            # self.assertEqual(solution, sol.findTheDifference_oneliner_using_sorted_3(s, t))
            self.assertEqual(
                solution, sol.findTheDifference_twoliner_using_sorted(s, t)
            )


# main
if __name__ == "__main__":
    unittest.main()
