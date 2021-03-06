#
# Time : O(N); Space: O(N)
# @tag : Graph
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Find first repeated character
#
# Description:
#
# Given a string S. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains a string S.
#
# Output:
# For each test case in a new line print the first repeating character in the string. If no such character exist print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= |S| <=104
#
# Example:
# Input:
# 2
# geeksforgeeks
# hellogeeks
#
# Output:
# e
# l
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/find-first-repeated-character/0 (GeeksForGeeks - Find first repeated character)
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
        for str1, solution in (["geeksforgeeks", "e"], ["hellogeeks", "l"]):
            self.assertEqual(solution, sol.first_repeated_char(str1))
            self.assertEqual(solution, sol.first_repeated_char_using_set(str1))


if __name__ == "__main__":
    unittest.main()
