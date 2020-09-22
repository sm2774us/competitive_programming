#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 199: Binary Tree Right Side View
#
# Description:
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-right-side-view/ (Leetcode - Problem 199 - Binary Tree Right Side View)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# **************************************************************************
# Recursive Method
# **************************************************************************
# The left view contains all nodes that are first nodes in their levels.
# A simple solution is to do level order traversal and print the first node in every level.
#
# The problem can also be solved using simple recursive traversal.
# We can keep track of the level of a node by passing a parameter to all recursive calls.
# The idea is to keep track of the maximum level also.
# Whenever we see a node whose level is more than maximum level so far, we print the node because
# this is the first node in its level (Note that we traverse the left subtree before right subtree).
#
# **************************************************************************
# Iterative Method
# **************************************************************************
# The idea is to do level order traversal of the Tree using a queue and print the first node at each level.
#
# While doing level order traversal, after traversing all node at each level,
# push a NULL delimiter to mark the end of the current level.
# So, do the level order traversal of the tree. Print the first node at each level in the tree
# and push the children of all nodes at each level in the queue until a NULL delimiter is encountered.
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        rs = []
        # q = []
        # could use list and pop(0) instead of deque and popleft() but less efficient
        q = deque()
        q.append(root)
        if not root:
            return
        while q:
            lvlsize = len(q)
            while lvlsize > 0:
                cur = q.popleft()
                lvlsize -= 1
                if lvlsize == 0:
                    rs.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return rs


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_rightSideView(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        self.assertEqual([1, 3, 4], s.rightSideView(root))


if __name__ == "__main__":
    unittest.main()
