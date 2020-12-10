#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 191: Number of 1 Bits
#
# Description:
#
# Write a function that takes an unsigned integer and returns the number of '1' bits it has
# (also known as the Hamming weight).
#
#
# Note:
#
#   * Note that in some languages such as Java, there is no unsigned integer type. In this
#     case, the input will be given as a signed integer type. It should not affect your implementation,
#     as the integer's internal binary representation is the same, whether it is signed or unsigned.
#   * In Java, the compiler represents the signed integers using 2's complement
#     notation. Therefore, in Example 3 above, the input represents the signed integer.
#     -3.
#
# Follow up: If this function is called many times, how would you optimize it?
#
# Example 1:
#
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
#
# Example 2:
#
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
#
# Example 3:
#
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#
#
# Constraints:
#   * The input must be a binary string of length 32
#
# **************************************************************************
# Source:   https://leetcode.com/problems/number-of-1-bits/ (LeetCode - Problem 191 - Number of 1 Bits)
# **************************************************************************
#
#
import unittest


class Solution(object):
    def hammingWeight_using_builtin(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")

    def hammingWeight_using_bit_operation_iterative(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

    def hammingWeight_using_bit_operation_recursive(
        self, n: int, count: int = 0
    ) -> int:
        """
        :type n: int
        :rtype: int
        """
        return (
            self.hammingWeight_using_bit_operation_recursive(n & n - 1, count + 1)
            if n != 0
            else count
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hammingWeight(self) -> None:
        sol = Solution()
        for n, solution in (
            [0b00000000000000000000000000001011, 3],
            [0b00000000000000000000000010000000, 1],
            [0b11111111111111111111111111111101, 31],
        ):
            self.assertEqual(solution, sol.hammingWeight_using_builtin(n))
            self.assertEqual(
                solution, sol.hammingWeight_using_bit_operation_iterative(n)
            )
            self.assertEqual(
                solution, sol.hammingWeight_using_bit_operation_recursive(n)
            )


# main
if __name__ == "__main__":
    unittest.main()
