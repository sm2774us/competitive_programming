#
# Time : O(N); Space: O(N)
# @tag : Recursion ; Jospehus Problem
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Josephus Problem
#
# Description:
#
# Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a fixed direction.â€‹
# The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the circle, you are the last one remaining and survive.
#
# Example 1:
#
# Input:
# n = 3 k = 2
# Output: 3
# Explanation: There are 3 persons so
# skipping 1 person i.e 1st person 2nd
# person will be killed. Thus the safe
# position is 3.
# Example 2:
#
# Input:
# n = 5 k = 3
# Output: 4
# Explanation: There are 5 persons so
# skipping 2 person i.e 3rd person will
# be killed. Thus the safe position is 4.
# Your Task:
# You don't need to read input or print anything. You are required to complete the function josephus () that takes two parameters n and k and returns an integer denoting safe position.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).
#
# **************************************************************************
# Source: https://leetcode.com/articles/4-keys-keyboard (Leetcode - Problem 651 - 4 Keys Keyboard)
#         https://practice.geeksforgeeks.org/problems/special-keyboard3018/1 (GeeksForGeeks - Special Keyboard)
#
# **************************************************************************
# Resources:
# **************************************************************************
# https://en.wikipedia.org/wiki/Josephus_problem (Wikipedia - Josephus Problem)
#
#
import unittest


class Solution(object):
    def josephus(self, n, k):
        return 1 if n == 1 else (self.josephus(n - 1, k) + k - 1) % n + 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxA(self) -> None:
        sol = Solution()
        for n, k, solution in ([3, 2, 3], [5, 3, 4]):
            self.assertEqual(
                solution,
                sol.josephus(n, k),
                "Should return the safe place in the circle where you survive",
            )


if __name__ == "__main__":
    unittest.main()
