#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Maximize Toys
#
# Description:
#
# Given an array arr of length N consisting cost of toys. Given an integer K depicting the amount with you. The task is to Maximise the number of different toys you can have with K amount.
#
# Example 1:
#
# Input: N = 7, K = 50
# arr = {1, 12, 5, 111, 200, 1000, 10}
# Output: 4
# Explaination: The costs of the toys are
# 1, 12, 5, 10.
# Example 2:
#
# Input: N = 3, K = 100
# arr = {20, 30, 50}
# Output: 3
# Explaination: We can buy all types of
# toys.
# Your Task:
# You do not need to read input or print anything. Your task is to complete the function toyCount() which takes the value N, K and the array arr and returns the maximum count of toys.
#
# Expected Time Complexity: O(NlogN)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 1 ≤ N ≤ 1000
# 1 ≤ K, arr[i] ≤ 10000
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/maximize-toys0331/1 (GeeksForGeeks - Maximize Toys)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest

# Python 3 Program to maximize the
# number of toys with K amount
class Solution:
    # This functions returns the required
    # number of toys
    def maximum_toys(self, cost: List[int], N: int, K: int) -> int:
        count = 0
        sum = 0

        # sort the cost array
        cost.sort(reverse=False)
        for i in range(0, N, 1):

            # Check if we can buy ith toy or not
            if sum + cost[i] <= K:
                sum = sum + cost[i]
                # Increment the count variable
                count += 1

        return count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maximum_toys(self) -> None:
        sol = Solution()
        for a, k, solution in (
            [[1, 12, 5, 111, 200, 1000, 10], 50, 4],
            [[20, 30, 50], 100, 3],
        ):
            self.assertEqual(solution, sol.maximum_toys(a, len(a), k))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # K = 50
    # cost = [1, 12, 5, 111, 200,
    #         1000, 10, 9, 12, 15]
    # N = len(cost)
    # print(sol.maximum_toys(cost, N, K))
    unittest.main()
