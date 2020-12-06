#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 693: Binary Number with Alternating Bits
#
# Description:
#
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
# Example 2:
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
# Example 3:
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
# Example 4:
#
# Input: n = 10
# Output: true
# Explanation: The binary representation of 10 is: 1010.
# Example 5:
#
# Input: n = 3
# Output: false
#
#
# Constraints:
#   * 1 <= n <= 2^31 - 1
#
# **************************************************************************
# Source:   https://leetcode.com/problems/binary-number-with-alternating-bits/ (LeetCode - Problem 693 - Binary Number with Alternating Bits)
#           https://practice.geeksforgeeks.org/problems/number-is-sparse-or-not-1587115620/1 (GeeksForGeeks - Number is sparse or not)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/679252/Fully-explained-using-XOR
#
# **************************************************************************
#
import unittest


class Solution(object):

    #
    # Assume that x has all bits alternating 0101 or like 1010
    # let y= x>>1
    #
    # since the bits are alternating, when you right shift them how will be the new bits compared to old bits????
    #
    # ALL bits will be flipped
    #
    # 1010 will become
    # 0101
    # and
    # 10101 will become
    # 01010
    #
    # How to detect that all bits are flipped??
    # thats why we use XOR
    # so if we take x^(x>>1) we should get 1111 all 1s
    #
    # next question ? how to detect 1111?
    #
    # if we add 1 to this number it will become power of 2
    #
    # we know how to detect power of 2 right? x&(x-1)==0
    #
    def hasAlternatingBits(self, n: int) -> bool:
        all_ones = n ^ (n >> 1)
        return (all_ones + 1) & all_ones == 0  # power of 2 test


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hasAlternatingBits(self) -> None:
        sol = Solution()
        for n, solution in ([5, True], [7, False], [2, True], [3, False]):
            self.assertEqual(solution, sol.hasAlternatingBits(n))


# main
if __name__ == "__main__":
    unittest.main()
