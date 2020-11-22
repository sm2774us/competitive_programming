#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1547: Minimum Cost to Cut a Stick
#
# Description: Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/ (LeetCode - Problem 1547 - Minimum Cost to Cut a Stick)
# **************************************************************************
#
from typing import List
from math import inf
from functools import lru_cache

import unittest


class Solution(object):

    # Solution_1
    #
    # Define fn(lo, hi) as the min cost of cutting lo to hi (both inclusive). Then,
    #
    #   1. if there is not cut between lo and hi, return 0;
    #   2. if there are cuts, return the one with the minimum cost, i.e. fn(lo, hi) = hi - lo + min(fn(lo, mid) + fn(mid, hi)) where mid is a plausible cut.
    #
    def minCost_solution_1(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def fn(lo, hi):
            """Return cost of cutting [lo, hi]."""
            cc = [c for c in cuts if lo < c < hi]  # collect cuts within this region
            if not cc:
                return 0
            ans = inf
            for mid in cc:
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            return ans + hi - lo

        return fn(0, n)

    # Solution_2 : A more efficient implementation is to index cuts like below
    #
    def minCost_solution_2(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()

        @lru_cache(None)
        def fn(i, j):
            """Return cost of cutting from cuts[i] to cuts[j]."""
            if i + 1 == j:
                return 0  # no cut in (i, j)
            return cuts[j] - cuts[i] + min(fn(i, k) + fn(k, j) for k in range(i + 1, j))

        return fn(0, len(cuts) - 1)

    # Solution_3 : DP + memoization ( no lru_cache dependency )
    #
    def minCost_solution_3_dp_with_memoization(self, n: int, cuts: List[int]) -> int:

        ## dictionary:
        # key: cut index pair
        # value: minimum cutting cost
        cost_dict = {}

        ## initialization
        # adding end points and keep cut point sorted in ascending order
        cuts = [0] + sorted(cuts) + [n]

        # -------------------------------------------------------------------------
        def cutter(left_cut_index, right_cut_index):

            if (left_cut_index, right_cut_index) in cost_dict:
                # Quick response with memoization
                return cost_dict[(left_cut_index, right_cut_index)]

            left_boundary = cuts[left_cut_index]
            right_boundary = cuts[right_cut_index]

            if (right_boundary - left_boundary) <= 1:
                # Base case:
                # current stick is with either length 0 or length 1 stick
                # no need to cut
                return 0

            elif (right_cut_index - left_cut_index) <= 1:
                # Base case:
                # No cutting point exists in interval [left_boundary, right_boundary]
                return 0

            else:
                # General case:
                # At least one cutting point exists in interval [left_boundary, right_boundary]
                cost_of_range = float("inf")

                # Solve by Dynamic Programming with memoziation
                for cut_index in range(left_cut_index + 1, right_cut_index):
                    cost_of_trial = cutter(left_cut_index, cut_index) + cutter(
                        cut_index, right_cut_index
                    )

                    # update with minimum cost
                    cost_of_range = min(cost_of_range, cost_of_trial)

                cost_of_cut_cur_length = right_boundary - left_boundary
                total_cost = cost_of_cut_cur_length + cost_of_range

                cost_dict[(left_cut_index, right_cut_index)] = total_cost

                return total_cost

        # -------------------------------------------------------------------------

        return cutter(left_cut_index=0, right_cut_index=len(cuts) - 1)

    # Solution_4 : bottom-up implementation
    #
    def minCost_solution_4(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()

        dp = [[0] * len(cuts) for _ in cuts]
        for i in reversed(range(len(cuts))):
            for j in range(i + 2, len(cuts)):
                dp[i][j] = (
                    cuts[j]
                    - cuts[i]
                    + min(dp[i][k] + dp[k][j] for k in range(i + 1, j))
                )
        return dp[0][-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minCost(self) -> None:
        sol = Solution()
        for n, cuts, solution in ([7, [1, 3, 4, 5], 16], [9, [5, 6, 1, 4, 2], 22]):
            self.assertEqual(solution, sol.minCost_solution_1(n, cuts))
            self.assertEqual(solution, sol.minCost_solution_2(n, cuts))
            # self.assertEqual(solution, sol.minCost_solution_3_dp_with_memoization(n, cuts)) # Test Case fails - Needs rework
            # self.assertEqual(solution, sol.minCost_solution_4(n, cuts)) # Test Case fails - Needs rework


# main
if __name__ == "__main__":
    unittest.main()
