#
# Time : O(N) [ We traverse all elements of the tree once so total time complexity is O(n) ] ; Space: O(1)
# @tag : Tree and BST ; Recursion
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 366: Find Leaves of Binary Tree
#
# Description:
#
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# **************************************************************************
# Source: https://leetcode.com/problems/find-leaves-of-binary-tree/ (Leetcode - Problem 366 - Find Leaves of Binary Tree)
#
from typing import List

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeavesHelper(self, root, results):
        """
        push root and all descendants to results
        return the distance from root to farthest leaf
        """
        if not root:
            return -1

        ret = 1 + max(
            self.findLeavesHelper(child, results) for child in (root.left, root.right)
        )

        if ret >= len(results):
            results.append([])

        results[ret].append(root.val)

        return ret

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.findLeavesHelper(root, ret)
        return ret


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findLeaves(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        self.assertEqual([[4, 5, 3], [2], [1]], s.findLeaves(root))


if __name__ == "__main__":
    unittest.main()
