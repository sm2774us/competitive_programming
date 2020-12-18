#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 1589: Maximum Sum Obtained of Any Permutation
#
# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.
#
# Return the maximum total sum of all requests among all permutations of nums.
#
# Since the answer may be too large, return it modulo 109 + 7.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
# Output: 19
# Explanation: One permutation of nums is [2,1,3,4,5] with the following result:
# requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
# requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
# Total sum: 8 + 3 = 11.
# A permutation with a higher total sum is [3,5,4,2,1] with the following result:
# requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
# requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
# Total sum: 11 + 8 = 19, which is the best that you can do.
# Example 2:
#
# Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
# Output: 11
# Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
# Example 3:
#
# Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
# Output: 47
# Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
#
#
# Constraints:
#
#   * n == nums.length
#   * 1 <= n <= 105
#   * 0 <= nums[i] <= 105
#   * 1 <= requests.length <= 105
#   * requests[i].length == 2
#   * 0 <= starti <= endi < n
#
# **************************************************************************
# Source: https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/ (LeetCode - Problem 1589 - Maximum Sum Obtained of Any Permutation)
# **************************************************************************
#
from typing import List

import unittest


class Solution(object):

    # Solution 1: Sweep Line Algorithm
    #
    # Intuition
    # We want to calculate the frequency for A[i].
    # Assign the big element A[i] to the position queried more frequently.
    #
    #
    # Explanation
    # For each request [i,j],
    # we set count[i]++ and count[j + 1]--,
    #
    # Then we sweep once the whole count,
    # we can find the frequency for count[i].
    #
    # Note that for all intervals inputs,
    # this method should be the first intuition you come up with.
    #
    #
    # Complexity
    # Time O(NlogN) for sorting
    # Space O(N)
    #
    # TC: O(NlogN) for sorting
    # SC: O(N)
    #
    # More Sweep Line Problems:
    # 1) LeetCode - Problem 253 - Meeting Rooms II - https://leetcode.com/problems/meeting-rooms-ii/
    # 2) LeetCode - Problem 1094 - Car Pooling - https://leetcode.com/problems/car-pooling/discuss/317610/JavaC++Python-Meeting-Rooms-III
    # 3) LeetCode - Problem 1109 - Corporate Flight Bookings - https://leetcode.com/problems/corporate-flight-bookings/discuss/328856/JavaC%2B%2BPython-Straight-Forward-Solution
    #
    def maxSumRangeQuery_solution_1(
        self, nums: List[int], requests: List[List[int]]
    ) -> int:
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for v, c in zip(sorted(count[:-1]), sorted(nums)):
            res += v * c
        return res % (10 ** 9 + 7)

    # Solution 2:
    #
    # Let's start with the obvious, if there is only one request = [start, end], which covers k = end - start + 1 elements, then the maximum sum would be the sum of the largest k numbers from nums. Because only elements in between start and end will count, we will greedily put the largest numbers to the index between start and end. Since we can choose any permutation, it means we have the freedom to assign numbers from nums to any index we want.
    #
    # In general, the greedy strategy still works. We need to put the largest number to the index that has been requested the most. Because if an index has been requested m times, then it will contribute m * (value we assign to that index) to the final sum. The number of requests plays the role of weight or importance.
    #
    # Now it boils down to how to compute the number of requests for each index. Since each request is an interval, we can do this more efficiently than looping over each requested interval and count. A similar problem is Car Pool. (BTW, I also encountered that problem during a contest, that time I struggled and used a heap).
    #
    # We can solve this problem in linear time. Starting from an array t = [0] * (len(nums) + 1), for each request = [start, end], we let t[start] += 1, indicate that every index after this point will be counted 1 more time because of this request, and t[end + 1] -= 1, indicate that every index after end will be counted 1 less time because of the end of this request. Now the prefix sum of this array t is corresponds to the number of requests for each index. We choose array t has length len(nums) + 1, only because we need to ensure end + 1 is within the range when we put t[end+1] -= 1. To compute the number of requests for indices, we will only count the first len(nums) prefix sums.
    #
    # We record every prefix sum(i.e. the number of requests) in a new array (or we can do it inplace at t), then we just follow the greedy strategy, to sort both t and nums, and take the sum of t[i] * nums[i] for all i, i.e. dot product between t and nums.
    #
    # Time Complexity:
    # Let N1, N2 be the size of nums and requests. Since we loop through all requests, that is O(N2),
    # computing prefix sum of t and looping through nums are O(N1). Finally sorting takes O(N1 * log(N1)), so it is O(N1 * log(N1) + N2).
    #
    # Space Complexity:
    # Only new array is t, it is O(N1).
    #
    #
    # TC: O(N1 * log(N1) + N2)
    # SC: O(N1)
    #
    # Similar Problems:
    # 2) LeetCode - Problem 1094 - Car Pooling - https://leetcode.com/problems/car-pooling/
    #
    def maxSumRangeQuery_solution_2(
        self, nums: List[int], requests: List[List[int]]
    ) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        t = [0] * (n + 1)
        for a, b in requests:
            t[a] += 1
            t[b + 1] -= 1
        for i in range(1, n):
            t[i] += t[i - 1]

        nums.sort()
        t.pop()
        t.sort()

        return sum(a * b for a, b in zip(nums, t)) % mod


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maxSumRangeQuery(self):
        s = Solution()
        for nums, requests, solution in (
            [[1, 2, 3, 4, 5], [[1, 3], [0, 1]], 19],
            [[1, 2, 3, 4, 5, 6], [[0, 1]], 11],
            [[1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]], 47],
        ):
            self.assertEqual(s.maxSumRangeQuery_solution_1(nums, requests), solution)
            self.assertEqual(s.maxSumRangeQuery_solution_2(nums, requests), solution)


if __name__ == "__main__":
    unittest.main()
