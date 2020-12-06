#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Party Of Couples
#
# Description:
#
# In a party of N people, each person is denoted by an integer. Couples are represented by the same number. Find out the only singe person in the party of couples.
#
#
# Example 1:
#
# Input: N = 5
# arr = {1, 2, 3, 2, 1}
# Output: 3
# Explaination: Only the number 3 is single.
#
# Example 2:
#
# Input: N = 11
# arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
# Output: 4
# Explaination: 4 is the only single.
#
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function findSingle() which takes the size of the array N and the array arr[] as input parameters and returns the only single person.
#
#
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
#
#
# Constraints:
# 1 ≤ N ≤ 10^4
# 1 ≤ arr[i] ≤ 10^6
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/alone-in-couple5507/1 (GeeksForGeeks - Party of Couples)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.geeksforgeeks.org/length-longest-consecutive-1s-binary-representation/
#
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):
    def findSingle_Solution_1(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        for k, v in d.items():
            if v % 2 == 1:
                return k

    def findSingle_Solution_2(self, arr: List[int]) -> int:
        x = 0
        for i in arr:
            x ^= i
        return x


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findSingle(self) -> None:
        sol = Solution()
        for arr, solution in (
            [[1, 2, 3, 2, 1], 3],
            [[1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6], 4],
        ):
            self.assertEqual(solution, sol.findSingle_Solution_1(arr))


# main
if __name__ == "__main__":
    unittest.main()
