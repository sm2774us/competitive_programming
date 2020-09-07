#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given two arrays X and Y of positive integers, find number of pairs
# such that xy > yx (raised to power of) where x is an element
# from X and y is an element from Y.
#
# Example:
#
# Given input            => [1, 2, 3, 4]
#       output should be => [4, 1, 3, 2]
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ M, N ≤ 105
# 1 ≤ X[i], Y[i] ≤ 103
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
# Source: https://practice.geeksforgeeks.org/problems/number-of-pairs/0/ ( Number of pairs )
#
# Solution Hint: https://github.com/Aditya-Gupta1/Practise-Questions
#
from typing import List
import bisect

import unittest

class Solution:
    def count(self, x: int, Y: List[int], n: int, counts: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return counts[0]
        idx = bisect.bisect_right(Y, x)
        ans = n - idx
        ans += (counts[0] + counts[1])
        if x == 2:
            ans -= (counts[3] + counts[4])
        if x == 3:
            ans += counts[2]
        return ans

    def countPairs(self, X: List[int], Y: List[int], m: int, n: int) -> int:
        counts = [0] * 5
        for y in Y:
            if y < 5:
                counts[y] += 1
        Y.sort()
        totalPairs = 0
        for x in X:
            totalPairs += self.count(x, Y, n, counts)
        return totalPairs

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countPairs(self) -> None:
        s = Solution()
        for X, Y, m, n, solution in (
                [[2,1,6], [1,5], 3, 2, 3],
                [[1,4,3], [1,2], 3, 2, 3]
        ):
            self.assertEqual(solution, s.countPairs(X, Y, m, n), "Should return the number of pairs such the x^y > y^x")

if __name__ == '__main__':
    unittest.main()