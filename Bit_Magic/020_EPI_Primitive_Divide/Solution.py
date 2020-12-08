#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Primitive Divide
#
# Description:
#
# Given two positive integers, compute their quotient, using only the addition, subtraction, and shifting operators.
#
# Hint: Relate x/y to (x - y)/y.
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/primitive_divide.py (EPI - Primitive Divide)
# **************************************************************************
#
from typing import List
import unittest


class Solution(object):

    # A brute-force approach is to iteratively subtract y from x until what remains
    # is less than y. The number of such subtractionsis exactly the quotient, x/y, and the
    # remainder is the term that's less than y. The complexity of the brute-force approach
    # is very high, e.g., when y = 1and x = 2^31 -1, it will take 231 -1iterations

    # Solution: Grade-School Division Algorithm.
    #
    # A better approach is to try and get more work done in each iteration. For example,
    # we can compute the largest `k` such that `2^k_y < x`, subtract `2^k_y` from `x`,
    # and add `2^k` to the quotient. For example, if x = (1011)2 and y = (10)2, then k = 2,
    # since `2 X 2^2 <= 11` and `2 X 2^3 > 11`.
    # We subtract (1000)2 from (1011)2 to get (11)2, add 2^k = 2^2 = (100)2 to the
    # quotient, and continue by updating x to (11)2.
    # The advantage of using `2^k * y` is that it can be computed very efficiently using shifting,
    # and `x` is at least halved in each iteration. If it takes `n` bits to represent `x/y`, there are
    # `O(n)` iterations. If the largest `k` such that `2^k_y < x` is computed by iterating through `k`,
    # each iteration has time complexity `O(n)`. This leads to an `O(n2)` algorithm.
    #
    # A better way to find the largest `k` in each iteration is to recognize that it keeps
    # decreasing. Therefore, instead of testing in each iteration whether 2^0_y,2^1_y,2^2_y,...
    # is less than or equal to x, after we initially find the largest k such that 2^k_y < x, in
    # subsequent iterations we test 2^k-1_y,2^k-2_y,2^k-3_y,... with x.
    #
    # For the example given earlier, after setting the quotient to (100)2 we continue with
    # (11)2- Now the largest k such that 2^k_y <= (11)2 is 0,so we add 2° = (1)2 to the quotient,
    # which is now (101)2. We continue with (11)2 -(10)2 = (1)2- Since (1)2 < y, we are
    # done—the quotient is(101)2 and the remainder is(1)2.
    #
    # Time Complexity: O(n^2)
    #                           n : the width of the operands.
    #
    # In essence, the program applies the grade-school division algorithm to binary numbers.
    # With each iteration, we process an additional bit. Therefore, assuming individual shift
    # and add operations take O(1) time, the time complexity is O(n).
    #
    def divide(self, x: int, y: int) -> int:
        result, power = 0, 32
        y_power = y << power
        while x >= y:
            while y_power > x:
                y_power >>= 1
                power -= 1

            result += 1 << power
            x -= y_power
        return result

    def divide_bsearch(self, x, y):
        if x < y:
            return 0

        power_left, power_right, power_mid = 0, x.bit_length(), -1
        while power_left < power_right:
            tmp = power_mid
            power_mid = power_left + (power_right - power_left) // 2
            if tmp == power_mid:
                break

            yshift = y << power_mid
            if yshift > x:
                power_right = power_mid
            elif yshift < x:
                power_left = power_mid
            else:
                return 1 << power_mid
        part = 1 << power_left
        return part | self.divide_bsearch(x - (y << power_left), y)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_primitive_divide(self) -> None:
        sol = Solution()
        for x, y, solution in (
            [64, 1, 64],
            [64, 2, 32],
            [64, 3, 21],
            [64, 4, 16],
            [64, 5, 12],
            [65, 2, 32],
            [4, 2, 2],
            [8186, 19, 430],
            [1313843, 515955, 2],
            [438, 1268, 0],
            [1441761, 7587904, 0],
        ):
            self.assertEqual(solution, sol.divide(x, y))
            self.assertEqual(solution, sol.divide_bsearch(x, y))


# main
if __name__ == "__main__":
    unittest.main()
