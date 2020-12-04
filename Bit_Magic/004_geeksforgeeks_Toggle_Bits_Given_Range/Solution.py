#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Toggle bits given range
#
# Description:
#
# Given a non-negative number N and two values L and R.
# The problem is to toggle the bits in the range L to R in the binary representation of n,
# i.e, to toggle bits from the rightmost Lth bit to the rightmost Rth bit.
# A toggle operation flips a bit 0 to 1 and a bit 1 to 0.
# Print n after the bits are toggled.
#
#
# Example 1:
#
# Input:
# n = 17 , L = 2 , R = 3
# Output:
# 23
# Explanation:
# (17)10 = (10001)2.  After toggling all
# the bits from 2nd to 3rd position we get
# (10111)2 = (23)10
# Example 2:
#
# Input:
# n = 50 , L = 2 , R = 5
# Output:
# 44
# Explanation:
# (50)10 = (110010)2.  After toggling all
# the bits from 2nd to 3rd position we get
# (101100)2 = (44)10
#
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function toggleBits()
# which takes 3 Integers n, L and R as input and returns the answer.
#
#
# Expected Time Complexity: O(1)
# Expected Auxiliary Space: O(1)
#
#
# Constraints:
#   * 1 <= n <= 105
#   * 1 <= L<=R <= Number of Bits in n
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/toggle-bits-given-range0952/1 (GeeksForGeeks - Toggle bits given range)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
# **************************************************************************
#
import unittest


class Solution(object):
    def toggleBitsFromLtoR(self, n: int, L: int, R: int) -> bool:
        # calculating a number
        # 'num' having 'r'
        # number of bits and
        # bits in the range l
        # to r are the only set bits
        num = ((1 << R) - 1) ^ ((1 << (L - 1)) - 1)

        # toggle bits in the
        # range l to r in 'n'
        # Besides this, we can calculate num as: num=(1<<r)-l .

        # and return the number
        return n ^ num


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_toggleBitsFromLtoR(self) -> None:
        sol = Solution()
        for n, L, R, solution in ([17, 2, 3, 23], [50, 2, 5, 44]):
            self.assertEqual(solution, sol.toggleBitsFromLtoR(n, L, R))


# main
if __name__ == "__main__":
    unittest.main()
