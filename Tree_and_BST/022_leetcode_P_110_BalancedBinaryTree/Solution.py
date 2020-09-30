#
# Time : O(N) ; Space: O(1)
# @tag : Tree and BST ; Recursion ;
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 110: Balanced Binary Tree
#
# Description:
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
#
# **************************************************************************
# Source: https://leetcode.com/problems/balanced-binary-tree/ (Leetcode - Problem 110 - Balanced Binary Tree)
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
    def isBalancedIterative(self, root: TreeNode) -> bool:
        stack = [(0, root)]
        depth = {None: 0}
        while stack:
            seen, node = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                if abs(depth[node.left] - depth[node.right]) > 1:
                    return False
                depth[node] = max(depth[node.left], depth[node.right]) + 1
        return True

    def isBalancedRecursiveWithoutExtraVariable(self, root: TreeNode) -> bool:
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1

    def isBalancedRecursiveWithSwitchVariable(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.switch = True

        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.switch = False
            return max(left, right) + 1

        dfs(root)
        return self.switch


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isBalancedIterative(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(True, s.isBalancedIterative(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertEqual(False, s.isBalancedIterative(root))

    def test_isBalancedRecursiveWithoutExtraVariable(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(True, s.isBalancedRecursiveWithoutExtraVariable(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertEqual(False, s.isBalancedRecursiveWithoutExtraVariable(root))

    def test_isBalancedRecursiveWithSwitchVariable(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(True, s.isBalancedRecursiveWithSwitchVariable(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertEqual(False, s.isBalancedRecursiveWithSwitchVariable(root))


if __name__ == "__main__":
    unittest.main()
