#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks: Find first set bit AKA Find Index of LSB - (Least Significant Bit)
#
# Description:
#
# Given an integer an N. The task is to return the position of first set bit found
# from the right side in the binary representation of the number.
#
# Note: If there is no set bit in the integer N, then return 0 from the function.
#
# Example 1:
# Input: N = 18
# Output: 2
# Explanation: Binary representation of 18 is 010010,
# the first set bit from the right side is at position 2.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases .
# Then T test cases follow. Each test case contains an integer x denoting the no of words in the dictionary.
# Then in the next line are x space separated strings denoting the contents of the dictinory.
# In the next line are two integers N and M denoting the size of the boggle. The last line of each test case contains NxM space separated values of the boggle.
#
# Example 2:
# Input: N = 12
# Output: 3
# Explanation: Binary representation of  12 is 1100,
# the first set bit from the right side is at position 3.
#
# Your Task:
# The task is to complete the function getFirstSetBit() that takes an integer n as a parameter and returns the position of first set bit.
#
# Expected Time Complexity: O(log N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
#   * 0 <= N <= 106
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1 (GeeksForGeeks - Find first set bit)
# **************************************************************************
#
# Reference:
# **************************************************************************
# https://stackoverflow.com/questions/5520655/return-index-of-least-significant-bit-in-python (Stackoverflow: return index of least significant bit in Python)
#
from math import log2

import unittest

class Solution(object):

    #
    # To explain how this works, in twos complement integer negation is equivalent to bitwise negation
    # followed by adding one.
    #
    # Adding one to a bit flips it and if the bit was previously one produces a carry
    # and thereby adding one to the next bit.
    #
    # The result of this is the only bit that is 1 in both x and -x is the
    # least significant bit (LSB) that was 1 in x.
    #
    # Python3 Learning Points:
    #
    # Q1> What does &- mean?
    # A1> It's x & (-x): bit-wise AND of x and negative x
    #
    # Q2> What does the expression x & (x - 1) do?
    # A2> The expression `x & (x - 1)` clears the LSB.
    def getFirstSetBit_solution_1(self, n: int) -> int:
        """Returns the index, counting from 0, of the
        least significant set bit in `x`.
        """
        return ((n & -n).bit_length() - 1) + 1

    #
    # n & -n first turns off all bits other than the rightmost bit that was originally set to 1,
    # then it takes the log2 of that resulting number to get its power-of-2
    # (which happens to be the same value as the 0-based position of the bit that was set to 1),
    # and finally adds 1 to that result to get a 1-based bit position
    # (which is weird since bits are typically referred to by their 0-based positions instead).
    #
    # Python3 Learning Points:
    #
    # Q1> What's the function of log2 in bit-manipulation?
    # A1> log2 ( log to the base 2 ) of any number yields its power-of-2,
    #     which happens to be the same value as the 0-based position of the bit that was set to 1.
    #
    def getFirstSetBit_solution_2(self, n: int) -> int:
        """Returns the index, counting from 0, of the
        least significant set bit in `n`. If no bit is set, returns 0.
        """
        return (int(log2(n & -n)))+1 if n else 0

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getFirstBit(self) -> None:
        sol = Solution()
        for n, solution in (
            [18,2],
            [12,3],
            [0,0]
        ):
            self.assertEqual(solution, sol.getFirstSetBit_solution_1(n))
            self.assertEqual(solution, sol.getFirstSetBit_solution_2(n))


# main
if __name__ == "__main__":
    unittest.main()
