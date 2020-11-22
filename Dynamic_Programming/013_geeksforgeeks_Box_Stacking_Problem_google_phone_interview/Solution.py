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
from typing import List

import unittest

# Data structure to store a box (L x W x H)
class Box:
    def __init__(self, length, width, height):
        # constraint: width is never more than length
        self.length = length
        self.width = width
        self.height = height


class Solution(object):
    # Function to generate rotations of all the boxes
    def createAllRotations(self, boxes: List[Box]) -> List[Box]:

        # stores all rotations of each box
        rotations = []

        # do for each box
        for box in boxes:
            # push the original box: L x W x H
            rotations.append(box)

            # push the first rotation: max(L, H) x min(L, H) x W
            rotations.append(
                Box(max(box.length, box.height), min(box.length, box.height), box.width)
            )

            # push the second rotation: max(W, H) x min(W, H) x L
            rotations.append(
                Box(max(box.width, box.height), min(box.width, box.height), box.length)
            )

        return rotations

    # Create a stack of boxes which is as tall as possible
    def maxHeight(self, boxes: List[Box]) -> int:

        # generate rotations of each box
        rotations = self.createAllRotations(boxes)

        # sort the boxes in descending order of area(L x W)
        rotations.sort(key=lambda x: x.length * x.width, reverse=True)

        # max_height[i] stores the maximum possible height when i'th box is on the top
        max_height = [0] * len(rotations)

        # fill max_height in bottom-up manner
        for i in range(len(rotations)):
            for j in range(i):
                # dimensions of the lower box are each strictly larger than those
                # of the higher box
                if (
                    rotations[i].length < rotations[j].length
                    and rotations[i].width < rotations[j].width
                ):
                    max_height[i] = max(max_height[i], max_height[j])

            max_height[i] += rotations[i].height

        # return the maximum value in max_height
        return max(max_height)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxHeight(self) -> None:
        sol = Solution()
        for boxes, solution in (
            [[Box(7, 6, 4), Box(3, 2, 1), Box(6, 5, 4), Box(32, 12, 10)], 60],
            [[Box(3, 2, 1), Box(6, 5, 4), Box(1, 4, 3)], 15],
            [[Box(4, 2, 5), Box(3, 1, 6), Box(3, 2, 1), Box(6, 3, 8)], 22]
            # [[Box(9,3,9), Box(10,1,4), Box(11,5,10), Box(3,3,9), Box(3,1,5), Box(1,7,12)], 3]
        ):
            self.assertEqual(solution, sol.maxHeight(boxes))


# main
if __name__ == "__main__":
    # sol = Solution()
    # # input boxes
    # boxes = [Box(4, 2, 5), Box(3, 1, 6), Box(3, 2, 1), Box(6, 3, 8)]
    # print("The maximum height is", sol.maxHeight(boxes))
    unittest.main()
