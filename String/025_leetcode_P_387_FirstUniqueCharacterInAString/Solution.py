#
# Time : O(N); Space: O(1)
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 387: First Unique Character in a String
#
# Description:
#
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
# Note: You may assume the string contains only lowercase English letters.
#
# **************************************************************************
# Source: https://leetcode.com/problems/first-unique-character-in-a-string/ (Leetcode - Problem 387 - First Unique Character in a String)
#         Variant => https://practice.geeksforgeeks.org/problems/non-repeating-character-1587115620/1 (GeeksForGeeks - Non Repeating Character)
#
# **************************************************************************
# Complexity Analysis:
# **************************************************************************
# Refer to Problem_Description.md.
#
import string

import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = [s.index(l) for l in string.ascii_lowercase if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    def firstUniqCharConcise(self, s: str) -> int:
        return min(
            [s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1]
        )

    def firstUniqCharGFG(self, s: str) -> int:
        index = [s.index(l) for l in string.ascii_lowercase if s.count(l) == 1]
        return s[min(index)] if len(index) > 0 else None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_firstUniqChar(self) -> None:
        s = Solution()
        for str, solution in (["leetcode", 0], ["loveleetcode", 2]):
            self.assertEqual(
                solution,
                s.firstUniqChar(str),
                "Should return the index of the first non-repeating character in a string",
            )

    def test_firstUniqCharConcise(self) -> None:
        s = Solution()
        for str, solution in (["leetcode", 0], ["loveleetcode", 2]):
            self.assertEqual(
                solution,
                s.firstUniqCharConcise(str),
                "Should return the index of the first non-repeating character in a string",
            )

    def test_firstUniqCharGFG(self) -> None:
        s = Solution()
        for str, solution in (
            ["leetcode", "l"],
            ["loveleetcode", "v"],
            ["hello", "h"],
            ["zxvczbtxyzvy", "c"],
        ):
            self.assertEqual(
                solution,
                s.firstUniqCharGFG(str),
                "Should return the first non-repeating character in a string",
            )


if __name__ == "__main__":
    unittest.main()
