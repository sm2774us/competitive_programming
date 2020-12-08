#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : FIND A CLOSEST INTEGER WITH THE SAME WEIGHT
#
# Description:
#
# Define the weight of a non-negative integer x to be the number of bits that are set to
# 1 in its binary representation. For example, since 92 in base-2 equals (1011100)2, the
# weight of 92 is 4.
#
# Write a program which takes as input a non-negative integer x and returns a number `y`
# which is not equal to `x`, but has the same weight as x and their difference,
# |y - x|, is as small as possible. You can assume `x` is not `0`, or all `1s`.
# For example, if `x = 6`, you should return `5`.
#
# Hint: Start with the least significant bit.
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/closest_int_same_weight.py (EPI - Find A Closest Integer With The Same Weight)
# **************************************************************************
#
import unittest


class Solution(object):

    # Solution 1 : Brute Force
    #
    # A brute-force approach might be to try all integers x-l,x+l,x-2,x+2, ,
    # stopping as soon as we encounter one with the same weight at x. This performs very
    # poorly on some inputs. One way to see this is to consider the case where x = 23 = 8.
    # The only numbers with a weight of 1 are powers of 2. Thus, the algorithm will try
    # the following sequence: 7,9,6,10,5,11,4, stopping at 4 (since its weight is the same
    # as 8's weight). The algorithm tries 23_1 numbers smaller than 8, namely, 7,6,5,4, and
    # 23_1 -1numbers greater than 8, namely, 9,10,11. This example generalizes. Suppose
    # x = 230. The power of 2 nearest to 230 is 229. Therefore this computation will evaluate
    # the weight of all integers between 230 and 229 and between 230 and 230 + 229 -1, i.e.,
    # over one billion integers
    #
    #

    # Solution 2 : Swapping the two right-most consecutive bits that diff
    #
    # Heuristically, it is natural to focus on the LSB of the input, specifically, to swap
    # the LSB with rightmost bit that differs from it. This yields the correct result for
    # some inputs, e.g., for (10)2 it returns (01)2, which is the closest possible. However,
    # more experimentation shows this heuristic does not work generally. For example,for
    # (111)2 (7 in decimal) it returns(1110)2 which is14 in decimal; however, (1011)2 (11 in
    # decimal) has the same weight, and is closer to (111)2.
    #
    # A little math leads to the correct approach. Suppose we flip the bit at index kl and
    # flip the bit at index k2, kl > k2. Then the absolute value of the difference between the
    # original integer and the new one is 2kl - 2kl. To minimize this, we should make kl as
    # small as possible and k2 as close to kl.
    #
    # Since we must preserve the weight, the bit at index kl has to be different from the
    # bit in k2, otherwise the flips lead to an integer with different weight. This means the
    # smallest kl can be is the rightmost bit that's different from the LSB, and k2 must be
    # the very next bit. In summary, the correct approach is to swap the two rightmost
    # consecutive bits that differ.
    #
    # Time Complexity: O(n)
    #                           n : the integer width
    #
    def closest_int_same_bit_count(self, x: int) -> int:
        num_unsigned_bits = 64
        for i in range(num_unsigned_bits - 1):
            if (x >> i) & 1 != (x >> (i + 1)) & 1:
                x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i + 1).
                return x

        # Raise error if all bits of x are 0 or 1.
        raise ValueError("All bits are 0 or 1")


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_closest_int_same_bit_count(self) -> None:
        sol = Solution()
        for x, solution in (
            [48, 40],
            [14, 13],
            [39698800462691, 39698800462693],
            [626143, 626159],
            [206, 205],
        ):
            self.assertEqual(solution, sol.closest_int_same_bit_count(x))


# main
if __name__ == "__main__":
    unittest.main()
