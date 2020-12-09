#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Generate Uniform Random Numbers
#
# Description:
#
# This problem is motivated by the following scenario. Six friends have to select
# a designated driver using a single unbiased coin. The process should be fair to
# everyone.
#
# How would you implement a random number generator that generates a random
# integer i between a and b,inclusive, given a random number generator that produces
# zero or one with equal probability? All values in [a, b] should be equally likely.
#
# Hint: How would you mimic a three-sided coin with a two-sided coin?
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/uniform_random_number.py (EPI - Generate Uniform Random Numbers)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import random
import unittest


class Solution(object):
    def zero_one_random(self):
        return random.randrange(2)

    def uniform_random(self, lower_bound: int, upper_bound: int) -> int:

        number_of_outcomes = upper_bound - lower_bound + 1
        while True:
            result, i = 0, 0
            while (1 << i) < number_of_outcomes:
                # zero_one_random() is the provided random number generator.
                result = (result << 1) | self.zero_one_random()
                i += 1
            if result < number_of_outcomes:
                break
        return result + lower_bound


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_uniform_random(self) -> None:
        sol = Solution()
        for lower_bound, upper_bound in (
            [0, 10],
            [10, 25],
            [1, 100],
            [0, 999],
            [0, 9999],
            [999, 1000],
            [0, 1],
        ):
            self.assertTrue(
                lower_bound
                <= sol.uniform_random(lower_bound, upper_bound)
                <= upper_bound
            )


# main
if __name__ == "__main__":
    unittest.main()
