# Google | OA 2020 | Min Cost to Keep Employees
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Twitter | OA 2019 | Social Network
#
# Problem Statement:
# **************************************************************************
# A Company needs to hire employees and to hire an employee, the company has to give a fixed fee to the employment agency,
# also a fixed amount of severance pay is given to the employee when they are terminated - in addition to the monthly salary
# they receive. You are given the following values hiring cost, salary of the employee, severance fee, number of months n,
# and an integer array which contains minimum employees required by the company for each month for n number of months.
# Calculate and print the minimum cost to the company which is require to keep minimum employees each month for n months.
#
# Note:
# **************************************************************************
# There are no employees on hand before the first month.
#
# Input Format:
# **************************************************************************
# Input contains 5 lines
#   * First 4 lines contain an integer which represents hiring cost, salary, severance fee and number of months respectively.
#   * Fifth line contains array of n integers which represents minimum number of employees required by the company each month
#     for n months.
#
# Output Format:
# **************************************************************************
# A single integer, i.e., the minimum cost required by the company.
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/397339/ (Google | OA 2020 | Min Cost to Keep Employees)
#
# **************************************************************************
# References:
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution:
    def minCost(self, cost: int, salary: int, severance: int, nums: List[int]) -> int:
        dp = {0: 0}
        for req in nums:
            tmp = collections.defaultdict(lambda: float("inf"))
            for key in dp:
                if key >= req:
                    for i in range(req, key + 1):
                        tmp[i] = min(
                            tmp[i], dp[key] + i * salary + (key - i) * severance
                        )
                else:
                    tmp[req] = min(
                        tmp[req], dp[key] + req * salary + (req - key) * cost
                    )
            dp = tmp
        return min(dp.values())


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minimumCostToKeepEmployees(self) -> None:
        sol = Solution()
        self.assertEqual(
            4312, sol.minCost(2, 100, 10, [3, 4, 5, 3, 2, 4, 5, 2, 4, 5, 3, 2])
        )
        self.assertEqual(307, sol.minCost(5, 6, 7, [14, 10, 11]))


# main
if __name__ == "__main__":
    unittest.main()
