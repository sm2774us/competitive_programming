#
# Time : O(N) ; Space: O(1)
# @tag : Tree and BST ; Recursion ;
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 114: Flatten Binary Tree to Linked List
#
# Description:
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
# **************************************************************************
# Source: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/ (Leetcode - Problem 114 - Flatten Binary Tree to Linked List)
#         https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/ (GeeksForGeeks - Flatten a binary tree into linked list)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
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
    # Iterative - take advantage of deque O(1) popleft operation
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque()
        queue.append(p)
        queue.append(q)

        while queue:
            p, q = queue.popleft(), queue.popleft()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)

        return True

    def flatten(self, root: TreeNode) -> None:
        """
        Input: root node of binary tree
        Output: convert binary tree to right-skewed linked list
        """

        # record of node of previous traversal
        previous_traversal = None

        def helper(node):
            if node:
                # DFS travesal to next level

                helper(node.right)
                helper(node.left)

                # flattern binary tree to right skewed linked list

                nonlocal previous_traversal
                node.right = previous_traversal
                node.left = None
                previous_traversal = node

        # ---------------------

        helper(root)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_flatten(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        expected = TreeNode(1)
        expected.right = TreeNode(2)
        expected.right.right = TreeNode(3)
        expected.right.right.right = TreeNode(4)
        expected.right.right.right.right = TreeNode(5)
        expected.right.right.right.right.right = TreeNode(6)
        s.flatten(root)
        self.assertEqual(True, s.isSameTree(expected, root))


if __name__ == "__main__":
    unittest.main()
