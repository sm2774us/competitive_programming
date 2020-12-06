#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Swap all odd and even bits
#
# Description:
#
# Given an unsigned integer N. The task is to swap all odd bits with even bits.
# For example, if the given number is 23 (00010111), it should be converted to 43(00101011).
# Here, every even position bit is swapped with adjacent bit on right side(even position bits
# are highlighted in binary representation of 23), and every odd position bit is swapped with adjacent on left side.
#
# Input:
# The first line of input contains T, denoting the number of testcases. Each testcase contains single line.
#
# Output:
# For each testcase in new line, print the converted number.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 100
#
# Example:
# Input:
# 2
# 23
# 2
#
# Output:
# 43
# 1
#
# Explanation:
# Testcase 1: BInary representation of the given number; 00010111 after swapping 00101011.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits/0 (GeeksForGeeks - Swap all odd and even bits)
# **************************************************************************
#
#
import unittest


class Solution(object):

    # Bit Magic Numbers
    # 1) 0x55555555
    # ========================================================================
    # For getting all odd bits
    # use the number 0x55555555 => 01010101 01010101 01010101 01010101
    # ( a 32-bit number with all odd bits set as 1 and all even bits as 0 )

    # 2) 0xAAAAAAAA
    # ========================================================================
    # For getting all even bits
    # use the number 0xAAAAAAAA => 10101010 10101010 10101010 10101010
    # ( a 32-bit number with all even bits set as 1 and all odd bits as 0 )

    def swapOddAndEvenBits(self, num):
        # The number 0x55555555 is a
        # 32-bit number with all odd bits set as 1 and all even bits as 0
        # 01010101 01010101 01010101 01010101
        #
        # 1) Get all odd bits of x by doing bitwise and of x with 0x55555555.
        odd_bits = num & 0x55555555  # to extract odd bits of num

        # The number 0xAAAAAAAA is a
        # 32-bit number with all even bits set as 1 and all odd bits as 0
        # 10101010 10101010 10101010 10101010
        #
        # 2) Get all even bits of x by doing bitwise and of x with 0xAAAAAAAA.
        even_bits = num & 0xAAAAAAAA  # to extract even bits of num
        # 3) Left shift all odd bits.
        odd_bits = odd_bits << 1  # to shift odd bits to even position
        # 4) Right shift all even bits.
        even_bits = even_bits >> 1  # to shift even bits to odd position
        # 5) Combine new even and odd bits and return.
        new_num = odd_bits | even_bits  # combining odd and even bits
        return new_num

    # What's the trick?
    #
    # Consider your number as a vector of bits. Exchanging pairs of bits is equivalent to moving
    # all even-numbered bits one position to the left, and
    # all odd-numbered bits one position to the right (assuming bit numbering start at 0,
    # begining with the LSB on the right).
    #
    # Moving to the left and to the right is just a binary shift: n << 1 and n >> 1.
    # But if I simply do (n << 1) | (n >> 1), I will move all bits, and the result will be wrong.
    # So, first select which bits you want: the even bits are 0x55555555 & n, the odd bits are n & 0xAAAAAAAA.
    #
    # So a possibility is:
    #   ((n & 0x55555555) << 1) | ((n & 0xaaaaaaaa) >> 1)
    def swapOddAndEvenBitsOneLiner_Solution_1(self, num):
        return ((num & 0x55555555) << 1) | ((num & 0xAAAAAAAA) >> 1)

    # Another way is to select bits after the shift but before the binary or:
    #   ((n << 1) & 0xaaaaaaaa) | ((n >> 1) & 0x55555555)
    #
    # Since the bit parity is reversed by the shift, I just have to swap the constants 0x55555555 and 0xaaaaaaaa.
    #
    # To get the same constant on both side of the binary or, I select before the shift on one side,
    # and after on the other.
    #
    def swapOddAndEvenBitsOneLiner_Solution_2(self, num):
        return ((num << 1) & 0xAAAAAAAA) | ((num >> 1) & 0x55555555)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_swapOddAndEvenBits(self) -> None:
        sol = Solution()
        for num, solution in ([23, 43], [2, 1]):
            self.assertEqual(solution, sol.swapOddAndEvenBits(num))
            self.assertEqual(solution, sol.swapOddAndEvenBitsOneLiner_Solution_1(num))
            self.assertEqual(solution, sol.swapOddAndEvenBitsOneLiner_Solution_2(num))


# main
if __name__ == "__main__":
    unittest.main()
