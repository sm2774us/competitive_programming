#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 354: Russian Doll Envelopes
#
# Description:
#
# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
# Note:
# Rotation is not allowed.
#
# Example:
#
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#
# **************************************************************************
# Source: https://leetcode.com/problems/russian-doll-envelopes/ (LeetCode - Problem 354 - Russian Doll Envelopes)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Sort the array. Ascend on width and descend on height if width are same.
# Find the longest increasing subsequence based on height.
# Since the width is increasing, we only need to consider height.
# [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise
# it will be counted as an increasing number if the order is [3, 3], [3, 4]
#
# **************************************************************************
# More Elaborate Explanation
# **************************************************************************
# For those who do not understand why Long Increasing Subsequence (LIS) can solve the problem,
# I will try to explain based on my understanding.
#
#   * This problem is asking for LIS in two dimensions, width and height.
#   * Sorting the width reduces the problem by one dimension.
#       + If width is strictly increasing, the problem is equivalent to finding LIS in only the height dimension.
#       + However, when there is a tie in width, a strictly increasing sequence in height may not be a correct solution.
#           > For example, [[3,3] cannot fit in [3,4]].
#       + Sorting height in descending order when there is a tie prevents such a sequence to be included in the solution.
# **************************************************************************
# The same idea can be applied to problems of higher dimensions.
# For example, box fitting is three dimensions, width, height, and length.
#
#   * Sorting width ascending and height descending reduces the problem by one dimension.
#   * Finding the LIS by height further reduces the problem by another dimension.
#   * When find LIS based on only length, it becomes a standard LIS problem.
#
# **************************************************************************
# Visual Explanation of the 3-D problem
# **************************************************************************
# [width, height, length] sorted by width increasing (height decreasing):
# [1 2 1] [1 1 9]   [2 2 8]   [3 4 2] [3 3 7]   [4 4 6]
#
# The heights are:
# [_ 2 _] [_ 1 _]   [_ 2 _]   [_ 4 _] [_ 3 _]   [_ 4 _]
#
# Longest Increasing Subsequence (LIS) on heights gives us the following 4, instead of 6, candidates
# [_ 2 _]                     [_ 4 _] [_ 3 _]   [_ 4 _]
#
# This narrow down the searching space, now we only need to check 4 items, performing LIS on 3rd dimension, i.e., length:
# solution so far has 3 possible result:
# [1 2 1]                     [3 4 2]
# [1 2 1]                             [3 3 7]
# [1 2 1]                                       [4 4 6]
#
# **************************************************************************
#
from typing import List

# Cartesian product of input iterables.
# Roughly equivalent to nested for-loops in a generator expression. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
from itertools import product
import unittest


class Solution(object):

    # Dynamic Programming - Knapsack - Solution ( Using 2D Array )
    #
    # TC: O(amount*N)
    # SC: O(amount*N)
    #
    # where N is number of different coins, because we need only O(1) to update each cell.
    #
    # In the code I use index i+1 instead of i, because we start from 1st column, not 0th.
    #
    # Update Space complexity can be reduced to O(amount), because for every j we look at most one row back.
    # Solution for reduced space complexity => changeUsingDP_KnapSack_1D_Array_Solution
    #
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort on basis of width and then find LIS on basis of height

        ln = len(envelopes)
        if ln < 2:
            return ln

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # If width is same then height should be in descending order as same width
        # envelopes can't fit into each other
        # [3,3] and [3,4] - should be in order [3,4] and [3,3]
        # so that during LIS on height we won't pick both

        dp = [envelopes[0][1]]

        for i in range(1, ln):
            w, h = envelopes[i]
            # Find upper bound for h in dp
            s, e = 0, len(dp) - 1
            idx = -1
            while s <= e:
                mid = s + (e - s) // 2
                if dp[mid] == h:
                    idx = mid
                    break
                if dp[mid] < h:
                    if mid == e:
                        dp.append(h)
                        break
                    if dp[mid + 1] > h:
                        idx = mid + 1
                        break
                    s += 1
                else:
                    if mid == 0:
                        idx = mid
                        break
                    e -= 1
            if idx > -1:
                dp[idx] = h

        return len(dp)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxEnvelopes(self) -> None:
        sol = Solution()
        boxes = [[5, 4], [6, 4], [6, 7], [2, 3]]
        self.assertEqual(3, sol.maxEnvelopes(boxes))


# main
if __name__ == "__main__":
    unittest.main()
