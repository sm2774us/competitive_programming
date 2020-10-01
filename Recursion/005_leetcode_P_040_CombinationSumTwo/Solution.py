#
# Time : O(N); Space: O(1)
# @tag : Recursion
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 40: Combination Sum II
#
# Description:
#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#   * All numbers (including target) will be positive integers.
#   * The solution set must not contain duplicate combinations.
#
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/combination-sum-ii/ (Leetcode - Problem 40 - Combination Sum II)
#         https://practice.geeksforgeeks.org/problems/combination-sum-part-2/0 (GeeksForGeeks - Combination Sum - Part 2)
#
#
from typing import List

import unittest


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.find_all_sum_up_to(candidates, target)

    def find_all_sum_up_to(self, elements: list, target: int) -> list:
        elements.sort()
        res = []
        self.find_all_combinations_sum_up_to(elements, target, res)
        return res

    def find_all_combinations_sum_up_to(
        self,
        elements: list,  # a list of candidates elements, assume repetitions, assume list if sorted.
        targetsum: int,  # The target we want to sum up to.
        solutionsbucket,  # a list of combinations
        choices: list = None,  # A combination of the list of elements.
        startingindex: int = 0,  # which part of the array we are looking at.
    ):

        if targetsum == 0 and choices is not None:
            solutionsbucket.append(choices)
            return

        # For each of the elements in the list beyond index i, we make choices on it.
        for i in range(startingindex, len(elements)):
            # Skip repeated elements:
            if i != startingindex and elements[i] == elements[i - 1]:
                continue

            # Sorted array check if element too big for sum.
            n = elements[i]
            if n > targetsum:
                break

            # make this choice and recur:
            choices = [] if choices is None else choices
            self.find_all_combinations_sum_up_to(
                elements, targetsum - n, solutionsbucket, choices + [n], i + 1
            )
        return


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_combinationSum2(self) -> None:
        sol = Solution()
        for candidates, target, solution in (
            [[10, 1, 2, 7, 6, 1, 5], 8, [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]],
            [[2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]],
        ):
            self.assertEqual(
                sorted(solution),
                sorted(sol.combinationSum2(candidates, target)),
                "Should return all unique combinations in candidates where the candidate numbers sums to target",
            )


if __name__ == "__main__":
    unittest.main()
