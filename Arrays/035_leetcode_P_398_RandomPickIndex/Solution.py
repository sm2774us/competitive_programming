#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 398: Random Pick Index
#
# Given an array of integers with possible duplicates, randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
#
# **************************************************************************
# Source: https://leetcode.com/problems/random-pick-index/ (LeetCode - Problem 398 - Random Pick Index)
# **************************************************************************
#
from typing import List
from collections import namedtuple
import random

import unittest


# Solution 1: Reservoir Sampling
#
# Reservoir sampling is usually used to randomly pick up k elements in an array S with very big size N
# or in a data stream S with the same probability.
# The idea of the algorithm is:
#
#   (1) Get the first k elements from S and put them into an array result[]
#   (2) for j >= k && j < N:
#           generate a random number r [0, j]
#           if r < k: result[r] = S[j]
#
# For this question, we can take k = 1, and we only care about the number whose value equals target.
# First, keep an array of size 1 (just a variable V works).
# Then assign the first index of the target to it. We can loop every element in input,
# and at the meantime, use a count to record how many target we've seen now (same role as j).
# Then generate a random number [0, count). If the number == 0, we can replace the V's value
# with the new index. After visiting every element in S, the V's value is what we want.
#
# You may wonder, why Reservoir Sampling can guarantee the equal possibility.
# Let's take a look at the original problem and solution. When we see element S[j],
# the possibility of choosing it into the reservoir is k/j, and the possibility of its
# being replaced by ONE elements(t, t > j) later is (k/t)/k = 1/t.
# Therefore, the probability of S[j] not being replaced by ANY OTHER elements later in S is:
#
# (1 - 1/(j + 1)) * (1 - 1/(j + 2)) * ......* (1 - 1/N) = j/N
#
# Therefore, the posibiility of S[j] is in the Reservoir is
#
# k/j * j/N = k/N
#
class ReservoirSamplingSolution(object):
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = idx = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            if cnt == 0:
                idx = i
                cnt = 1
            else:
                # this random will already give me numbers
                # between 0 and cnt inclusive
                # so for 2nd number I am getting random number 0 and 1
                # so each having a probability of 1/2
                # similarly for three numbers it will be 1/3
                rnd = random.randint(0, cnt)
                if rnd == cnt:
                    idx = i
                cnt += 1

        return idx


#
# The fact there's an __init__ in the template implies that the solution wants us to preprocess
# and optimise for the pick()
#
# 0. Store the numbers as pairs: (num, original_idx), then sort this list by num so we can do binary search
#
# 1. Do 2 binary searches:
#   1.1. To find the leftmost index in srt_nums that contians the target.
#   We do this by checking when target is found, is the target also to the left of us? Then move search space left
#   1.2. To find the rightmost.
#   When target is found, if target is also to the right of us, then move search space right
#
# 2. Pick an index between leftmost and rightmost, get that element from srt_nums and return its original index.
#
# RT: Preprocess = O(N lg N), Pick = O(lg N)
# Spc: O(N), we must store the original indices
#
# TC: O(NlogN) preprocess ; O(logN) pick
# SC: O(N)
class BinarySearchSolution(object):
    def __init__(self, nums: List[int]):
        Pair = namedtuple("Pair", ["num", "idx"])
        # Store the numbers along with their original indices.
        self.nums = [Pair(num, i) for i, num in enumerate(nums)]
        # Sort by the numbers so we can binary search over them.
        self.nums.sort()

    def bin_search(self, nums, target, find_begin):
        """@find_begin: If True, then we're trying to find the lowest index
            that contains the target. If False, we're trying to find the highest index.
        """
        L = 0
        R = len(nums) - 1
        while True:  # Target guaranteed to be in nums so no break condition.
            mid = (L + R) // 2
            if nums[mid].num < target:
                L = mid + 1
            elif nums[mid].num > target:
                R = mid - 1
            else:
                if find_begin:
                    # If we found the target but the target is also to the left of us
                    # move the search space to the left so that we can find the leftmost
                    # index containing the target.
                    if (mid - 1) >= 0 and nums[mid - 1].num == target:
                        R = mid - 1
                    else:
                        # If the target is not to the left, we found the leftmost index.
                        return mid
                else:
                    # The same but we check if target is to the right, and in this case
                    # move search space to the right.
                    if (mid + 1) < len(nums) and nums[mid + 1].num == target:
                        L = mid + 1
                    else:
                        return mid

    def pick(self, target: int) -> int:
        begin_idx = self.bin_search(self.nums, target, True)
        end_idx = self.bin_search(self.nums, target, False)
        between_idx = random.randint(begin_idx, end_idx)
        return self.nums[between_idx].idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pick(self):
        nums = [1, 2, 3, 3, 3]
        reservoirSamplingSolution = ReservoirSamplingSolution(nums)
        pick = reservoirSamplingSolution.pick(3)
        print(f"Reservoir Sampling Algorithm pick = {pick}")

        binarySearchSolution = BinarySearchSolution(nums)
        pick = binarySearchSolution.pick(3)
        print(f"Binary Search Algorithm pick = {pick}")


if __name__ == "__main__":
    unittest.main()
