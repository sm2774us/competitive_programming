# Time : O(N); Space: O(N)
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 13: Roman to Integer
#
# Description:
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/roman-to-integer/ (Leetcode - Problem 13 - Roman To Integer)
#             https://practice.geeksforgeeks.org/problems/roman-number-to-integer/0 (GeeksForGeeks - Roman Number To Integer)
#
from functools import reduce

import unittest


class Solution:
    # A different approach in Python - EAFP :
    #   Easier to ask for forgiveness than permission (https://docs.python.org/3.5/glossary.html#term-eafp)
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        dict_ = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result, i = 0, 0
        while i < len(s):
            try:
                result += dict_[s[i] + s[i + 1]]
                i += 2
            except (KeyError, IndexError):
                result += dict_[s[i]]
                i += 1
        return result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_romanToInt(self) -> None:
        sol = Solution()
        for s, solution in (
            ["III", 3],
            ["IV", 4],
            ["IX", 9],
            ["LVIII", 58],
            ["MCMXCIV", 1994],
        ):
            self.assertEqual(
                solution,
                sol.romanToInt(s),
                "Should convert a roman numeral into an integer value",
            )


if __name__ == "__main__":
    unittest.main()
