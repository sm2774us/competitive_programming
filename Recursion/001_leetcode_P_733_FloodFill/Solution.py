#
# Time : O(N); Space: O(1)
# @tag : Recursion ; DFS ; BFS
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 733: Flood Fill
#
# Description:
#
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image
# (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
# and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally
# to the starting pixel of the same color as the starting pixel, plus any pixels
# connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
# Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
#
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
#
# Note:
#
#   * The length of image and image[0] will be in the range [1, 50].
#   * The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
#   * The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
#
# **************************************************************************
# Source: https://leetcode.com/problems/flood-fill/ (Leetcode - Problem 733 - Flood Fill)
#         https://practice.geeksforgeeks.org/problems/flood-fill-algorithm/0 (GeeksForGeeks - Flood fill Algorithm)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
#
from typing import List

import unittest

# This question is a simplified version of - [ LeetCode - Problem 200 - Number of Islands ].
# There is no difference in speed between DFS and BFS.
#
# NOTES:
# ==================
# DFS - because of the use of recursion, will be shorter to write
# BDS - Uses deque ( collections.deque )
#
# Paint the initial grid, and then recursively fill the function in four directions.
# Flood Fill is completed when the recursion ends.
#
# For [ LeetCode - Problem 200 - Number of Islands ], you only need to nest a double loop in the outer layer,
# and run the paint function once for each grid.


class Solution:
    # DFS Recursive Solution
    def floodFillRecursiveUsingDFS(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:

        color = image[sr][sc]
        if color == newColor:
            return image
        row, col = len(image), len(image[0])

        def paint(x, y):
            nonlocal row, col, newColor, image
            if x in range(row) and y in range(col) and image[x][y] == color:
                image[x][y] = newColor
                # In Python3, the map function is lazy, and the function inside will not be calculated without adding list
                list(map(paint, (x + 1, x - 1, x, x), (y, y, y + 1, y - 1)))

        paint(sr, sc)
        return image

    # BFS Iterative Solution
    def floodFillIterativeUsingBFS(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:

        # The coloring problem is a classic BFS problem
        if not image:
            return None
        if image[sr][sc] == newColor:
            return image

        row, col = len(image), len(image[0])
        oldColor = image[sr][sc]
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        from collections import deque

        paint = deque([(sr, sc)])

        # Starting from sr, sc, put the grid of the same color into the deque,
        # Pop out the elements from the deque and fill in four directions
        # deque empty stop the loop
        while paint:
            i, j = paint.popleft()
            image[i][j] = newColor
            for dx, dy in direction:
                if (
                    i + dx >= 0
                    and i + dx < row
                    and j + dy >= 0
                    and j + dy < col
                    and image[i + dx][j + dy] == oldColor
                ):
                    # python does not support the continuous writing of 0 <= x < row
                    paint.append((i + dx, j + dy))
                    image[i + dx][j + dy] = newColor

        return image


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_floodFillRecursiveUsingDFS(self) -> None:
        s = Solution()
        image, sr, sc, newColor = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2
        self.assertEqual(
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            s.floodFillRecursiveUsingDFS(image, sr, sc, newColor),
        )

    def test_floodFillIterativeUsingBFS(self) -> None:
        s = Solution()
        image, sr, sc, newColor = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2
        self.assertEqual(
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            s.floodFillIterativeUsingBFS(image, sr, sc, newColor),
        )


if __name__ == "__main__":
    unittest.main()
