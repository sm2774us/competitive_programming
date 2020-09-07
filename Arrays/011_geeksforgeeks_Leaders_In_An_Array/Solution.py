#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given an array of positive integers. Your task is to find the leaders in the array.
# Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader.
#
# Input:
# An array.
#
# Output:
# Output an array with the leaders.
#
# Example:
#
# Given input            => [16,17,4,3,5,2]
#       output should be => [17,5,2]
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0 ( Leaders in an array )
#
# Solution Hint: https://github.com/jainaman224/Algo_Ds_Notes/blob/master/Leaders_Of_Array/Leaders_Of_Array.py
#
from typing import List

import unittest

class Solution:
    def find_leaders(self, nums: List[int]) -> List[int]:
        size = len(nums)
        # Last element is always a leader.
        # Assigning n to hold the last value
        n = nums[len(nums) - 1]
        # List (or Array) to store the leaders
        result = [n]
        # Iterating backwards
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= n:
                n = nums[i]
                result.append(n)

        result.reverse()
        #print(result)
        return result

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_rearrange(self) -> None:
        s = Solution()
        for nums, solution in (
                [[16,17,4,3,5,2], [17,5,2]],
                [[1,2,3,4,0], [4,0]],
                [[7,4,5,7,3], [7,7,3]],
                [[13,4,12,1,5], [13,12,5]]
        ):
            self.assertEqual(solution, s.find_leaders(nums), "Should return the array with the leaders")


if __name__ == '__main__':
    unittest.main()