#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Google | Phone | Box Stacking Problem
#
# Description:
#
# Given a collection of boxes. Return the max number of boxes that you can russian doll.
# Each box has (w, h, l).
#
# Example:
#
# Input:
#
# [
# 	[3,9,9],
# 	[1,4,10],
# 	[5,10,11],
# 	[3,9,3],
# 	[1,5,3]
# 	[7, 12, 1]
# ]
#
# Output:
#
# 3
#
# Explanation: [1,5,3] fits in [3,9,9] which fits in [5,10,11]
# All the dimensions must be smaller to fit into a larger box -- [1,5,3] does not fit into [3,9,3]
#
# This seems to be a variation of the known [Box Stacking Problem](https://practice.geeksforgeeks.org/problems/box-stacking/1).
# May be similar to [Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
# question but harder with the extra dimension.
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/540814/google-phone-box-stacking-problem (Google | Phone | Box Stacking Problem)
# **************************************************************************
#
# Reference
# **************************************************************************
# https://github.com/OpenGenus/cosmos/blob/bb07b7beb3fb2e367e83b1c81bfc08a76d50a16b/code/dynamic_programming/src/box_stacking/box_stacking.py
#
from typing import List

from collections import namedtuple

import unittest

dimension = namedtuple("Dimension", "height length width")


class Solution(object):
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort on basis of width and height and then find LIS on basis of length
        ln = len(envelopes)
        if ln < 2:
            return ln

        # If width is same then height should be in descending order as same width
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # If height is same then length should be in descending order as same height
        envelopes.sort(key=lambda x: (x[1], -x[2]))
        # envelopes can't fit into each other
        # [3,3,3] and [3,3,4] - should be in order [3,3,4] and [3,3,3]
        # so that during LIS on length we won't pick both

        dp = [envelopes[0][1]]

        for i in range(1, ln):
            w, h, l = envelopes[i]
            # Find upper bound for l in dp
            s, e = 0, len(dp) - 1
            idx = -1
            while s <= e:
                mid = s + (e - s) // 2
                if dp[mid] == l:
                    idx = mid
                    break
                if dp[mid] < l:
                    if mid == e:
                        dp.append(l)
                        break
                    if dp[mid + 1] > l:
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
        boxes = [[3, 9, 9], [1, 4, 10], [5, 10, 11], [3, 9, 3], [1, 5, 3], [7, 12, 1]]
        self.assertEqual(3, sol.maxEnvelopes(boxes))

        boxes = [[3, 9, 9], [1, 4, 10], [5, 10, 11], [3, 9, 3], [1, 5, 3], [10, 20, 22]]
        self.assertEqual(4, sol.maxEnvelopes(boxes))

        boxes = [
            [3, 9, 9],
            [5, 10, 11],
            [10, 20, 22],
            [3, 9, 3],
            [1, 5, 3],
            [6, 11, 13],
        ]
        self.assertEqual(5, sol.maxEnvelopes(boxes))


# main
if __name__ == "__main__":
    unittest.main()
