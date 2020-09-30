#
# Time : O(N) ; Space: O(1)
# @tag : Tree and BST ; Recursion ;
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 449: Serialize and Deserialize BST
#
# Description:
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note:
#   * Do not use class member/global/static variables to store states.
#   * Your serialize and deserialize algorithms should be stateless.
#
#
# Example 1:
#
# Given the following tree [8,5,10,1,7,null,12]:
#
#        8
#     /    \
#    5       10
#  /  \        \
# 1    7        12
# Input: root = [8,5,10,1,7,null,12]
# Output: [8,5,1,7,10,12]
#
# **************************************************************************
# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ (Leetcode - Problem 449 - Serialize and Deserialize BST)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
#
import sys
from collections import deque

import unittest

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

    def serialize(self, root: TreeNode) -> str:
        """O(N) TS"""

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def traversal(node):
            if not node:
                return []

            return [str(node.val)] + traversal(node.left) + traversal(node.right)

        return ",".join(traversal(root))
        # serializedStr = ",".join(traversal(root))
        # serializedStr = serializedStr.rstrip(',')
        # return serializedStr

    def deserialize(self, data: str) -> TreeNode:
        """O(N) TS"""

        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(",")[::-1] if data else []

        def helper(minn, maxx):
            node_val = int(tree[-1]) if tree else None
            if node_val is None or not (
                minn < node_val <= maxx
            ):  # is_None because node_val can be 0
                return None
            tree.pop()

            node = TreeNode(node_val)
            node.left = helper(minn, node_val)
            node.right = helper(node_val, maxx)
            return node

        return helper(INT_MIN, INT_MAX)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_serialize(self) -> None:
        s = Solution()
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(2)
        root.left.left.right = TreeNode(3)
        root.right = TreeNode(7)
        root.right.right = TreeNode(9)
        root.right.right.right = TreeNode(10)
        self.assertEqual("5,4,2,3,7,9,10", s.serialize(root))
        root = TreeNode(None)
        self.assertEqual("None", s.serialize(root))
        root = TreeNode(1)
        self.assertEqual("1", s.serialize(root))
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual("1,2", s.serialize(root))

    def test_deserialize(self) -> None:
        s = Solution()
        expected = TreeNode(5)
        expected.left = TreeNode(4)
        expected.left.left = TreeNode(2)
        expected.left.left.right = TreeNode(3)
        expected.right = TreeNode(7)
        expected.right.right = TreeNode(9)
        expected.right.right.right = TreeNode(10)
        actual = s.deserialize("5,4,2,3,7,9,10")
        # actual = s.deserialize("5,2,3,4,7,9,10")
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = None
        actual = s.deserialize("")
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = TreeNode(1)
        actual = s.deserialize("1")
        self.assertEqual(True, s.isSameTree(expected, actual))
        expected = TreeNode(1)
        expected.right = TreeNode(2)
        actual = s.deserialize("1,2")
        self.assertEqual(True, s.isSameTree(expected, actual))


if __name__ == "__main__":
    unittest.main()
