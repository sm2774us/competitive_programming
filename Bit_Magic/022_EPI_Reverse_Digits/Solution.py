#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Reverse Digits
#
# Description:
#
# Write a program which takes an integer and returns the integer corresponding to the
# digits of the input written in reverse order. For example, the reverse of 42 is 24, and
# the reverse of -314 is-413.
#
# Hint: How would you solve the same problem if the input is presented as a string?
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/reverse_digits.py (EPI - Reverse Digits)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import unittest


class Solution(object):
    def reverse(self, x: int) -> int:
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        return -result if x < 0 else result


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverse(self) -> None:
        sol = Solution()
        for x, solution in (
            [1683683571, 1753863861],
            [1799113645, 5463119971],
            [2138559785, 5879558312],
            [-1856396381, -1836936581],
            [1296932912, 2192396921],
            [-778610391, -193016877],
            [-1203840386, -6830483021],
            [1963072368, 8632703691],
            [-363773848, -848377363],
            [-1299988089, -9808899921],
            [388359, 953883],
            [-388359, -953883],
        ):
            self.assertEqual(solution, sol.reverse(x))


# main
if __name__ == "__main__":
    unittest.main()
