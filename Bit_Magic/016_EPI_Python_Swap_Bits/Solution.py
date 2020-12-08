#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Swap Bits
#
# Description:
#
# Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/swap_bits.py (EPI - Swap Bits)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):
    def swap_bits(self, x: int, i: int, j: int) -> int:
        # Extract the i-th and j-th bits, and see if they differ.
        if (x >> i) & 1 != (x >> j) & 1:
            # i-th and j-th bits differ. We will swap them by flipping their values.
            # Select the bits to flip with bit_mask. Since x^1 = 0 when x = 1 and 1
            # when x = 0, we can perform the flip XOR.
            bit_mask = (1 << i) | (1 << j)
            x ^= bit_mask
        return x


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_swap_bits(self) -> None:
        sol = Solution()
        for x, i, j, solution in (
            [73, 1, 6, 11],
            [19574056046756, 15, 14, 19574056063140],
            [106, 3, 7, 226],
            [4, 0, 0, 4],
            [18875686394025, 0, 40, 18875686394025],
            [1585902379909443641, 26, 41, 1585902379909443641],
            [1972974, 12, 4, 1968894],
        ):
            self.assertEqual(solution, sol.swap_bits(x, i, j))


# main
if __name__ == "__main__":
    unittest.main()
