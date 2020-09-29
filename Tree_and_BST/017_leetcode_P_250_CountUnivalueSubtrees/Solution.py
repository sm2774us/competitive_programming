#
# Time : O(N) [ N = Number of nodes in the Binary Tree ] ; Space: O(1)
# @tag : Tree and BST ; Recursion ; Divide and Conquer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 250: Longest Univalue Path
#
# Description:
#
# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# For example:
# Given binary tree,
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# return 4.
#
# **************************************************************************
# Source: https://leetcode.com/problems/count-univalue-subtrees/ (Leetcode - Problem 250 - Count Univalue Subtrees)
#         https://www.geeksforgeeks.org/find-count-of-singly-subtrees/ (GeeksForGeeks - Find Count of Single Valued Subtrees)
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
    def countUnivalSubtreesHelper(self, root: TreeNode) -> (int, bool):
        """
        return a pair (univalTreeCount, isUnival)
        """
        if root is None:
            return (0, True)

        countL, isUnivalL = self.countUnivalSubtreesHelper(root.left)
        countR, isUnivalR = self.countUnivalSubtreesHelper(root.right)

        univalTreeCount = countL + countR

        isUnival = (
            isUnivalL
            and isUnivalR
            and (root.left is None or root.val == root.left.val)
            and (root.right is None or root.val == root.right.val)
        )

        if isUnival:
            univalTreeCount += 1

        return univalTreeCount, isUnival

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        univalTreeCount, isUnival = self.countUnivalSubtreesHelper(root)
        return univalTreeCount


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_countUnivalSubtrees(self) -> None:
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(5)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        self.assertEqual(4, s.countUnivalSubtrees(root))
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        self.assertEqual(5, s.countUnivalSubtrees(root))


if __name__ == "__main__":
    unittest.main()
