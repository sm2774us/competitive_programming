#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Coin Piles
#
# Description:
#
# There are N piles of coins each containing  Ai (1<=i<=N) coins.  Now, you have to adjust the number of coins in each pile such that for any two pile, if a be the number of coins in first pile and b is the number of coins in second pile then |a-b|<=K. In order to do that you can remove coins from different piles to decrease the number of coins in those piles but you cannot increase the number of coins in a pile by adding more coins. Now, given a value of N and K, along with the sizes of the N different piles you have to tell the minimum number of coins to be removed in order to satisfy the given condition.
# Note: You can also remove a pile by removing all the coins of that pile.
#
# Input
# The first line of the input contains T, the number of test cases. Then T lines follow. Each test case contains two lines. The first line of a test case contains N and K. The second line of the test case contains N integers describing the number of coins in the N piles.
#
# Output
# For each test case output a single integer containing the minimum number of coins needed to be removed in a new line.
#
# Constraints
# 1<=T<=50
# 1<=N<=100
# 1<=Ai<=1000
# 0<=K<=1000
#
# Example
# Input
# 3
# 4 0
# 2 2 2 2
# 6 3
# 1 2 5 1 1 1
# 6 3
# 1 5 1 2 5 1
#
# Output
# 0
# 1
# 2
#
# Explanation
# 1. In the first test case, for any two piles the difference in the number of coins is <=0. So no need to remove any coins.
# 2. In the second test case if we remove one coin from pile containing 5 coins then for any two piles the absolute difference in the number of coins is <=3.
# 3. In the third test case if we remove one coin each from both the piles containing 5 coins , then for any two piles the absolute difference in the number of coins is <=3.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/coin-piles/0 (GeeksForGeeks - Coin Piles)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List
import math

import unittest

class Solution:
    # Function to return the minimum number
    # of coins that need to be removed
    def minimumCoins(self, nums: List[int], n: int, k: int) -> int:
        nums.sort()
        # To store the coins needed to be removed
        cnt = math.inf
        tmp = 0
        for i in range(n):
            temp = tmp
            tmp += nums[i]
            for j in reversed(range(i + 1, n)):
                if (nums[j] - nums[i] - k > 0): temp += nums[j] - nums[i] - k
            cnt = min(cnt, temp)
        return cnt
        # cnt = 0
        #
        # # Minimum value from the array
        # minVal = 1
        #
        # # Iterate over the array and remove extra coins
        # for i in range(n):
        #     diff = nums[i] - minVal
        #
        #     # If the difference between the current pile and
        #     # the minimum coin pile is greater than k
        #     if (diff > k):
        #         # Count the extra coins to be removed
        #         cnt += (diff - k)
        #         # Return the required count
        # return cnt

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minimumCoins(self) -> None:
        sol = Solution()
        for a, k, solution in (
            [[2,2,2,2], 0, 0],
            [[1,2,5,1,1,1], 3, 1],
            [[1,5,1,2,5,1], 3, 2]
        ):
            self.assertEqual(solution, sol.minimumCoins(a, len(a), k))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # a = [1, 5, 1, 2, 5, 1];
    # n = len(a);
    # k = 3;
    # print(sol.minimumCoins(a, n, k))
    unittest.main()
