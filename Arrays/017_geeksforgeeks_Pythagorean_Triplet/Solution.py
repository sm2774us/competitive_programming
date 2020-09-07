#
# Time : O(N); Space: O(1)
# @tag : Arrays, Math
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Pythagorean Triplet
#
# Given an array of integers, write a function that returns true if there is a triplet (a, b, c)
# that satisfies a^2 + b^2 = c^2.
#
# Example:
#
# Input: [3, 2, 4, 6, 5]
# Output: True
# Explanation: a=3, b=4, and c=5 forms a pythagorean triplet, so True
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/pythagorean-triplet/0 (GeeksForGeeks - Pythagorean Triplet)
#
# Solution Hint: https://leetcode.com/discuss/interview-question/125149/find-pythagorean-triplets-in-an-array-faster-than-on2
#
# Math explanation: https://www.youtube.com/watch?v=86YAPbZmsRI
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# We use a math trick:
#   1. Given the lowest number in a Pythagoream Triplet => [5, 12, 13] => 5^2 + 12^2 = 13^2 => 25 + 144 = 169
#      5
#       1.1 If the number is odd
#       1.2 Square the lowest number and then divide by 2 => 5^2 / 2 => 12.5
#       1.3 To obtain the next two numbers in the triplet subtract 0.5 and add 0.5 =>
#           12.5 - 0.5 => 12
#           12.5 + 0.5 => 13
#   2. Given the lowest number in a Pythagoream Triplet => [8, 15, 17] => 8^2 + 15^2 = 17^2 => 64 + 225 = 289
#      8
#       2.1 If the number is even
#       1.2 Divide the number by 2 and then square this number => 8/2 => 4^2 => 16
#       1.3 To obtain next two numbers in the triplet subtract 1 and add 1 =>
#           16 - 1 => 15
#           16 + 1 => 17
#
from typing import List

import unittest


class Solution:
    # Time: O(n)
    # Space: O(1)
    def findPythagoreanTriplets(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        b = c = 0

        for val in nums:
            # odd number
            if val % 2 != 0:
                b = val ** 2 // 2
                c = b + 1
                if b in nums and c in nums:
                    return True
            # even number
            else:
                b = (val // 2) ** 2 - 1
                c = b + 2
                if b in nums and c in nums:
                    return True
        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findPythagoreanTriplets(self) -> None:
        s = Solution()
        for nums, solution in (
            [[3, 2, 4, 6, 5], True],  # 3^2 + 4^2 = 5^2 => So Pythagorean Triplets exist
            [[3, 2, 4, 6, 7], False],  # No Pythagorean Triplets exist
            [
                [1, 2, 5, 12, 13],
                True,
            ],  # 5^2 + 12^2 = 13^2 => So Pythagorean Triplets exist
            [
                [25, 2, 24, 1, 7],
                True,
            ],  # 7^2 + 24^2 = 15^2 => So Pythagorean Triplets exist
            [
                [9, 10, 8, 61, 60, 35, 11],
                True,
            ],  # 11^2 + 60^2 = 61^2 => So Pythagorean Triplets exist
            [[9, 10, 8, 11, 16, 35, 17], False],  # No Pythagorean Triplets exist
            [
                [17, 10, 15, 11, 8, 35, 46],
                True,
            ],  # 8^2 + 15^2 = 17^2 => So Pythagorean Triplets exist
        ):
            self.assertEqual(
                solution,
                s.findPythagoreanTriplets(nums),
                "Should return true if Pythagorean Triplets exist in the array",
            )


if __name__ == "__main__":
    unittest.main()
