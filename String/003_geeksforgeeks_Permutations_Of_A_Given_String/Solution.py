#
# Time : O(N^3*N!); Space: O(N!) [ Bounded by # of permutations, which is O(N!) ]
# @tag : String, Iterative, Backtracking, DFS ( Depth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Description:
#
# Given a string S. The task is to print all permutations of a given string.
#
# Example 1:
#
# Input: ABC
# Output: ABC ACB BAC BCA CAB CBA
#
# Example 2:
#
# Input: ABSG
# Output: ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
#
# Example 3:
#
# Input: 123
# Output: 123 132 213 231 312 321
#
# **************************************************************************
# Source: https://leetcode.com/problems/permutations/ (Leetcode - Problem 46 - Permutations)
#         https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0 (GeeksForGeeks - Permutations of a given string)
#
# Solution Explanation
# **************************************************************************
# 1) Iterative Approach
# the basic idea is, to permute n numbers, we can add the nth number into the resulting List[List[int]]
# from the n-1 numbers, in every possible position.
#
# For example, if the input num[] is [1,2,3]: First, add 1 into the initial List[List[int]]
# (let's call it "perms").
#
# Then, 2 can be added in front or after 1.
# So we have to copy the List in answer (it's just [1]), add 2 in position 0 of [1], then copy the original [1] again,
# and add 2 in position 1. Now we have an answer of [[2,1],[1,2]]. There are 2 lists in the current answer.
#
# Then we have to add 3. first copy [2,1] and [1,2], add 3 in position 0; then copy [2,1] and [1,2], and
# add 3 into position 1, then do the same thing for position 3.
# Finally we have 2*3=6 lists in answer, which is what we want.
#
# Complexity Analysis:
#
# Time Complexity: O(N^3*N!) ; Space: O(N!) = Bounded by # of permutations, which is O(N!)
#
# For every step i, where i ranges from 1 to n(both including), ans is going to be of length i! where every element
# is of length i. Hence, the lowermost for loop "for (List l : ans)" will take i! time.
# But we also make complex operations inside the loop: constructing a new arraylist from an arraylist of length i
# takes i time.
# Adding an element to some index in between of a list of length i takes i time, and adding that list of length i
# to the new_ans list takes i time. Hence the inner loop takes a total of ii! time. Note that we do this i many times,
# i.e., once per every possible position, hence the lower two loops take i^2i! time. We then realize that
# we repeat the procedure for i=1 to n. We can either try to do the summation sum i^2i! from i = 1 to n, or,
# we can simply say that in the worst case, this happens n^2n! times, and we do this n times, which would be O(n^3*n!)
#
# **************************************************************************
# 2) DFS Approach
# Visualization:
# dfs(strs = [1, 2, 3] , path = [] , result = [] )
# |____ dfs(strs = [2, 3] , path = [1] , result = [] )
# |      |___dfs(strs = [3] , path = [1, 2] , result = [] )
# |      |    |___dfs(strs = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
# |      |___dfs(strs = [2] , path = [1, 3] , result = [[1, 2, 3]] )
# |           |___dfs(strs = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
# |____ dfs(strs = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |___dfs(strs = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
# |      |    |___dfs(strs = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
# |      |___dfs(strs = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
# |           |___dfs(strs = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
# |____ dfs(strs = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |___dfs(strs = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
#        |    |___dfs(strs = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
#        |___dfs(strs = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
#             |___dfs(strs = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
#
# **************************************************************************
# 3) Backtracking Approach
#
# Backtracking Definition:
# **************************************************************************
# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems,
# notably constraint satisfaction problems, that incrementally builds candidates to the solutions,
# and abandons a candidate ("backtracks") as soon as it determines that the candidate
# cannot possibly be completed to a valid solution.
# **************************************************************************
#
# First we have the main driver permute function
# • We create a visited variable
# • A result variable
# • And call the recursive backtracking function (arguments - results, visited, empty subset and given collection)
# • Then return the result
#
# Then the backtracking recursive function
# • Checks if the length of our current running subset is equal to the length of the collection given
# ○ If yes we append our results variable with the subset (e.g. [1,3,2])
# • Then we iterate over the range of the length of the collection
# ○ If the current number of the collection[i] is not already in our visited set:
# § Add it to visited
# § call the recursive function, the same as before but this time with the subset + the current number we are iterating over in the collection, such that each iteration has an increasing amount of digits in the subset until we reach the same length as the original collection - where it will be added to our results list
# We then remove the current number from visited in order to allow for the creation of new permutations
#

