#
# Time  : O(n^2)
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks : Count number of hops
#
# Description:
#
# A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top. As the answer will be large find the answer modulo 1000000007.
#
# Example 1:
#
# Input:
# N = 1
# Output: 1
# Example 2:
#
# Input:
# N = 4
# Output: 7
# Explanation:Below are the 7 ways to reach
# 4
# 1 step + 1 step + 1 step + 1 step
# 1 step + 2 step + 1 step
# 2 step + 1 step + 1 step
# 1 step + 1 step + 2 step
# 2 step + 2 step
# 3 step + 1 step
# 1 step + 3 step
#
# Your Task:
# Your task is to complete the function countWays() which takes 1 argument(N) and returns the answer%(10^9 + 7).
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 ≤ N ≤ 105
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/count-number-of-hops-1587115620/1 (GeeksForGeeks - Count number of hops)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://stackoverflow.com/questions/22562023/n-steps-with-1-2-or-3-steps-taken-how-many-ways-to-get-to-the-top
# https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
#
#
import functools

import unittest


class Solution(object):

    # Solution - 1
    # ===================================
    # Recursive Solution
    # Time Complexity   : O(n)
    # Space Complexity  : O(n)
    @functools.lru_cache(maxsize=None)
    def countWays_solution_1(self, n):
        if n < 4:
            initial = [1, 2, 4]
            return initial[n - 1]
        else:
            return (
                self.countWays_solution_1(n - 1)
                + self.countWays_solution_1(n - 2)
                + self.countWays_solution_1(n - 3)
            )

    # Solution - 2
    # ===================================
    # Recursive - O(log(n)) Solution
    # This tribonacci-by-doubling solution is analogous to the fibonacci-by-doubling solution
    # in the algorithms by Nayuki.
    # Note that multiplication has a higher complexity than constant.
    # This doesn't require or benefit from a cache.
    #
    # Reference:
    # Tribonacci Number     : http://mathworld.wolfram.com/TribonacciNumber.html
    # Algorithms by Nayuki  : https://www.nayuki.io/res/fast-fibonacci-algorithms/fastfibonacci.py
    #                         https://www.nayuki.io/page/fast-fibonacci-algorithms
    #
    # Time Complexity   : O(log(n))
    def countWays_solution_2(self, n):
        def recursive_tribonacci_tuple(n):
            """Return the n, n+1, and n+2 tribonacci numbers for n>=0.

            Tribonacci forward doubling identities:
            T(2n)   = T(n+1)^2 + T(n)*(2*T(n+2) - 2*T(n+1) - T(n))
            T(2n+1) = T(n)^2 + T(n+1)*(2*T(n+2) - T(n+1))
            T(2n+2) = T(n+2)^2 + T(n+1)*(2*T(n) + T(n+1))
            """
            assert n >= 0
            if n == 0:
                return 0, 0, 1  # T(0), T(1), T(2)

            a, b, c = recursive_tribonacci_tuple(n // 2)
            x = b * b + a * (2 * (c - b) - a)
            y = a * a + b * (2 * c - b)
            z = c * c + b * (2 * a + b)

            return (x, y, z) if n % 2 == 0 else (y, z, x + y + z)

        return recursive_tribonacci_tuple(n)[2]  # Is offset by 2 for the steps problem.

    # Solution - 3
    # ===================================
    # Iterative - O(n) Solution
    #
    # This is motivated by => https://stackoverflow.com/a/34593246/832230.
    # It is a modified tribonacci extension
    # of the iterative fibonacci solution (https://stackoverflow.com/a/15047141/832230).
    # It is modified from tribonacci in that it returns c, not a.
    #
    # Time Complexity   : O(log(n))
    def countWays_solution_3(self, n):
        a, b, c = 0, 0, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c

    # Solution - 4
    # ===================================
    # Iterative O(log(n)) (left to right)
    #
    # This is per a comment for this answer. This modified iterative
    # tribonacci-by-doubling solution is derived from the
    # corresponding recursive solution.
    # For some background,
    #   see
    #       here => https://en.wikipedia.org/wiki/Exponentiation_by_squaring#Basic_method
    #       and
    #       here => http://eli.thegreenplace.net/2009/03/21/efficient-integer-exponentiation-algorithms
    #
    #  It is modified from tribonacci in that it returns c, not a.
    #  Note that multiplication has a higher complexity than constant.
    #
    # The bits of n are iterated from left to right,
    # i.e. MSB => https://en.wikipedia.org/wiki/Most_significant_bit
    #      to
    #      LSB => https://en.wikipedia.org/wiki/Least_significant_bit.
    #
    # Notes:
    #   * list(range(m - 1, -1, -1)) == list(reversed(range(m)))
    #   * If the bit is odd (1), the sequence is advanced by one iteration.
    #     This intuitively makes sense after understanding the same for the
    #     efficient integer exponentiation problem.
    #
    # Time Complexity   : O(log(n))
    def countWays_solution_4(self, n):
        """Return the n+2 tribonacci number for n>=0.

        Tribonacci forward doubling identities:
        T(2n)   = T(n+1)^2 + T(n)*(2*T(n+2) - 2*T(n+1) - T(n))
        T(2n+1) = T(n)^2 + T(n+1)*(2*T(n+2) - T(n+1))
        T(2n+2) = T(n+2)^2 + T(n+1)*(2*T(n) + T(n+1))
        """
        assert n >= 0
        a, b, c = 0, 0, 1  # T(0), T(1), T(2)
        for i in range(n.bit_length() - 1, -1, -1):  # Left (MSB) to right (LSB).
            x = b * b + a * (2 * (c - b) - a)
            y = a * a + b * (2 * c - b)
            z = c * c + b * (2 * a + b)
            bit = (n >> i) & 1
            a, b, c = (y, z, x + y + z) if bit else (x, y, z)
        return c

    # Solution - 5
    # ===================================
    # Iterative O(log(n)) (right to left)
    #
    # This is per a comment for this answer.
    # The bits of n are iterated from right to left, i.e. LSB to MSB.
    # This approach is probably not prescriptive.
    #
    # Time Complexity   : O(log(n))
    def countWays_solution_5(self, n):
        """Return the n+2 tribonacci number for n>=0.

        Tribonacci forward doubling identities:
        T(2n)   = T(n+1)^2 + T(n)*(2*T(n+2) - 2*T(n+1) - T(n))
        T(2n+1) = T(n)^2 + T(n+1)*(2*T(n+2) - T(n+1))
        T(2n+2) = T(n+2)^2 + T(n+1)*(2*T(n) + T(n+1))

        Given Tribonacci tuples (T(n), T(n+1), T(n+2)) and (T(k), T(k+1), T(k+2)),
        we can "add" them together to get (T(n+k), T(n+k+1), T(n+k+2)).

        Tribonacci addition formulas:
        T(n+k)   = T(n)*(T(k+2) - T(k+1) - T(k)) + T(n+1)*(T(k+1) - T(k)) + T(n+2)*T(k)
        T(n+k+1) = T(n)*T(k) + T(n+1)*(T(k+2) - T(k+1)) + T(n+2)*T(k+1)
        T(n+k+2) = T(n)*T(k+1) + T(n+1)*(T(k) + T(k+1)) + T(n+2)*T(k+2)
        When n == k, these are equivalent to the doubling formulas.
        """
        assert n >= 0
        a, b, c = 0, 0, 1  # T(0), T(1), T(2)
        d, e, f = 0, 1, 1  # T(1), T(2), T(3)
        for i in range(n.bit_length()):  # Right (LSB) to left (MSB).
            bit = (n >> i) & 1
            if bit:
                # a, b, c += d, e, f
                x = a * (f - e - d) + b * (e - d) + c * d
                y = a * d + b * (f - e) + c * e
                z = a * e + b * (d + e) + c * f
                a, b, c = x, y, z
            # d, e, f += d, e, f
            x = e * e + d * (2 * (f - e) - d)
            y = d * d + e * (2 * f - e)
            z = f * f + e * (2 * d + e)
            d, e, f = x, y, z
        return c

    # Solution - 6
    # ===================================
    # Approximations
    #
    # Approximations are of course useful mainly for very large n. The exponentiation operation is used.
    # Note that exponentiation has a higher complexity than constant.
    #
    # The approximation below was tested to be correct till n = 53, after which it differed.
    #
    # Time Complexity   : O(log(n))
    def countWays_solution_6(self, n):
        a_pos = (19 + 3 * (33 ** 0.5)) ** (1.0 / 3)
        a_neg = (19 - 3 * (33 ** 0.5)) ** (1.0 / 3)
        b = (586 + 102 * (33 ** 0.5)) ** (1.0 / 3)
        return round(
            3 * b * ((1.0 / 3) * (a_pos + a_neg + 1)) ** (n + 1) / (b ** 2 - 2 * b + 4)
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countWays(self) -> None:
        sol = Solution()
        for n, solution in ([1, 1], [4, 7]):
            self.assertEqual(solution, sol.countWays_solution_1(n))
            self.assertEqual(solution, sol.countWays_solution_2(n))
            self.assertEqual(solution, sol.countWays_solution_3(n))
            self.assertEqual(solution, sol.countWays_solution_4(n))
            self.assertEqual(solution, sol.countWays_solution_5(n))
            self.assertEqual(solution, sol.countWays_solution_6(n))


# main
if __name__ == "__main__":
    unittest.main()
