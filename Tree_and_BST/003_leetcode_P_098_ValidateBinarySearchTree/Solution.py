#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 98: Validate Binary Search Tree
#
# Description:
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# **************************************************************************
# Source: https://leetcode.com/problems/validate-binary-search-tree/ (Leetcode - Problem 98 - Validate Binary Search Tree)
#         https://practice.geeksforgeeks.org/problems/check-for-bst/1 (GeeksForGeeks - Check for BST)
#
#
from typing import List
from collections import deque

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        rst = []
        stack = [(root, False)]

        while stack:
            cur = stack.pop()
            if not cur[0]:
                continue

            if cur[1]:
                if rst and cur[0].val <= rst[-1]:
                    return False
                rst.append(cur[0].val)
            else:
                stack.append((cur[0].right, False))
                stack.append((cur[0], True))
                stack.append((cur[0].left, False))

        return True

    def isValidBSTRecursive(
        self, root: TreeNode, min: float = float("-inf"), max: float = float("inf")
    ) -> bool:
        if not root:
            return True
        return (
            min <= root.val < max
            and self.isValidBSTRecursive(root.left, min, root.val)
            and self.isValidBSTRecursive(root.right, root.val + 1, max)
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isValidBST(self) -> None:
        s = Solution()
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(True, s.isValidBST(root))
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertEqual(False, s.isValidBST(root))

    def test_isValidBSTRecursive(self) -> None:
        s = Solution()
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(True, s.isValidBSTRecursive(root))
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertEqual(False, s.isValidBSTRecursive(root))


if __name__ == "__main__":
    unittest.main()
