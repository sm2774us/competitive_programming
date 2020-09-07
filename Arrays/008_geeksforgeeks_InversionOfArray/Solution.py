#
# Time : O(logN); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given an array of positive integers. The task is to find inversion count of array.
#
# Inversion Count Definition:
# For an array, inversion count indicates how far (or close) the array
# is from being sorted. If array is already sorted then inversion count is 0.
# If array is sorted in reverse order that inversion count is the maximum.
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
#
# Example:
#
# Given input            => [2, 4, 1, 3, 5]
#       output should be => 3
#
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ N ≤ 107
# 1 ≤ C ≤ 1018
#
# **************************************************************************
#
# Explanation
#
# Given input            => X = [2,1,6], Y = [1,5], m = 3, n = 2
#       output should be => 3
#                           The pairs which follow xy > yx are as such: 2^1 > 1^2,  2^5 > 5^2 and 6^1 > 1^6
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/number-of-pairs/0/ (GeeksForGeeks - Inversion of array)
# Solution Hint: https://stackoverflow.com/a/23201616/4014959
# ( Answered by Niklas B. Apr 21 2014 at 16:40 )
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# Hint: Use a Binary Indexed Tree, aka a Fenwick tree
# https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
# We often need some sort of data structure to make our algorithms faster. In this article we will discuss about the
# Binary Indexed Trees structure, proposed by Peter M. Fenwick.
# This structure was first used for data compression, by Peter M. Fenwick.
# In algorithmic contests it is often used for storing frequencies and manipulating cumulative frequency tables.
#
# **************************************************************************
# You can use one to maintain prefix sums on the values of your permutation elements.
# Then you can just proceed from right to left and count for every element
# the number of elements smaller than it to the right.
#
# Uses the built-in sort to determine the ranking of array items, and a Binary Indexed Tree (aka Fenwick tree)
# to store the cumulative sums required to calculate the inversion count.
# **************************************************************************
# Another possible solution for smaller list sizes ( which ends being faster for list sizes under 40,000 or so ) is:
# **************************************************************************
# Another Python solution, short one.
# Makes use of builtin bisect module, which provides functions to insert element into its place
# in sorted array and to find index of element in sorted array.
#
# The idea is to store elements left of n-th in such array, which would allow us
# to easily find the number of them greater than n-th.
#
# "i & -i" - this is clear all bits "1", but last significant one. For example:
#
#         <2's complement binary integer>      <decimal representation of 2's complement>
#      i: 0b1101001010000000                => (-11648)dec10
#     -i: 0b0010110110000000                => (11648)dec10
# i & -i: 0b0000000010000000                => (128)dec10
#
#      i: 0b11010010 1 0000000
#     -i: 0b00101101 1 0000000
# i & -i: 0b00000000 1 0000000
#
# i(dec)   i(bin)     i&-i
#  1            1        1
#  5          101        1
#  8         1000     1000
# 12         1100     0100
#
from typing import List

from bisect import bisect, insort_left

import unittest


class Solution:

    # solution using a Binary Indexed Tree, aka a Fenwick tree
    # ( performs well on large list sizes and decently on small list sizes )
    def count_inversions(self, a: List[int]) -> int:
        res = 0
        counts = [0] * (len(a) + 1)
        rank = {v: i + 1 for i, v in enumerate(sorted(a))}
        for x in reversed(a):
            i = rank[x] - 1
            while -i:  # Returns the sum from index 1 to i
                res += counts[i]
                i -= (
                    i & -i
                )  # i & -i is used to increment i by the least significant 1 in the binary representation of i
            i = rank[x]
            while i <= len(a):  # Adds k to element with index i
                counts[i] += 1
                i += (
                    i & -i
                )  # i & -i is used to increment i by the least significant 1 in the binary representation of i
        return res

    # # solution for smaller list sizes
    # def count_inversions(a):
    #     sorted_left = []
    #     res = 0
    #     for i in xrange(1, len(A)):
    #         insort_left(sorted_left, A[i-1])
    #         # i is also the length of sorted_left
    #         # res += (i - bisect(sorted_left, A[i]))
    #     return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countPairs(self) -> None:
        s = Solution()
        for a, solution in ([[2, 4, 1, 3, 5], 3], [[5, 9, 13, 11, 7], 4]):
            self.assertEqual(
                solution,
                s.count_inversions(a),
                "Should return the inversion count of array",
            )


if __name__ == "__main__":
    unittest.main()
