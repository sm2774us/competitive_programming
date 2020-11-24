#
# Time  :
# Space :
#
# @tag : Divide And Conquer ; Binary Search
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 33: Search in Rotated Sorted Array
#
# Description:
#
# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#   * 1 <= nums.length <= 5000
#   * -10^4 <= nums[i] <= 10^4
#   * All values of nums are unique.
#   * nums is guranteed to be rotated at some pivot.
#   * -10^4 <= target <= 10^4
#
# **************************************************************************
# Source: https://leetcode.com/problems/search-in-rotated-sorted-array/ (LeetCode - Problem 33 - Search in Rotated Sorted Array)
#         https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array/0 (GeeksForGeeks - Search in a Rotated Array)
# **************************************************************************
#
# References:
# **************************************************************************
# https://en.wikipedia.org/wiki/Binary_search_algorithm
#
from typing import List
import bisect

import unittest


class Solution(object):

    # Solution_1 : Binary Search
    #
    # Base Case : if found target value, return the index
    #
    # 1) Determine it's left rotated or right rotated
    #
    #       No rotated:
    #             1 2 3 4 5 6 7
    #                  mid
    #
    #             left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
    #             3 4 5 6 7 1 2
    #                  mid
    #             search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side
    #
    #             right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
    #             6 7 1 2 3 4 5
    #                  mid
    #             search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
    #
    #   1.1) If Left-Rotated
    #           - handle ascending order side
    #           - handle descending order side
    #
    #   1.2) If Right-Rotated
    #           - handle ascending order side
    #           - handle descending order side
    #
    # 2) Cannot find the target value
    #
    # Time: O(log(n))
    #
    def search_solution_1_simple_binary_search(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if found target value, return the index
            if nums[mid] == target:
                return mid

            # determine it's left rotated or right rotated
            """
            No rotated:
            1 2 3 4 5 6 7
                 mid

            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid          
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
            """
            if nums[mid] >= nums[left]:  # left rotated
                # in ascending order side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # right rotated
                # in ascending order side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        # cannot find the target value
        return -1

    # Solution_2 : Binary Search Variant
    #
    # 1) Find the index of the smallest value using binary search.
    # 2) Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
    # 3) Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
    # 4) left==right is the index of the smallest value and also the number of places rotated.
    # 5) The usual binary search and accounting for rotation.
    #
    # Time: O(log(n))
    #
    def search_solution_2_binary_search_variant(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the least value: pivot idx
        pivot_idx = self.find_pivot(nums)
        # the normal binary search
        left = pivot_idx
        right = pivot_idx + len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[self.change_idx(nums, mid)] == target:
                return self.change_idx(nums, mid)
            elif nums[self.change_idx(nums, mid)] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def find_pivot(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            # until left == right
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return left

    def change_idx(self, nums: List[int], idx: int) -> int:
        return idx % len(nums)

    # Solution_3 : Binary Search With Clever Idea
    #
    # Explanation:
    # ===================
    #   Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #
    #   Because it's not fully sorted, we can't do normal binary search. But here comes the trick:
    #
    #       * If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
    #         [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
    #
    #       * If target is let's say 7, then we adjust nums to this:
    #         [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #
    #   And then we can simply do ordinary binary search.
    #
    #   Of course we don't actually adjust the whole array but instead adjust only on the fly only the elements
    #   we look at. And the adjustment is done by comparing both the target and the actual element against nums[0].
    #
    # Code
    #
    #   If nums[mid] and target are "on the same side" of nums[0], we just take nums[mid]. Otherwise we use -infinity or +infinity as needed.
    #
    #
    # Time: O(log(n))
    #
    def search_solution_3_binary_search_with_clever_idea(
        self, nums: List[int], target: int
    ) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, H = 0, len(nums)
        while L < H:
            M = (L + H) // 2
            if target < nums[0] < nums[M]:  # -inf
                L = M + 1
            elif target >= nums[0] > nums[M]:  # +inf
                H = M
            elif nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                H = M
            else:
                return M
        return -1

    # Solution_3 : Binary Search With Clever Idea
    #
    # Explanation:
    # ===================
    # We can also view the array as already sorted with the following transformation:
    #
    # tuple: (value less than nums[0]?, value)
    # [1,2,3,4,5] -> [(0,1), (0,2), (0,3), (0,4), (0,5)]
    # [5,1,2,3,4] -> [(0,5), (1,1), (1,2), (1,3), (1,4)]
    #
    # then we can apply our standard binary search
    #
    # Time: O(log(n))
    #
    def search_solution_4_binary_search_with_presort_using_transform(
        self, nums: List[int], target: int
    ) -> int:
        lo, hi, t = 0, len(nums) - 1, (target < nums[0], target)
        while lo <= hi:
            mid = (lo + hi) // 2
            guess = (nums[mid] < nums[0], nums[mid])
            if guess == t:
                return mid
            elif guess < t:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def search_solution_5_binary_search_with_presort_using_transform_and_using_bisect(
        self, nums: List[int], target: int
    ) -> int:
        N, t = nums, target
        i = bisect.bisect_left([(x < N[0], x) for x in N], (t < N[0], t))
        return i if t in N[i : i + 1] else -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_search(self) -> None:
        sol = Solution()
        for nums, target, solution in (
            [[5, 6, 7, 8, 9, 10, 1, 2, 3], 10, 5],
            [[3, 1, 2], 1, 1],
            [[3, 5, 1, 2], 6, -1],
            [[4, 5, 6, 7, 0, 1, 2], 0, 4],
            [[4, 5, 6, 7, 0, 1, 2], 3, -1],
            [[1], 0, -1],
        ):
            self.assertEqual(
                solution, sol.search_solution_1_simple_binary_search(nums, target)
            )
            self.assertEqual(
                solution, sol.search_solution_2_binary_search_variant(nums, target)
            )
            self.assertEqual(
                solution,
                sol.search_solution_3_binary_search_with_clever_idea(nums, target),
            )
            self.assertEqual(
                solution,
                sol.search_solution_4_binary_search_with_presort_using_transform(
                    nums, target
                ),
            )
            self.assertEqual(
                solution,
                sol.search_solution_5_binary_search_with_presort_using_transform_and_using_bisect(
                    nums, target
                ),
            )


# main
if __name__ == "__main__":
    unittest.main()
