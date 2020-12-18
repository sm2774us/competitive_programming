#
# Time  :
# Space :
# @tag  : Arrays
# @by   : Shaikat Majumdar
# @date : Aug 27, 2020
# **************************************************************************
# Facebook | Onsite | Generate random max index
#
# Given an array of integers arr, randomly return an index of the maximum value seen by far.
#
# Example:
# Input: [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
#
# Having iterated up to the at element index 5 (where the last 30 is), randomly give an index among [1, 3, 4, 5]
# which are indices of 30 - the max value by far. Each index should have a ¼ chance to get picked.
#
# Having iterated through the entire array, randomly give an index between 8 and 9
# which are indices of the max value 62.
#
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/451431/facebook-onsite-generate-random-max-index (Facebook | Onsite | Generate random max index)
#
# **************************************************************************
# Reference: https://www.careercup.com/question?id=5732335291465728
# **************************************************************************
#
#
from typing import List
from random import randint

import unittest


class Solution:

    #
    # Facebook have a practice of asking problems on Random and Reservoir Sampling.
    # This problem relates to Reservoir Sampling.
    # It should be solved with O(1) space and time O(N).
    # Hence, any solution beyond would be considered by interviewer as failed.
    #
    def maxRandomIndex(self, arr: List[int]) -> None:
        max_value = 0
        for i in range(len(arr)):
            if arr[i] > max_value:
                max_value = arr[i]
                max_indexes = []
            if arr[i] == max_value:
                max_indexes.append(i)
            print("Seen so far: {}".format(arr[: i + 1]))
            print("Max: {}".format(max_value))
            print("Max indexes: {}".format(max_indexes))
            print(
                "Random max index: {}".format(
                    max_indexes[randint(0, len(max_indexes) - 1)]
                )
            )
            print("")


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxRandomIndex(self) -> None:
        sol = Solution()
        arr = [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
        sol.maxRandomIndex(arr)


if __name__ == "__main__":
    # sol = Solution()
    # arr = [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
    # sol.maxRandomIndex(arr)
    unittest.main()
