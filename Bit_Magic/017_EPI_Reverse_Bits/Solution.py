#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Reverse Bits
#
# Description:
#
# Write a program that takes a 64-bit word and returns the 64-bit word consisting of
# the bits of the input word in reverse order. For example, if the input is alternating Is
# and Os, i.e., (1010...10), the outputshould be alternating Os and Is, i.e., (0101...01).

# Hint: Use a lookup table
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/parity.py (EPI - Reverse Bits)
# **************************************************************************
#
from typing import List
import unittest


class Solution(object):
    def __init__(self):
        self.PRECOMPUTED_REVERSE = [
            self.reverse_bits_solution_1_brute_force(i, 15) for i in range(1 << 16)
        ]

    def swap_bits(self, x: int, i: int, j: int) -> int:
        # Extract the i-th and j-th bits, and see if they differ.
        if (x >> i) & 1 != (x >> j) & 1:
            # i-th and j-th bits differ. We will swap them by flipping their values.
            # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
            # when x = 0, we can perform the flip XOR.
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        return x

    # Solution 1 : Brute Force
    #
    # If we need to perform this operation just once, there is a simple bruteforce algorithm:
    # iterate through the 32 least significant bits of the input, and swap each with the corresponding
    # mostsignificant bit, using,for example, the approach in 015_EPI_Python_Computing_Parity_Of_A_Word.
    #
    def reverse_bits_solution_1_brute_force(self, x: int, n: int = 63) -> int:
        i, j = 0, n
        while i < j:
            x = self.swap_bits(x, i, j)
            i += 1
            j -= 1
        return x

    # Solution 2 : A precomputed lookup table based solution
    #
    # To implement reverse when the operation is to be performed repeatedly, we look
    # more carefully at the structure of the input, with an eye towards using a cache.
    # Let the input consist of the four 16-bit words y3,y2,y1,yo with y3 holding the most
    # significant bits. Then the 16 least significant bits in the reverse come from 1/3. To be
    # precise, these bits appear in the reverse order in which they do in 1/3. For example, if
    # 1/3 is(1110000000000001), then the 16 LSBs of the result are (1000000000000111).
    #
    # Similar to computing parity (015_EPI_Python_Computing_Parity_Of_A_Word), a very fast way to reverse
    # bits for 16-bit words when we are performing many reverses is to build an array-based lookup-table
    # `A` such that for every 16-bit number `y`, `A[y]` holds the bit-reversal of `y`.
    # We can then form the reverse of `x` with the reverse of `y0` in the most significant
    # bit positions, followed by the reverse of `y1`, followed by the reverse of `y2` followed by
    # the reverse of `y3`.
    #
    # We illustrate the approach with 8-bit words and 2-bit lookup table keys. The
    # table is rev = ((00),(10),(01),(11)). If the input is (10010011), its reverse is
    # rev(ll),rev(00),rev(01),rev(10), i.e., (11001001).
    #
    # Time Complexity: O(n/L)
    #                           n : n-bit integers
    #                           L : L-bit cache keys
    #
    def reverse_bits_solution_2_lookup_table(self, x):
        mask_size = 16
        bit_mask = 0xFFFF
        return (
            self.PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size)
            | self.PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size)
            | self.PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size
            | self.PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask]
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverse_bits(self) -> None:
        sol = Solution()
        for x, solution in (
            [1351510410656, 405942121183313920],
            [528, 594475150812905472],
            [425765368052, 3391185800900116480],
            [6, 6917529027641081856],
            [970, 6034823500676464640],
        ):
            self.assertEqual(solution, sol.reverse_bits_solution_1_brute_force(x))
            self.assertEqual(solution, sol.reverse_bits_solution_2_lookup_table(x))


# main
if __name__ == "__main__":
    unittest.main()
