#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks for Geeks - Count Leaves in Binary Tree
#
# Description:
#
# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function getLeafCount(), which accepts root of the tree as argument.
#
# Left view of following tree is 1 2 4 8.
#
#           1
#        /     \
#      2        3
#    /     \    /    \
#   4     5   6    7
#    \
#      8
#
# Example 1:
#
# Input:
#    1
#  /  \
# 3    2
# Output: 1 3
#
# Example 2:
#
#           10
#        /     \
#      20       30
#    /     \
#   0      60
#
# Output: 10 20 40
#
# Your Task:
# You just have to complete the function getLeafCount() that prints the left view. The newline is automatically appended by the driver code.
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(Height of the Tree).
#
# Constraints:
# 1 <= Number of nodes <= 100
# 1 <= Data of a node <= 1000
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/0 (GeeksForGeeks - Left View of Binary Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
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
#
# Python program to count leaf nodes in Binary Tree
#
from typing import List
from collections import deque

import unittest

# A Binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Function to print the getLeafCount
    # of Binary Tree
    def getLeafCount(self, root: Node) -> List[int]:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return self.getLeafCount(root.left) + self.getLeafCount(root.right)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getLeafCount(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(10)
        root.right = Node(39)
        root.left.left = Node(5)
        self.assertEqual(2, s.getLeafCount(root))
        root = Node(3)
        root.left = Node(4)
        root.right = Node(2)
        self.assertEqual(2, s.getLeafCount(root))
        root = Node(4)
        root.left = Node(8)
        root.left.left = Node(7)
        root.left.left.left = Node(3)
        root.right = Node(10)
        root.right.left = Node(5)
        root.right.right = Node(1)
        self.assertEqual(3, s.getLeafCount(root))


if __name__ == "__main__":
    unittest.main()
