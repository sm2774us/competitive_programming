#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Is Palindromic Number?
#
# Description:
#
# A palindromic string is one which reads the same forwards and backwards, e.g.,
# "redivider". In this problem, you are to write a program which determines if the
# decimal representation of an integer is a palindromic string. For example, your
# program should return true for the inputs 0,1,7,11,121,333, and 2147447412, and
# false for the inputs-1,12,100, and 2147483647.
#
# Write a program that takes an integer and determines if that integer'srepresentation
# as a decimal string is a palindrome.
#
# Hint: It's easy to come up with a simple expression that extracts the least significant digit. Can
# you find a simple expression for the most significant digit?
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/is_number_palindromic.py (EPI - Is Palindromic Number?)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import math
import unittest


class Solution(object):
    def is_palindrome_number(self, x: int) -> bool:
        if x <= 0:
            return x == 0

        num_digits = math.floor(math.log10(x)) + 1
        msd_mask = 10 ** (num_digits - 1)
        for i in range(num_digits // 2):
            if x // msd_mask != x % 10:
                return False
            x %= msd_mask  # Remove the most significant digit of x.
            x //= 10  # Remove the least significant digit of x.
            msd_mask //= 100
        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_is_palindrome_number(self) -> None:
        sol = Solution()
        for x, solution in (
            [7915, False],
            [-7915, False],
            [20692, False],
            [-20692, False],
            [904196, False],
            [-904196, False],
            [14, False],
            [-14, False],
            [30, False],
            [-30, False],
            [2982623, False],
            [-2982623, False],
            [496146024, False],
            [-496146024, False],
            [413, False],
            [-413, False],
            [230, False],
            [-230, False],
            [1941, False],
            [-1941, False],
            [9, True],
        ):
            self.assertEqual(solution, sol.is_palindrome_number(x))


# main
if __name__ == "__main__":
    unittest.main()
