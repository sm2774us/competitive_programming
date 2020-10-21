#
# Time  : O(N log N)
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Shop in Candy Store
#
# Description:
#
# In a candy store there are N different types of candies available  and the prices of all the N different types of candies are provided to you.
# You are now provided with an attractive offer.
# You can buy a single candy from the store and get atmost K other candies ( all are different types ) for free.
# Now you have to answer two questions. Firstly, you have to tell what is the minimum amount of money you have to spend to buy all the N different candies. Secondly, you have to tell what is the maximum amount of money you have to spend to buy all the N different candies.
# In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.
#
#
# Input
# The first line of the input contains T the number of test cases. Each test case consists of two lines. The first line of each test case contains the values of N and K as described above.  Then in the next line N integers follow denoting the price of each of the N different candies.
#
#
# Output
# For each test case output a single line containing 2 space separated integers , the first denoting the minimum amount of money required to be spent and the second denoting the maximum amount of money to be spent.
# Remember to output the answer of each test case in a new line.
#
# Constraints
# 1 <= T <= 50
# 1 <= N <= 1000
#  0 <= K <= N-1
# 1 <= Ai <= 100
#
#
# Expected Time Complexity : O(nlogn)
#
# Example:
# Input
#  1
#  4  2
#  3 2 1 4
#
# Output
#  3 7
#
# Explanation
# As according to the offer if you but one candy you can take atmost two more for free.
# So in the first case you buy the candy which costs 1 and take candies worth 3 and 4 for free, also you buy candy worth 2 as well.
# So min cost = 1+2 =3.
# In the second case I buy the candy which costs 4 and take candies worth 1 and 2 for free, also I  buy candy worth 3 as well.
# So max cost = 3+4 =7.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/shop-in-candy-store/0 (GeeksForGeeks - Shop in Candy Store)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest

# Python implementation
# to find the minimum
# and maximum amount
class Solution:
    # Function to find
    # the minimum amount
    # to buy all candies
    def findMinimum(self, arr: List[int], n: int, k: int) -> int:
        res = 0
        i = 0
        while n:
            # Buy current candy
            res += arr[i]

            # And take k
            # candies for free
            # from the last
            n = n - k
            i += 1
        return res

        return result

    # Function to find
    # the maximum amount
    # to buy all candies
    def findMaximum(self, arr: List[int], n: int, k: int) -> int:
        res = 0
        index = 0
        i = n - 1
        while i >= index:
            # Buy candy with
            # maximum amount
            res += arr[i]

            # And get k candies
            # for free from
            # the starting
            index += k
            i -= 1

        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMinimumAndMaximum(self) -> None:
        sol = Solution()
        arr = [3, 2, 1, 4]
        k = 2
        arr.sort()
        self.assertEqual(3, sol.findMinimum(arr, len(arr), k))
        self.assertEqual(7, sol.findMaximum(arr, len(arr), k))


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # arr = [3, 2, 1, 4]
    # k = 2
    # arr.sort()
    # print("{} {}".format(sol.findMinimum(arr, len(arr), k),
    #                      sol.findMaximum(arr, len(arr), k)))
    unittest.main()
