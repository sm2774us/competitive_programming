#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 45: Jump Game II
#
# Description:
#
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#   * 1 <= nums.length <= 3 * 104
#   * 0 <= nums[i] <= 105
#
# **************************************************************************
# Source: https://leetcode.com/problems/jump-game-ii/ (LeetCode - Problem 45 - Jump Game II)
#         https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0 (GeeksForGeeks - Minimum number of jumps)
# **************************************************************************
#
from typing import List
import collections

import unittest


class Solution(object):

    # Dynamic Programming based Solution
    def jump(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## Similar Problems ##
        ## 1024. Video Stiching
        ## 1326. Minimum Number Of Taps To Open To Water A Garden
        """
            ## LOGIC ##
            1. Initally I start with 0 steps and maximum reachable distance is 0.
            2. At an index if I take jump. What is the maximum distance reachable ? ( i.e our jumps will be = curr_steps + 1 AND I can reach till index+number position  )
            3. steps_maxReach ({ steps : maxReachableIndex }) will store what is the maximum dist reachable with steps 1, steps 2, steps 3 ... so on..
            4. so when I'm at i = 1, my curr_steps, curr_max_reachable_dist will be still 0. but I have already computed, what is the maximum distance reachable for steps = 1 (in hashmap).
                I enter if cond, I increment the steps count to steps = 1 and get the value of maxReachDist from hashmap, update the variables. Also I will update hashmap with # point 2

                EXAMPLE : [2, 3, 1, 1, 4]
                index  current steps  current max Reacheable       dictionary
                    0       0               0                        {1: 2})
                    1       1               2                        {1: 2, 2: 4})
                    2       1               2                        {1: 2, 2: 4})
                    3       2               4                        {1: 2, 2: 4, 3: 4})
                    4       2               4                        {1: 2, 2: 4, 3: 8})

            5. MEMORY OPTIMIZATION : Actually we donot need steps = 0 details, when we are already at steps = 1. so we delete them.
        """
        #
        curr_max_reachable_dist = 0
        curr_steps = 0
        steps_maxReach = collections.defaultdict(int)
        for index, num in enumerate(nums):
            if index > curr_max_reachable_dist:
                # I'm not supposed to be here, coz, max dist reachable is less than current Index.
                # I can only be at this index if and only if I took jump before. so increment steps and update variables.
                curr_steps += 1
                curr_max_reachable_dist = steps_maxReach[curr_steps]
            steps_maxReach[curr_steps + 1] = max(
                steps_maxReach[curr_steps + 1], index + num
            )  # 2
            # print(index, curr_steps, curr_max_reachable_dist, steps_maxReach)
            if curr_steps - 1 in steps_maxReach:
                del steps_maxReach[curr_steps - 1]  # 5
        return curr_steps

    # Solution using Two Pointers Approach
    #
    # Algorithm:
    # Maintain two pointers curr and next which point to the end of current and next chunks.
    # We scan through the array using index i. When i is beyond curr, update curr to be next and increment jump.
    # At each point, update next to i + nums[i] if it is larger.
    #
    # Analysis:
    # Time complexity O(N)
    # Space complexity O(1)
    #
    def jumpUsingTwoPointers(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        curr = next = jump = 0
        for i in range(len(nums)):
            if i > curr:
                curr = next
                jump += 1
            next = max(next, i + nums[i])
        return jump


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_jump(self) -> None:
        sol = Solution()
        for nums, solution in (
            [
                [2, 3, 1, 1, 4],
                2,
            ],  # Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index
            [[2, 3, 0, 1, 4], 2],
            [[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 3],
            [[1, 4, 3, 2, 6, 7], 2],
        ):
            self.assertEqual(solution, sol.jump(nums))
            self.assertEqual(solution, sol.jumpUsingTwoPointers(nums))


# main
if __name__ == "__main__":
    unittest.main()
