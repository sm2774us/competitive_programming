#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Find first repeated character
#
# Description:
#
# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains 3 lines . The first line contains 3 space separated integers N, M, X. Then in the next two lines are space separated values of the array A and B respectively.
#
# Output:
# For each test case in a new line print the sorted space separated values of all the pairs u,v where u belongs to array A and v belongs to array B, such that each pair is separated from the other by a ',' without quotes also add a space after the ',' . If no such pair exist print -1.
#
# Constraints:
# 1 <= T <= 100
# 1 <= N, M, X <= 106
# -106 <= A, B <= 106
#
# Example:
# Input:
# 2
# 5 5 9
# 1 2 4 5 7
# 5 6 3 4 8
# 2 2 3
# 0 2
# 1 3
# Output:
# 1 8, 4 5, 5 4
# 0 3, 2 1
#
# Explanation:
# Testcase 1: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.
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
