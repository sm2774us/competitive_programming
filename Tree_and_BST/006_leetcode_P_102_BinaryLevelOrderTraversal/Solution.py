#
# Time : O(N); Space: O(N)
# @tag : Stack and Queue ; BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 102: Binary Tree Level Order Traversal
#
# Description:
#
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-level-order-traversal/ (Leetcode - Problem 102 - Binary Tree Level Order Traversal)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Breadth First Search
#
#   * Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
#   * When we start the while loop, we have L1 nodes in the queue.
#   * for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
#   * Time complexity: O(N). Space Complexity: O(N)
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_levelOrder(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual([[3], [9, 20], [15, 7]], s.levelOrder(root))


if __name__ == "__main__":
    unittest.main()
