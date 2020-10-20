#
# Time  :
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Geek collects the balls
#
# Description:
#
# There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
# The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help Geek to collect the maximum number of balls.
#
# Input:
# The first line of input contains T denoting the number of test cases. The first line of each test case contains two integers N and M, denoting the number of buckets on road1 and road2 respectively. 2nd line of each test case contains N integers, number of balls in buckets on the first road. 3rd line of each test case contains M integers, number of balls in buckets on the second road.
#
# Output:
# For each test case output a single line containing the maximum possible balls that Geek can collect.
#
# Constraints:
# 1<= T <= 1000
# 1<= N <= 10^3
# 1<= M <=10^3
# 0<= A[i],B[i]<=10^6
#
# Example:
# Input:
# 1
# 5 5
# 1 4 5 6 8
# 2 3 4 6 9
#
# Output:
# 29
#
# Explanation:
#
# The path with maximum sum is (2,3,4)[5,6](9). Integers in [] are the buckets of first road and in () are the buckets of second road. So, max balls geek can collect is 29.
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/geek-collects-the-balls/0 (GeeksForGeeks - Geek collects the balls)
#
# **************************************************************************
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
    def findMaximumNumberOfBallsCollected(self, N: int, M: int, first: List[int], second: List[int]) -> int:
        intersection = [[0, 0]]
        f = 0
        s = 0
        while (True):
            if f >= M or s >= N:
                break
            if first[f] > second[s]:
                s += 1
            elif first[f] < second[s]:
                f += 1
            elif first[f] == second[s]:
                try:
                    if first[f + 1] == first[f]:
                        f += 1
                        continue
                    if second[s + 1] == second[s]:
                        s += 1
                        continue
                except:
                    pass
                intersection.append([f, s])
                f += 1
                s += 1
        count = 0
        f = 0
        s = 0

        def segcount(intsc0, intsc1=None):
            fcount = 0
            scount = 0
            if intsc1 == None:
                for i in range(intsc0[0], M):
                    fcount += first[i]
                for i in range(intsc0[1], N):
                    scount += second[i]
                return [fcount, scount]
            for i in range(intsc0[0], intsc1[0]):
                fcount += first[i]
            for i in range(intsc0[1], intsc1[1]):
                scount += second[i]
            return [fcount, scount]

        for i in range(0, len(intersection)):
            if i + 1 != len(intersection):
                result = segcount(intersection[i], intersection[i + 1])
            else:
                result = segcount(intersection[i])
            count += max(result[0], result[1])
        # print(count)
        return count

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findMaximumNumberOfBallsCollected(self) -> None:
        sol = Solution()
        first = [1,4,5,6,8]
        second = [2,3,4,6,9]
        self.assertEqual(29, sol.findMaximumNumberOfBallsCollected(len(first), len(second), first, second))


# main
if __name__ == "__main__":
    unittest.main()
