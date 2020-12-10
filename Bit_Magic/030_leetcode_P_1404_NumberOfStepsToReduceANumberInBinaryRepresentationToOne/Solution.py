#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1404: Number of Steps to Reduce a Number in Binary Representation to One
#
# Description:
#
# Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:
#
# If the current number is even, you have to divide it by 2.
#
# If the current number is odd, you have to add 1 to it.
#
# It's guaranteed that you can always reach to one for all testcases.
#
#
#
# Example 1:
#
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14.
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.
# Step 5) 4 is even, divide by 2 and obtain 2.
# Step 6) 2 is even, divide by 2 and obtain 1.
# Example 2:
#
# Input: s = "10"
# Output: 1
# Explanation: "10" corressponds to number 2 in their decimal representation.
# Step 1) 2 is even, divide by 2 and obtain 1.
# Example 3:
#
# Input: s = "1"
# Output: 0
#
#
# Constraints:
#
#   * 1 <= s.length <= 500
#   * s consists of characters '0' or '1'
#   * s[0] == '1'
#
# **************************************************************************
# Source:   https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/ (LeetCode - Problem 1404 - Number of Steps to Reduce a Number in Binary Representation to One)
# **************************************************************************
#
from collections import Counter
from functools import reduce
from operator import xor
import unittest


class Solution(object):

    # Solution 1 :  Bitwise Operator Solution => O(N) time, O(1) space without converting entire string to integer
    #
    # Algorithm:
    # -----------
    # 1. Traverse the string in reverse
    # 2. For every char, carry = carry & s[i] (carry = 1, if both carry and s[i] are 1)
    # 3. And digit at ith place = carry ^ s[i] (if carry and s[i] are 1, digit will be 0)
    # 4. Thus if digit is 0, increment result by 1 (for even digits)
    # 5. If digit is 1, then increment the result by 2 (once for adding 1 and making
    # 6. last digit even and then dividing by 2). And carry = 1
    # 7. Repeat for all characters in s
    #
    # TC: O(N)
    # SC: O(1)
    #
    def numSteps_solution_1_bitwise_operator_without_converting_entire_string_to_int(
        self, s: str
    ) -> int:
        """
        :type s: str
        :rtype: int
        """
        carry = 0
        result = 0

        for i in range(len(s) - 1, 0, -1):
            n = int(s[i])
            carry, sm = carry & n, carry ^ n
            if sm == 0:
                result += 1
            else:
                carry = 1
                result += 2
        if carry:
            result += 1
        return result

    # Solution 2 :  One-Liner - Using XOR to find a single character
    #
    # Algorithm:
    # -----------
    # 1. find the first 0 from the end and toggle every subsequent digit - for odd
    # 2. remove the last index - for even
    #
    # TC: O(N)
    # SC: O(N)
    #
    def numSteps_solution_2_bitwise_operator_odd_and_even(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        n, steps = [int(i) for i in s], 0
        while n != [1]:
            if n[-1] == 0:
                # for even
                n = n[:-1]
            else:
                # for odd
                found = False
                for i in range(len(n) - 1, -1, -1):
                    if n[i] == 1:
                        n[i] = 0
                    else:
                        n[i] = 1
                        found = True
                        break
                if not found:
                    n = [1] + n
            steps += 1
        return steps


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_numSteps(self) -> None:
        sol = Solution()
        for s, solution in (["1101", 6], ["10", 1], ["1", 0]):
            self.assertEqual(
                solution,
                sol.numSteps_solution_1_bitwise_operator_without_converting_entire_string_to_int(
                    s
                ),
            )
            self.assertEqual(
                solution, sol.numSteps_solution_2_bitwise_operator_odd_and_even(s)
            )


# main
if __name__ == "__main__":
    unittest.main()
