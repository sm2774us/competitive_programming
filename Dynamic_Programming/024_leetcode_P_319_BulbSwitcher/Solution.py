#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 319: Bulb Switcher
#
# Description: Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/bulb-switcher/ (LeetCode - Problem 319 - Bulb Switcher)
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# Before we take a jump to the solution, let's first try to clear out what exactly the problem is talking about:
#
#   * every i-th distance you switch the bulb to the opposite state (from on to off, or from off to on);
#     actually suppose the bulbs are labelled from 1 to n then the every second bulb will mean that 2, 4, 6, 8, ...
#     all even numbers less than n; while every third bulb will be 3, 6, 9, 12, ... all multiples of 3
#     that is less than n and so on;
#   * since the bulb will only have two different states - on or off, the result will be quite clear now;
#     odd switching operations will result in bulb-on state (since original state is bulb-off)
#     while even switching operations will give us bulb-off state;
#
# Now the purpose here is clear searching for the odd-operation numbers:
#
#   * as for primes, they only have 1 and itself as their factors, even-operation numbers;
#   * as for non-primes, normally they will have different pairs of factors like 12 whose factors
#     are (1, 12), (3, 4), (2, 6) - 6 different factors, also even-operation numbers;
#   * but among non-primes, there are some special numbers, perfect square numbers like 9 whose factors are (1, 9) and (3, 3) - odd-operation numbers, which means there will be only three different numbers that will affect the current bulb and result in bulb-on state!
#
# So that's all we need to know to hack this problem now. But how to get the amount of squares that are less than n,
# quite simple. Sqrt(n) is the answer, since all square numbers that is less than n will be 1, 4, 9 ... n
# and their corresponding square roots will be 1, 2, 3,... sqrt(n).
#
# Space Complexity: O(1)
# Time Complexity : O(1)
#
#
import math
import unittest


class Solution(object):

    # Solution_1: Using math
    #
    # I try explain my though as following:
    #
    # How many "on" at the end of nth toggle?
    #
    # --> "on" or "off" at each position in an array of length n?
    #
    # --> toggle even number times will result in "on", toggle odd number times will result in "off"
    #
    # --> for position k, the number of toggles is the number of distinct divisors that k has
    #
    # --> divisors always come in pair, which means even number of divisors, for example, 12 has (1,12),(2,6),(3,4).
    #
    # --> however, Square Number has odd number of divisors, e.g. 25 has 1,25,5
    #
    # --> thus, the number of "on", is the number of perfect square number <= n
    def bulbSwitch_solution_1_math(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))

    # Solution_2 : Using numpy makes this solution much faster
    #
    # Time Complexity: O(n^2)
    def bulbSwitch_solution_2_numpy(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(0, n + 1, i):
                a[j] = 1 - a[j]
        return sum(a[1:])
        # if numpy is available for use in interview => then use the below solution
        # a = [0] * (n + 1)
        # a = numpy.array(a)
        # for i in xrange(1, n + 1):
        #     a[::i] = 1 - a[::i]
        # return sum(a[1:])

    # Solution_3 : variation of sqrt() makes use of the property of square numbers
    #
    # Seemingly method 4 does not look like sqrt(), it make use of the property of square numbers.
    # The difference between two square numbers` different is 2:
    # eg.
    #
    # original number     square number    difference
    # 1                      1
    # 2                      4             3   （4-1）
    # 3                      9             5   （9-4）
    # 4                     16             7   （16-7）
    # 5                     25             9    （25-16）
    #
    # That`s why we say it is a variation of sqrt().
    def bulbSwitch_solution_3_sqrt_variation_making_use_of_property_of_square_numbers(
        self, n: int
    ) -> int:
        """
        :type n: int
        :rtype: int
        """
        res, p = 0, 0
        if n == 0:
            return 0
        elif n < 4:
            return 1
        elif n == 4:
            return 2
        for i in range(3, n + 1, 2):
            res += 1
            p += i
            if n <= p:
                break
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_bulbSwitch(self) -> None:
        sol = Solution()
        for n, solution in ([3, 1], [0, 0], [1, 1]):
            self.assertEqual(solution, sol.bulbSwitch_solution_1_math(n))
            self.assertEqual(solution, sol.bulbSwitch_solution_2_numpy(n))
            self.assertEqual(
                solution,
                sol.bulbSwitch_solution_3_sqrt_variation_making_use_of_property_of_square_numbers(
                    n
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
