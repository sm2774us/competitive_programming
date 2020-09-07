#
# Time : O(N); Space: O(N)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Description:
#
# The cost of stock on each day is given in an array A[] of size N.
# Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
#
# Example 1:
#
# Input: [100, 180, 260, 310, 40, 535, 695]
# Output: [ (0, 3), (4, 6) ]
# Explanation: We can buy stock on day 0, and sell it on 3rd day, which will give us maximum profit.
#
# Example 2:
# Input: [100, 180, 260, 310, 40, 535, 695]
# Output: [ (1, 4), (5, 9) ]
#
# **************************************************************************
# Source:
#   https://practice.geeksforgeeks.org/problems/stock-buy-and-sell/0 (GeeksForGeeks - Stock buy and sell)
# Solution Hint:
#   https://www.geeksforgeeks.org/stock-buy-sell/
from typing import List
from itertools import accumulate

import unittest

class Solution:
    # Reduce to one-line using accumulate
    def stockBuySell(self, price: List[int]) -> int:
        n = len(price)
        # Prices must be given for at least two days
        if (n == 1):
            return

        result = []
        # Traverse through given price array
        i = 0
        while (i < (n - 1)):

            # Find Local Minima
            # Note that the limit is (n-2) as we are
            # comparing present element to the next element
            while ((i < (n - 1)) and
                   (price[i + 1] <= price[i])):
                i += 1

            # If we reached the end, break
            # as no further solution possible
            if (i == n - 1):
                break

            # Store the index of minima
            buy = i
            i += 1

            # Find Local Maxima
            # Note that the limit is (n-1) as we are
            # comparing to previous element
            while ((i < n) and (price[i] >= price[i - 1])):
                i += 1

            # Store the index of maxima
            sell = i - 1

            result.append((buy, sell))
            #print("Buy on day: ", buy, "\t",
            #      "Sell on day: ", sell)
        return result

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_stockBuySell(self) -> None:
        sol1 = [ (0,3), (4,6) ]
        sol2 = []
        sol3 = [ (1,4), (5,9) ]
        s = Solution()
        for price, solution in (
                [[100,180,260,310,40,535,695], sol1 ],
                [[100,50,30,20], sol2 ],
                [[23,13,25,29,33,19,34,45,65,67], sol3 ]
        ):
            self.assertEqual(solution, s.stockBuySell(price),
                             """Should the days on which you buy and sell the stock so that 
                             in between those days your profit is maximum""")


if __name__ == '__main__':
    unittest.main()