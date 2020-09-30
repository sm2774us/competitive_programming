#
# Time : O(N) [ N = Number of nodes in the Binary Tree ] ; Space: O(1)
# @tag : Tree and BST ; Recursion ; Divide and Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 543: Diameter of Binary Tree
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
# Source: https://leetcode.com/problems/diameter-of-binary-tree/ (Leetcode - Problem 543 - Diameter of Binary Tree)
#         https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1 (GeeksForGeeks - Diameter of Binary Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
#   * Height of node [ See reference ] The height of a node is the number of edges on the longest downward path between that node and a leaf.
#     dfs function calculates the height of the node, i.e, the longest downward path between the node and a leaf.
#   * For a node, the length of longest path going through the node is the sum of left child's height plus right child's height.
#   * For each node in the binary tree, we calculate the length of the longest length going through the node, the maximum length
#     is the diameter of the binary tree according to the definition --The diameter of a binary tree is the length of the longest
#     path between any two nodes in a tree.
# **************************************************************************
#
# Reference:
# **************************************************************************
# Height of node - http://typeocaml.com/2014/11/26/height-depth-and-level-of-a-tree/
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
    def dfs(self, node: TreeNode) -> int:
        # base case:
        if node == None:
            return 0
        # recursive cases
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_diameterOfBinaryTree(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        self.assertEqual(3, s.diameterOfBinaryTree(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(2, s.diameterOfBinaryTree(root))
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(60)
        root.right = TreeNode(30)
        self.assertEqual(3, s.diameterOfBinaryTree(root))


if __name__ == "__main__":
    unittest.main()
