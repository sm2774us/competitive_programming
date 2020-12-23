#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Repeated Character
#
# Description:
#
# Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.
#
# Example 1:
#
# Input:
# S = "geeksforgeeks"
# Output: g
# Explanation: g, e, k and s are the repeating
# characters. Out of these, g occurs first.
# â€‹Example 2:
#
# Input:
# S = "abcde"
# Output: -1
# Explanation: No repeating character present.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function firstRep() which takes the string S as input and returns the the first repeating character in the string. In case there's no repeating character present, return '#'.
#
#
# Expected Time Complexity: O(|S|).
# Expected Auxiliary Space: O(1).
#
#
# Constraints:
# 1<=|S|<=105
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/repeated-character2058/1 (GeeksForGeeks - Repeated Character)
#
#
import unittest


class Solution:
    # Suggest this approach first in an interview situation, if no additional data structures allowed
    def first_repeated_char(self, str1: str) -> str:
        for index, c in enumerate(str1):
            if str1[: index + 1].count(c) > 1:
                return c
        return ""

    # Use this in an interview situation, if the use of additional data structures is allowed for the problem
    def first_repeated_char_using_set(self, str1: str) -> str:
        seen = set()
        for letter in str1:
            if letter in seen:
                return letter
            else:
                seen.add(letter)
        return ""


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_first_repeated_char(self) -> None:
        sol = Solution()
        for str1, solution in (
            ["geeksforgeeks", "e"],
            ["hellogeeks", "l"],
            ["abcde", ""],
        ):
            self.assertEqual(solution, sol.first_repeated_char(str1))
            self.assertEqual(solution, sol.first_repeated_char_using_set(str1))


if __name__ == "__main__":
    unittest.main()
