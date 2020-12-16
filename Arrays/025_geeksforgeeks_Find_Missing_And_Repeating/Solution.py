#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Find Missing And Repeating
#
# Given an unsorted array Arr of size N of positive integers.
# One number 'A' from set {1, 2, ... N} is missing and
# one number 'B' occurs twice in array. Find these two numbers.
#
# Example 1:
#
# Input:
# N = 2
# Arr[] = {2, 2}
# Output: 2 1
# Explanation: Repeating number is 2 and
# smallest positive missing number is 1.
#
# Example 2:
#
# Input:
# N = 3
# Arr[] = {1, 3, 3}
# Output: 3 2
# Explanation: Repeating number is 3 and
# smallest positive missing number is 2.
#
# Your Task:
# --------------------------------------
# You don't need to read input or print anything. Your task is to complete the function findTwoElement()
# which takes the array of integers arr and n as parameters and returns an array of integers of size 2
# denoting the answer ( The first index contains B and second index contains A.)
#
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 ≤ N ≤ 105
# 1 ≤ Arr[i] ≤ N
#
# **************************************************************************
# Source:
#   https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1 (GeeksForGeeks - Find Missing And Repeating)
#
# Reference:
#   https://gist.github.com/AshishNamdev/c1614cc2d7ca6d15f44c84bbd4be1289
#   https://www.techiedelight.com/find-missing-number-duplicate-elements-array/
# **************************************************************************
#
from typing import List

# from typing import Tuple
from math import log2

import collections

import unittest


class Solution:
    def find_repeating_number_solution_1(self, arr: List[int]) -> int:
        """
        """
        repeating_number = []
        for number in arr:
            if number not in repeating_number:
                repeating_number.append(number)
            else:
                repeating_number = number
                break
        return repeating_number

    def find_missing_number_solution_1(self, arr: List[int]) -> int:
        """
        """
        missing_number = 0
        for i in range(len(arr)):
            if i not in arr:
                missing_number = i
        return missing_number

    def findTwoElements_solution_1(self, arr: List[int], n: int) -> str:
        return "%d %d" % (
            self.find_repeating_number_solution_1(arr),
            self.find_missing_number_solution_1(arr),
        )

    # Function to find the missing number and duplicate element
    # using XOR operator in a list of size n and range of
    # elements between [1 to n]
    #
    # Solution Explanation:
    # ----------------------------
    # We can solve this problem in O(n) time and in O(1) space using XOR operator.
    # We know that if we XOR a number with itself an odd number of times the result is the number itself,
    # otherwise, if we XOR a number an even number of times with itself, the result is 0.
    # Also XOR with 0 is always the number itself.
    #
    # XOR with 0
    # x ^ 0 = x
    #
    # XOR x with itself even number of times
    # x ^ x = 0
    # x ^ x ^ x ^ x = (x ^ x) ^ (x ^ x) = 0 ^ 0 = 0
    #
    # XOR x with itself odd number of times
    # (x ^ x ^ x) = (x ^ (x ^ x)) = (x ^ 0) = x
    # (x ^ x ^ x ^ x ^ x) = (x ^ (x ^ x) ^ (x ^ x)) = (x ^ 0 ^ 0) = x
    #
    # So, if we take XOR of all elements present in the array with every element in the range[1 ... n],
    # even appearing elements will cancel out each other and we are left with XOR of x and y (x ^ y)
    # where x and y are duplicate and missing elements.
    # Note:
    #   1) the duplicate element will be XORed 3 times in total.
    #   2) the missing element will be XORed 1 time
    #   3) all other elements will be XORed twice
    #
    # How to find x (repeating element) and y (missing element) ?
    #
    # res = (x ^ y)
    #
    # We know that any set bit in 'res' will be either set in x or y (but not in both - as a bit will only set
    # in res when it is set in one number and unset in the other).
    #
    # The idea is to consider the rightmost set bit in res (or any other set bit) and split the array/range into two lists -
    #   1. First list contains all elements of the array and numbers in range that have this bit set.
    #   2. Second list contains all elements of the array and numbers in range that have this bit unset.
    #
    # As rightmost bit is set in one number and unset in the other, we will have duplicate element present in
    # one list, and, missing number present in the other. Basically we have isolated trait of one number with other
    # so that both x and y will go to different lists.
    #
    # Now we iterate both lists once more, do XOR on each element of the list and the result will be the duplicate element
    # present in one list and missing number present in the other list (since elements appearing twice will cancel
    # each other).
    def findTwoElements_solution_2(self, arr: List[int], n: int) -> str:
        # take XOR of all list elements from index [0 to n-1]
        # and all numbers in range [1 to n]
        res = n
        for i in range(n):
            res = res ^ arr[i] ^ i

        # x, y stores the duplicate element and missing number
        x = y = 0

        # res stores (x ^ y)

        # find position of the rightmost set bit in res
        k = int(log2(res & -res))

        # split the list into two sublists
        for i in range(len(arr)):
            # list elements that have k'th bit 1
            if (arr[i] & (1 << k)) == 1:
                x = x ^ arr[i]
            # list elements that have k'th bit 0
            else:
                y = y ^ arr[i]

        # split the range [1-n] into two sub-range
        for i in range(1, n + 1):
            # number i have k'th bit 1
            if (i & (1 << k)) == 1:
                x = x ^ i
            # number i have k'th bit 0
            else:
                y = y ^ i

        # # linear search for missing element
        # print("Duplicate and missing elements are ", end='')
        # if x in arr:
        #     print(x, "and", y)
        # else:
        #     print(y, "and", x)
        # if x in arr:
        ans = "{0} {1}".format(x, y) if x in arr else "{0} {1}".format(y, x)
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findTwoElements(self) -> None:
        s = Solution()
        for arr, solution in ([[2, 2], "2 1"], [[1, 3, 3], "3 2"]):
            self.assertEqual(
                solution,
                s.findTwoElements_solution_1(arr, len(arr)),
                "Should find the repeating number and the missing number in the given array",
            )
            self.assertEqual(
                solution,
                s.findTwoElements_solution_2(arr, len(arr)),
                "Should find the repeating number and the missing number in the given array",
            )


if __name__ == "__main__":
    unittest.main()
