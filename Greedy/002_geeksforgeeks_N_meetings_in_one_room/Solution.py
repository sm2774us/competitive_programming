#
# Time : O(n log n)
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - N meetings in one room
#
# Description:
#
# There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
#
# What is the maximum number of meetings that can be accommodated in the meeting room?
#
# Input:
# The first line of input consists number of the test cases. The description of T test cases is as follows:
# The first line consists of the size of the array, second line has the array containing the starting time of all the meetings each separated by a space, i.e., S [ i ]. And the third line has the array containing the finishing time of all the meetings each separated by a space, i.e., F [ i ].
#
# Output:
# In each separate line print the order in which the meetings take place separated by a space.
#
# Constraints:
# 1 ≤ T ≤ 70
# 1 ≤ N ≤ 100
# 1 ≤ S[ i ], F[ i ] ≤ 100000
#
# Example:
# Input:
# 2
# 6
# 1 3 0 5 8 5
# 2 4 6 7 9 9
# 8
# 75250 50074 43659 8931 11273 27545 50879 77924
# 112960 114515 81825 93424 54316 35533 73383 160252
#
# Output:
# 1 2 4 5
# 6 7 1
#
# Explanation:
# Testcase 1: Four meetings can held with given start and end timings.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room/0 (GeeksForGeeks - N meetings in one room)
#
# **************************************************************************
#
from typing import List

import unittest

class Solution:
    def getMaxMeetingsInOneRoom(self, a: List[int], b: List[int]) -> List[int]:
        n = len(a)
        ans = []
        for i in range(n):
            ans.append([a[i], b[i], i + 1])
        ans.sort(key=lambda x: x[1])
        max_meetings = [ans[0][2]]
        #print(ans[0][2], end=" ")
        prev = ans[0][1]
        for i in range(1, n):
            if ans[i][0] >= prev:
                max_meetings.append(ans[i][2])
                #print(ans[i][2], end=" ")
                prev = ans[i][1]
        #print()
        return max_meetings

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getMaxMeetingsInOneRoom(self) -> None:
        sol = Solution()
        for a, b, solution in (
            [[1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], [1, 2, 4, 5]],
            [[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924], [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252 ], [6, 7, 1]]
        ):
            self.assertEqual(solution, sol.getMaxMeetingsInOneRoom(a, b))


# main
if __name__ == "__main__":
    # sol = Solution
    # # Driver program to test above function
    # a = [1, 3, 0, 5, 8, 5]
    # b = [2, 4, 6, 7, 9, 9]
    # sol.getMaxMeetingsInOneRoom(a, b)
    ## prints => 1,2,4,5
    unittest.main()
