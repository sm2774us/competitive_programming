#
# Time : O(N); Space: O(LogN)
# @tag : Tree and BST ; BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 101: Symmetric Tree
#
# Description:
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# Follow up: Solve it both recursively and iteratively.
#
# **************************************************************************
# Source: https://leetcode.com/problems/symmetric-tree/ (Leetcode - Problem 101 - Symmetric Tree)
#         https://practice.geeksforgeeks.org/problems/symmetric-tree/1 (GeeksForGeeks - Symmetric Tree)
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
    def dfs(self, l: TreeNode, r: TreeNode) -> bool:
        if l and r:
            return (
                l.val == r.val
                and self.dfs(l.left, r.right)
                and self.dfs(l.right, r.left)
            )
        return l == r

    # Recursive solution using BFS
    def isSymmetricRecursive(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    # Iterative solution using deque - takes advantage of deque O(1) popleft operation
    def isSymmetricIterative(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            left, right = q.popleft(), q.popleft()

            if not left and not right:
                continue
            elif (not left or not right) or (left.val != right.val):
                return False

            q += [left.left, right.right, left.right, right.left]

        return True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isSymmetricRecursive(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertEqual(True, s.isSymmetricRecursive(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(False, s.isSymmetricRecursive(root))

    def test_isSymmetricIterative(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertEqual(True, s.isSymmetricIterative(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(False, s.isSymmetricIterative(root))


if __name__ == "__main__":
    unittest.main()
