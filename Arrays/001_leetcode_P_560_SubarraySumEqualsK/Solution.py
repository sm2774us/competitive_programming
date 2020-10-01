#
# Time : O(N); Space: O(N)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Leetcode - Problem 560 - Subarray Sum Equals K
#
# Description:
#
# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# For example,
#  Input:nums = [1,1,1], k = 2
#  Output: 2
#
# Constraints:
#   1) The length of the array is in range [1, 20,000].
#   2) The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
# **************************************************************************
# Source: https://leetcode.com/problems/subarray-sum-equals-k/ (Leetcode - Problem 560 - Subarray Sum Equals K)
#         https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0 (GeeksForGeeks - Subarray with given sum)
#
# **************************************************************************
# Algorithm Complexity Explanation
# **************************************************************************
# Time : O(N)
# **************************************************************************
# The time complexity is O(N): The entire nums array is traversed only once.
#
# **************************************************************************
# Space : O(N)
# **************************************************************************
# Hashmap/dictionary running_sum can contain upto nn distinct entries in the worst case.
#
# **************************************************************************
# Explanation
# **************************************************************************
#
# First of all, the basic idea behind this code is that, whenever the sums has increased by a value of k,
# we've found a subarray of sums=k.
# I'll also explain why we need to initialise a 0 in the hashmap [ in python we can use a defaultdict(int)  for this ].
# Example: Let's say our elements are [1,2,1,3] and k = 3.
# and our corresponding running sums = [1,3,4,7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7,
# there is an increase of k.
# So, we've found 2 subarrays of sums=k.
#
# But, if you look at the original array, there are 3 subarrays of sums==k.
# Now, you'll understand why 0 comes in the picture.
#
# In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
# However, if sums==k, it should've been 3-0=k. But 0 is not present in the array.
# To account for this case, we include the 0.
# Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.
#
# 0->3
# 1->4
# 4->7
# Hence, 3 sub arrays of sums=k
from collections import defaultdict
from typing import List

import unittest


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, sum = 0, 0
        running_sum = defaultdict(int)
        running_sum[0] = 1

        for n in nums:
            sum += n
            count += running_sum[sum - k]
            running_sum[sum] += 1

        return count


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_subarraySum(self) -> None:
        s = Solution()
        # nums = [1, 1, 1]
        # k = 2
        # solution = 2
        # self.assertEqual(solution, s.subarraySum(nums, k), "Should return the total number of continuous subarrays whose sum equals to K")
        for nums, k, solution in (
            [[1, 1, 1], 2, 2],  # [1,1] [1,1]
            [[1, 2, 3], 3, 2],  # [1,2] [3]
            [
                [2, 2, 3, 0, 4, -1, 1, 6],
                7,
                5,
            ],  # [2,2,3] [2,2,3,0] [3,0,4] [3,0,4,-1,1] [1,6]
        ):
            self.assertEqual(
                solution,
                s.subarraySum(nums, k),
                "Should return the total number of continuous subarrays whose sum equals to K",
            )


if __name__ == "__main__":
    unittest.main()