from typing import List
from typing import Set

import unittest


class Solution:
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    # def permuteUsingIterativeApproach(self, strs: List[str]) -> List[List[str]]:
    #     perms = [[]]
    #     for s in strs:
    #         new_perms = []
    #         for perm in perms:
    #             for i in range(len(perm) + 1):
    #                 new_perms.append(perm[:i] + [s] + perm[i:])  ###insert n
    #         perms = new_perms
    #     return perms
    def permuteUsingIterativeApproach(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)

        # Create an empty permutation as the base
        current_perms = [[]]

        # Fill in permutations of length 1, of length 2, etc.
        for i in range(0, N):

            # Create the next permutations
            next_perms = []
            for perm in current_perms:
                for s in strs:
                    if s not in perm:
                        next_perms.append(perm[:] + [s])

            current_perms = next_perms

        return current_perms

    def dfs(self, strs: List[str], path: List[str], res: List[List[str]]) -> None:
        if not strs:
            res.append(path)
            # return # backtracking
        for i in range(len(strs)):
            self.dfs(strs[:i] + strs[i + 1 :], path + [strs[i]], res)

    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    def permuteUsingDFS(self, strs: List[str]) -> List[List[str]]:
        res = []
        self.dfs(strs, [], res)
        return res

    def backtracking(
        self,
        visited: Set[str],
        subset: List[str],
        strs: List[str],
        res: List[List[str]],
    ) -> None:
        if len(subset) == len(strs):
            res.append(subset)
        for i in range(len(strs)):
            if i not in visited:
                visited.add(i)
                self.backtracking(visited, subset + [strs[i]], strs, res)
                visited.remove(i)

    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    def permuteUsingBacktracking(self, strs: List[str]) -> List[List[str]]:
        visited = set()
        res = []
        self.backtracking(visited, [], strs, res)
        return res


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_permute(self) -> None:
        self.maxDiff = None
        s = Solution()
        for strs, solution in (
            [
                ["A", "B", "C"],
                [
                    ["A", "B", "C"],
                    ["A", "C", "B"],
                    ["B", "A", "C"],
                    ["B", "C", "A"],
                    ["C", "A", "B"],
                    ["C", "B", "A"],
                ],
            ],
            [
                ["A", "B", "S", "G"],
                [
                    ["A", "B", "S", "G"],
                    ["A", "B", "G", "S"],
                    ["A", "S", "B", "G"],
                    ["A", "S", "G", "B"],
                    ["A", "G", "B", "S"],
                    ["A", "G", "S", "B"],
                    ["B", "A", "S", "G"],
                    ["B", "A", "G", "S"],
                    ["B", "S", "A", "G"],
                    ["B", "S", "G", "A"],
                    ["B", "G", "A", "S"],
                    ["B", "G", "S", "A"],
                    ["S", "A", "B", "G"],
                    ["S", "A", "G", "B"],
                    ["S", "B", "A", "G"],
                    ["S", "B", "G", "A"],
                    ["S", "G", "A", "B"],
                    ["S", "G", "B", "A"],
                    ["G", "A", "B", "S"],
                    ["G", "A", "S", "B"],
                    ["G", "B", "A", "S"],
                    ["G", "B", "S", "A"],
                    ["G", "S", "A", "B"],
                    ["G", "S", "B", "A"],
                ],
            ],
            [
                ["1", "2", "3"],
                [
                    ["1", "2", "3"],
                    ["1", "3", "2"],
                    ["2", "1", "3"],
                    ["2", "3", "1"],
                    ["3", "1", "2"],
                    ["3", "2", "1"],
                ],
            ],
        ):
            self.assertEqual(
                solution,
                s.permuteUsingIterativeApproach(strs),
                "Should return all possible permutations",
            )
            self.assertEqual(
                solution,
                s.permuteUsingDFS(strs),
                "Should return all possible permutations",
            )
            self.assertEqual(
                solution,
                s.permuteUsingBacktracking(strs),
                "Should return all possible permutations",
            )


if __name__ == "__main__":
    unittest.main()
