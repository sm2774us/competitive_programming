#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks for Geeks - Left View of Binary Tree
#
# Description:
#
# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.
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
# You just have to complete the function leftView() that prints the left view. The newline is automatically appended by the driver code.
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
from typing import List
from collections import deque

import unittest

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Utility function to print the left
    # view of the binary tree
    def leftViewUntill(self, root: Node) -> List[int]:
        rs = []
        if root == None:
            return None

        # append root
        rs.append(root)

        # Delimiter
        rs.append(None)

        while len(rs):
            temp = rs[0]

            if temp:

                # Prints first node of each level
                # print(temp.val, end=" ")

                # append children of all nodes
                # at current level
                while rs[0] != None:
                    temp = rs[0]

                    # If left child is present
                    # append into queue
                    if temp.left:
                        rs.append(temp.left)

                        # If right child is present
                    # append into queue
                    if temp.right:
                        rs.append(temp.right)

                    # Pop the current node
                    rs.pop(0)

                # append delimiter
                # for the next level
                rs.append(None)

            # Pop the delimiter of
            # the previous level
            rs.pop(0)
            return rs

    # Function to print the leftView
    # of Binary Tree
    def leftView(self, root: Node) -> List[int]:
        # return self.leftViewUntill(root)
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
                try:
                    cur = q.popleft()
                except IndexError:
                    cur = None
                if cur is None:
                    break
                lvlsize -= 1
                if lvlsize == 0:
                    rs.append(cur.val)
                q.append(cur.left if cur.left else cur.right)
        return rs


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_leftView(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.left.left.right = Node(8)
        root.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(7)

        self.assertEqual([1, 2, 4, 8], s.leftView(root))

        root = Node(1)
        root.left = Node(3)
        root.right = Node(2)

        self.assertEqual([1, 3], s.leftView(root))

        root = Node(10)
        root.left = Node(20)
        root.left.left = Node(40)
        root.left.right = Node(60)
        root.right = Node(30)

        self.assertEqual([10, 20, 40], s.leftView(root))


if __name__ == "__main__":
    unittest.main()
