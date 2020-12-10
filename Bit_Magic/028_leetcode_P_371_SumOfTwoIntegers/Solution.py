#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 371: Sum of Two Integers
#
# Description:
#
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1
#
# **************************************************************************
# Source:   https://leetcode.com/problems/sum-of-two-integers/ (LeetCode - Problem 371 - Sum of Two Integers)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):
    def getSum(self, a: int, b: int) -> int:
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry

        if (a >> 31) & 1:  # If a is negative in 32 bits sense
            return ~(a ^ mask)
        return a


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getSum(self) -> None:
        sol = Solution()
        for a, b, solution in ([1, 2, 3], [-2, 3, 1], [-8, -12, -20]):
            self.assertEqual(solution, sol.getSum(a, b))


# main
if __name__ == "__main__":
    unittest.main()
