#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Longest Consecutive 1's
#
# Description:
#
# Given a number N. The task is to find the length of the longest consecutive 1s in its binary representation.
#
# Example 1:
#
# Input: N = 14
# Output: 3
# Explanation: Binary representation of 14 is
# 1110, in which 111 is the longest consecutive
# set bits of length is 3.
# Example 2:
#
# Input: N = 222
# Output: 4
# Explanation: Binary representation of 222 is
# 11011110, in which 1111 is the longest
# consecutive set bits of length 4.
#
# Your Task: The task is to complete the function maxConsecutiveOnes() which returns the length of the longest consecutive 1s in the binary representation of given N.
#
# Expected Time Complexity: O(log N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 <= N <= 10^6
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1 (GeeksForGeeks - Longest Consecutive 1's)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# https://www.geeksforgeeks.org/length-longest-consecutive-1s-binary-representation/
#
# **************************************************************************
#
import unittest


class Solution(object):

    #
    #   Naive Approach: One simple way would be to simply loop over the bits,
    #   and keep track of the number of consecutive set bits, and the maximum that this value has reached.
    #   In this approach, we need to convert it to binary (base-2) representation and then find and print the result.
    #
    #   Using Bit Magic: The idea is based on the concept that if we AND a bit sequence with a shifted version
    #   of itself, we’re effectively removing the trailing 1 from every sequence of consecutive 1s.
    #
    #       11101111   (x)
    #     & 11011110   (x << 1)
    #     ----------
    #       11001110   (x & (x << 1))
    #         ^    ^
    #         |    |
    #    trailing 1 removed
    #
    #   So the operation x = (x & (x << 1)) reduces length of every sequence of 1s by one in binary representation of x.
    #   If we keep doing this operation in a loop, we end up with x = 0. The number of iterations required to reach 0
    #   is actually length of the longest consecutive sequence of 1s.
    #
    def maxConsecutiveOnes(self, x: int) -> int:
        # Initialize result
        count = 0

        # Count the number of iterations to
        # reach x = 0.
        while x != 0:
            # This operation reduces length
            # of every sequence of 1s by one.
            x = x & (x << 1)

            count = count + 1

        return count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxConsecutiveOnes(self) -> None:
        sol = Solution()
        for n, solution in ([14, 3], [222, 4]):
            self.assertEqual(solution, sol.maxConsecutiveOnes(n))


# main
if __name__ == "__main__":
    unittest.main()
