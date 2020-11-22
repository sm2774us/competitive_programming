#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Geeks For Geeks: Box Stacking Problem
#
# Description:
#
# You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and length l. You task is to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base.It is also allowable to use multiple instances of the same type of box. You task is to complete the function maxHeight which returns the height of the highest possible stack so formed.
#
#
# Note:
# Base of the lower box should be strictly larger than that of the new box we're going to place. This is in terms of both length and width, not just in terms of area. So, two boxes with same base cannot be placed one over the other.
#
#
#
# Example 1:
#
# Input:
# n = 4
# height[] = {4,1,4,10}
# width[] = {6,2,5,12}
# length[] = {7,3,6,32}
# Output: 60
# Explanation: One way of placing the boxes is
# as follows in the bottom to top manner:
# (Denoting the boxes in (l, w, h) manner)
# (12, 32, 10) (10, 12, 32) (6, 7, 4) (5, 6, 4)
# (4, 5, 6) (2, 3, 1) (1, 2, 3)
# Hence, the total height of this stack is
# 10 + 32 + 4 + 4 + 6 + 1 + 3 = 60.
# No other combination of boxes produces a height
# greater than this.
#
# Example 2:
#
# Input:
# n = 3
# height[] = {1,4,3}
# width[] = {2,5,4}
# length[] = {3,6,1}
# Output: 15
#
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function maxHeight() which takes three arrays height[], width[], length[], and N as a number of boxes and returns the highest possible stack height which could be formed.
#
#
# Expected Time Complexity : O(N*N)
# Expected Auxiliary Space: O(N)
#
#
# Constraints:
#   * 1<=N<=100
#   * 1<=l,w,h<=100
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/box-stacking/1 (GeeksForGeeks - Box Stacking Problem)
# **************************************************************************
#
# Reference
# **************************************************************************
# https://github.com/OpenGenus/cosmos/blob/bb07b7beb3fb2e367e83b1c81bfc08a76d50a16b/code/dynamic_programming/src/box_stacking/box_stacking.py
#
from typing import List

from collections import namedtuple
from itertools import permutations

import unittest

dimension = namedtuple("Dimension", "height length width")


class Solution(object):
    def create_rotation(self, given_dimensions: List[dimension]) -> dimension:
        """
        A rotation is an order wherein length is greater than or equal to width. Having this constraint avoids the
        repetition of same order, but with width and length switched.
        For e.g (height=3, width=2, length=1) is same the same box for stacking as (height=3, width=1, length=2).
        :param given_dimensions: Original box dimensions
        :return: All the possible rotations of the boxes with the condition that length >= height.
        """
        for current_dim in given_dimensions:
            for (height, length, width) in permutations(
                (current_dim.height, current_dim.length, current_dim.width)
            ):
                if length >= width:
                    yield dimension(height, length, width)

    def sort_by_decreasing_area(self, rotations: List[dimension]) -> List[dimension]:
        return sorted(rotations, key=lambda dim: dim.length * dim.width, reverse=True)

    def can_stack(self, box1: dimension, box2: dimension) -> bool:
        return box1.length < box2.length and box1.width < box2.width

    def box_stack_max_height(self, dimensions: List[dimension]) -> int:
        boxes = self.sort_by_decreasing_area(
            [rotation for rotation in self.create_rotation(dimensions)]
        )
        num_boxes = len(boxes)
        T = [rotation.height for rotation in boxes]
        R = [idx for idx in range(num_boxes)]

        for i in range(1, num_boxes):
            for j in range(0, i):
                if self.can_stack(boxes[i], boxes[j]):
                    stacked_height = T[j] + boxes[i].height
                    if stacked_height > T[i]:
                        T[i] = stacked_height
                        R[i] = j

        max_height = max(T)
        start_index = T.index(max_height)

        # # Prints the dimensions which were stored in R list.
        # while True:
        #     print(boxes[start_index])
        #     next_index = R[start_index]
        #     if next_index == start_index:
        #         break
        #     start_index = next_index

        return max_height


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_box_stack_max_height(self) -> None:
        sol = Solution()
        for boxes, solution in (
            [
                [
                    dimension(4, 7, 6),
                    dimension(1, 3, 2),
                    dimension(4, 6, 5),
                    dimension(10, 32, 12),
                ],
                60,
            ],
            [[dimension(1, 3, 2), dimension(4, 6, 5), dimension(3, 1, 4)], 15],
            [
                [
                    dimension(5, 4, 2),
                    dimension(6, 3, 1),
                    dimension(1, 3, 2),
                    dimension(8, 6, 3),
                ],
                22,
            ],
        ):
            self.assertEqual(solution, sol.box_stack_max_height(boxes))


# main
if __name__ == "__main__":
    # sol = Solution()
    # # input boxes
    # boxes = [dimension(5, 4, 2), dimension(6, 3, 1), dimension(1, 3, 2), dimension(8, 6, 3)]
    # print("The maximum height is", sol.box_stack_max_height(boxes))
    unittest.main()
