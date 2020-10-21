#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Page Faults in LRU
#
# Description:
#
# In operating systems that use paging for memory management, page replacement algorithm are needed to decide
# which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present
# in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page.
# Given a sequence of pages and memory capacity, your task is to find the number of page faults
# using Least Recently Used (LRU) Algorithm.
#
# Input:
#   * The first line of input contains an integer T denoting the number of test cases.
#   * Each test case contains n number of pages and next line contains space seaprated sequence of pages.
#   * The following line consist of the capacity of the memory.
#
# Note: Pages are referred in the order left to right from the array (i.e index 0 page is referred first
#       then index 1 and so on). Memory is empty at the start.
#
# Output:
# Output the number of page faults.
#
# Constraints:
# 1<=T<=100
# 1<=n<=1000
# 4<=capacity<=100
#
# Example:
# Input:
# 2
# 9
# 5 0 1 3 2 4 1 0 5
# 4
# 8
# 3 1 0 2 5 4 1 2
# 4
#
# Output:
# 8
# 7
#
# Explanation:
# Testcase 1:
# memory allocated with 4 pages 5, 0, 1, 3: page fault = 4
# page number 2 is required, replaces LRU 5: page fault = 4+1 = 5
# page number 4 is required, replaces LRU 0: page fault = 5 + 1 = 6
# page number 1 is required which is already present: page fault = 6 + 0 = 6
# page number 0 is required which replaces LRU 1: page fault = 6 + 1 = 7
# page number 5 is required which replaces LRU 3: page fault = 7 + 1  =8.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/page-faults-in-lru/0 (GeeksForGeeks - Page Faults in LRU)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest


class Solution:
    # This functions returns the required
    # number of toys
    def findPageFaultsInLRU(self, processList: List[int], N: int, capacity: int) -> int:
        # List of current pages in Main Memory
        s = []

        pageFaults = 0
        # pageHits = 0

        for i in processList:

            # If i is not present in currentPages list
            if i not in s:

                # Check if the list can hold equal pages
                if len(s) == capacity:
                    s.remove(s[0])
                    s.append(i)

                else:
                    s.append(i)

                # Increment Page faults
                pageFaults += 1

            # If page is already there in
            # currentPages i.e in Main
            else:

                # Remove previous index of current page
                s.remove(i)

                # Now append it, at last index
                s.append(i)

        # print(f"{pageFaults}")
        return pageFaults


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findPageFaultsInLRU(self) -> None:
        sol = Solution()
        for processList, capacity, solution in (
            [[5, 0, 1, 3, 2, 4, 1, 0, 5], 4, 8],
            [[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2], 4, 6],
            [[3, 1, 0, 2, 5, 4, 1, 2], 4, 7],
        ):
            self.assertEqual(
                solution,
                sol.findPageFaultsInLRU(processList, len(processList), capacity),
            )


# main
if __name__ == "__main__":
    # # Driver code
    # sol = Solution()
    # capacity = 4
    # processList = [7, 0, 1, 2, 0, 3, 0,
    #                4, 2, 3, 0, 3, 2]
    # print(sol.findPageFaultsInLRU(processList, len(processList), capacity))
    unittest.main()
