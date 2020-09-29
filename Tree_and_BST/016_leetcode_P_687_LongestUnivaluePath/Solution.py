#
# Time : O(N) [ N = Number of nodes in the Binary Tree ] ; Space: O(1)
# @tag : Tree and BST ; Recursion ; Divide and Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 687: Longest Univalue Path
#
# Description:
#
# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
#
# **************************************************************************
# Source: https://leetcode.com/problems/longest-univalue-path/ (Leetcode - Problem 687 - Longest Univalue Path)
#         https://www.geeksforgeeks.org/longest-path-values-binary-tree/ (GeeksForGeeks - Longest Path with Same Values in a Binary Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# We are asked to find maxUnivaluePath, the length of the longest path where each node in the path has the same value.
# The maxUnivaluePath is possible to root at each node.
#
#      root
#   /       \
# leftPath  rightPath
# we assume
# leftPath indicates max univalue path starting from root.left,
# rightPath indicates max univalue path starting from root.right,
#
# then
# leftPath = (root.val == root.left.val) ? leftPath + 1 : 0// subproblem
# rightPath = (root.val == root.right.val) ? rightPath + 1 : 0 // subproblem
#
# update maxUnivaluePath by leftPath + rightPath, which is max univalue path rooted at root.
#
# then
# max(leftPath, rightPath) is max univalue path starting from root // conquer
#
from collections import deque

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.maxUnivalPath = (
            0
        )  # The length of the longest path where each node in the path has the same value.
        self.getLongestUnivaluePathRootedAt(root)
        return self.maxUnivalPath

    def getLongestUnivaluePathRootedAt(self, root):
        """Get length of longest univalue path rooted at root."""
        if not root:
            return 0

        leftSubtreePath = self.getLongestUnivaluePathRootedAt(root.left)
        rightSubtreePath = self.getLongestUnivaluePathRootedAt(root.right)

        if root.left != None and root.val == root.left.val:
            leftSubtreePath += 1
        else:
            leftSubtreePath = 0

        if root.right != None and root.val == root.right.val:
            rightSubtreePath += 1
        else:
            rightSubtreePath = 0

        self.maxUnivalPath = max(self.maxUnivalPath, leftSubtreePath + rightSubtreePath)

        return max(leftSubtreePath, rightSubtreePath)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_longestUnivaluePath(self) -> None:
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        self.assertEqual(2, s.longestUnivaluePath(root))
        root = TreeNode(1)
        root.left = TreeNode(4)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        self.assertEqual(2, s.longestUnivaluePath(root))
        root = TreeNode(2)
        root.left = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(2)
        self.assertEqual(2, s.longestUnivaluePath(root))
        root = TreeNode(4)
        root.left = TreeNode(4)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(9)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(3, s.longestUnivaluePath(root))


if __name__ == "__main__":
    unittest.main()
