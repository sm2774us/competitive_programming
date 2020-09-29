#
# Time : O(N) [ N = Number of nodes in the Binary Tree ] ; Space: O(1)
# @tag : Tree and BST ; Recursion ; DFS ; Kadane's Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 124: Binary Tree Maximum Path Sum
#
# Description:
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
# along the parent-child connections. The path must contain at least one node and does not need to go through
# the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-maximum-path-sum/ (Leetcode - Problem 124 - Binary Tree Maximum Path Sum)
#         https://practice.geeksforgeeks.org/problems/maximum-path-sum/1 (GeeksForGeeks - Maximum Path Sum between 2 Leaf Nodes)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Recursive
# **************************************************************************
# Refer to Solution_Explanation.md.
#
# **************************************************************************
# Iterative ( using DFS )
# **************************************************************************
# The idea is to update node values with the biggest, positive cumulative sum gathered by its children:
#
#   * If both contributions are negative, no value is added.
#   * If both are positive, only the biggest one is added, so that we don't include both children during the rest of the tree exploration.
#   * Leaves return its own value and we recursively work our way upwards.
#
# A global maximum sum variable is maintained so that every path can be individually checked, while updated node values on the tree allow for exploration of other valid paths outside of the current subtree.
#
# More details in the code comments:
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
    # Recursive solution
    def maxPathSumRecursive(self, root: TreeNode) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if node is None:
                return 0

            gain_on_left = max(
                get_max_gain(node.left), 0
            )  # Read the part important observations
            gain_on_right = max(
                get_max_gain(node.right), 0
            )  # Read the part important observations

            current_max_path = (
                node.val + gain_on_left + gain_on_right
            )  # Read first three images of going down the recursion stack
            max_path = max(
                max_path, current_max_path
            )  # Read first three images of going down the recursion stack

            return node.val + max(
                gain_on_left, gain_on_right
            )  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path

    def dfs(self, node: TreeNode):
        if node is None:
            return 0

        # only add positive contributions
        leftST_sum = max(0, self.dfs(node.left))
        rightST_sum = max(0, self.dfs(node.right))

        # check if cumulative sum at current node > global max sum so far
        # this evaluates a candidate path
        self.max_sum = max(self.max_sum, leftST_sum + rightST_sum + node.val)

        # add to the current node ONLY one of the children contributions
        # in order to maintain the constraint of considering only paths
        # if not, we would be exploring explore the whole tree - against problem definition
        return max(leftST_sum, rightST_sum) + node.val

    # Iterative solution using DFS
    def maxPathSumIterative(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")
        self.dfs(root)
        return self.max_sum

    # Solution using Kadane's Algorithm
    def maxPathSumUsingKadaneAlgorithm(self, root: TreeNode) -> int:
        def backtracking(node: TreeNode) -> tuple:
            if node is None:
                return float("-inf"), 0
            left_so_far, left_ending_here = backtracking(node.left)
            right_so_far, right_ending_here = backtracking(node.right)
            max_so_far = max(
                left_so_far,
                right_so_far,
                node.val + left_ending_here + right_ending_here,
            )
            max_ending_here = max(
                0, node.val + max(left_ending_here, right_ending_here)
            )
            return max_so_far, max_ending_here

        return backtracking(root)[0]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxPathSumRecursive(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(6, s.maxPathSumRecursive(root))
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(42, s.maxPathSumRecursive(root))
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.left.left = TreeNode(-10)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        self.assertEqual(16, s.maxPathSumRecursive(root))
        root = TreeNode(-15)
        root.left = TreeNode(5)
        root.left.left = TreeNode(-8)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(2)
        root.left.left.right = TreeNode(-3)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(9)
        root.right.right.right = TreeNode(0)
        root.right.right.left = TreeNode(4)
        root.right.right.right = TreeNode(-1)
        root.right.right.right.left = TreeNode(10)
        self.assertEqual(27, s.maxPathSumRecursive(root))

    def test_maxPathSumIterative(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(6, s.maxPathSumIterative(root))
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(42, s.maxPathSumIterative(root))
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.left.left = TreeNode(-10)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        self.assertEqual(16, s.maxPathSumIterative(root))
        root = TreeNode(-15)
        root.left = TreeNode(5)
        root.left.left = TreeNode(-8)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(2)
        root.left.left.right = TreeNode(-3)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(9)
        root.right.right.right = TreeNode(0)
        root.right.right.left = TreeNode(4)
        root.right.right.right = TreeNode(-1)
        root.right.right.right.left = TreeNode(10)
        self.assertEqual(27, s.maxPathSumIterative(root))

    def test_maxPathSumUsingKadaneAlgorithm(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(6, s.maxPathSumUsingKadaneAlgorithm(root))
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(42, s.maxPathSumUsingKadaneAlgorithm(root))
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.left.left = TreeNode(-10)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        self.assertEqual(16, s.maxPathSumUsingKadaneAlgorithm(root))
        root = TreeNode(-15)
        root.left = TreeNode(5)
        root.left.left = TreeNode(-8)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(2)
        root.left.left.right = TreeNode(-3)
        root.right = TreeNode(6)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(9)
        root.right.right.right = TreeNode(0)
        root.right.right.left = TreeNode(4)
        root.right.right.right = TreeNode(-1)
        root.right.right.right.left = TreeNode(10)
        self.assertEqual(27, s.maxPathSumUsingKadaneAlgorithm(root))


if __name__ == "__main__":
    unittest.main()
