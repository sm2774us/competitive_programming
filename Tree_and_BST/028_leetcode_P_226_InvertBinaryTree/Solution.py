#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 226: Invert Binary Tree
#
# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
#
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree
# on a whiteboard so f*** off.
#
# **************************************************************************
# Source: https://leetcode.com/problems/invert-binary-tree/ (LeetCode - Problem 226 - Invert Binary Tree)
# **************************************************************************
#
from typing import List
import collections

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def treeToList(self, root):
        if not root:
            return []

        q = collections.deque([root])
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


class Solution(object):

    # Solution_1: Recursive Solution
    #
    def invertTree_solution_1_recursive(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = (
            self.invertTree_solution_1_recursive(root.right),
            self.invertTree_solution_1_recursive(root.left),
        )
        return root

    # Solution_2a : BFS using stack
    #
    def invertTree_solution_2a_BFS_using_stack(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        level = [root] if root else []
        while level:
            q = []
            for node in level:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                node.left, node.right = node.right, node.left

            level = q

        return root

    # Solution_2b : BFS using deque
    #
    def invertTree_solution_2b_BFS_using_deque(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.extend([node.left, node.right])
        return root

    # Solution_3 : DFS
    #
    def invertTree_solution_3_DFS(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_invertTree(self) -> None:
        sol = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        invertedRoot = sol.invertTree_solution_1_recursive(root)
        invertedTreeNodesAsList = TreeNode.treeToList(invertedRoot)
        self.assertEqual([[4], [7, 2], [9, 6, 3, 1]], invertedTreeNodesAsList)

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        invertedRoot = sol.invertTree_solution_2a_BFS_using_stack(root)
        invertedTreeNodesAsList = TreeNode.treeToList(invertedRoot)
        self.assertEqual([[4], [7, 2], [9, 6, 3, 1]], invertedTreeNodesAsList)

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        invertedRoot = sol.invertTree_solution_2b_BFS_using_deque(root)
        invertedTreeNodesAsList = TreeNode.treeToList(invertedRoot)
        self.assertEqual([[4], [7, 2], [9, 6, 3, 1]], invertedTreeNodesAsList)

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        invertedRoot = sol.invertTree_solution_3_DFS(root)
        invertedTreeNodesAsList = TreeNode.treeToList(invertedRoot)
        self.assertEqual([[4], [7, 2], [9, 6, 3, 1]], invertedTreeNodesAsList)


# main
if __name__ == "__main__":
    unittest.main()
