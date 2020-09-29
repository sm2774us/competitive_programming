#
# Time : O(N); Space: O(N)
# @tag : Tree and BST ; BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 107: Binary Tree Level Order Traversal - TWO
#
# Description:
#
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/ (Leetcode - Problem 107 - Binary Tree Level Order Traversal II)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# This question is simply almost same as Binary Tree Level Order Traversal:
# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# ( refer to Tree_and_BST/006_leetcode_P_102_BinaryTreeLevelOrderTraversal/Solution.py )
#
# you just need to do [::-1] on ans
#
# class Solution(object):
#     def zigzagLevelOrder(self, root):
#         if not root: return []
#         q = deque([root])
#         ans = []
#         while q:
#             temp = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.left: q.append(node.left)
#                 if node.right: q.append(node.right)
#                 temp.append(node.val)
#             ans.append(temp)
#         return ans[::-1]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                temp.append(node.val)
            ans.append(temp)
        return ans[::-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_levelOrderBottom(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual([[15, 7], [9, 20], [3]], s.levelOrderBottom(root))


if __name__ == "__main__":
    unittest.main()
