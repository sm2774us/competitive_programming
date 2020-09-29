#
# Time : O(N) ; Space: O(1) [ If we don’t consider size of stack for function calls, otherwise, O(N) ]
# @tag : Tree and BST ; Level Order Traversal
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 104: Maximum Depth of Binary Tree
#
# Description:
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its depth = 3.
#
# **************************************************************************
# Source: https://leetcode.com/problems/maximum-depth-of-binary-tree/ (Leetcode - Problem 104 - Maximum Depth of Binary Tree)
#         https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1 (GeeksForGeeks - Height of Binary Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Recursive
# **************************************************************************
# The idea is we start from the top of the tree. Each node adds one level of depth to the subtree rooted at its left
# and right child. The maximum depth of the tree rooted at the current node is the maximum depth of the tree rooted
# at the left and right child + 1. The base case for our recursion is when we hit an empty child who does not
# contribute to increasing the depth of the tree and therefore it's maximum depth is 0.
#
# Let's take an example:
#
#          10
#        /    \
#      5      19
#            /
#          17
#
# We start the algorithm at node 10. Note the below is just pseudocode showcasing the expansion of the recursive call.
#
# # self. maxDepth(None) = 0 by definition
#
# self. maxDepth(10)
# max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10
# max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion
# max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0
# max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19
# max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0
# max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17
# max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0
# max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max
# max(1, 1 + 1) + 1 # Replacing the inner most max
# max(1, 2) + 1
# 2 + 1 # Replacing the inner most max
# 3
#
# **************************************************************************
# Iterative
# **************************************************************************
# Here the idea is to visit the node of the tree in level order (not BFS or DFS). You can have a look at the following articles to understand traversal and level order in particular:
#
# https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search_/_level_order
# https://www.geeksforgeeks.org/level-order-tree-traversal/
#
# To do a level order we use a queue (worklist of type deque in the code) and deque (from the nodes until we exhaust the nodes for a given level. We also enqueue the nodes for the next level. The queue is a First In First Out (FIFO) queue. To keep track of how many nodes for the current level are at the front of the queue we use a counter num_node_level which is populated at each iteration transition (i.e. num_node_level == 0). Each time we transition level we increment the levels counter. Initially, the worklist contains only the root of the tree and the number of nodes for that level is 1.
#
# Let's take an example:
#
#          10
#        /    \
#      5      19
#            /
#          17
# Please note the below is pseudocode illustrating the state of the algorithm at different iteration.
#
#
# # Initial state before the while
#
# worklist = [10]
# levels = 0
# num_node_level = 1
#
# # Iteration with node 10
# node = 10
# worklist.append(5)
# worklist.append(19)
# # State of worklist = [5, 19]
# num_node_level -= 1
# # num_node_level == 0 --> True
# levels += 1 # State levels = 1
# num_node_level = len(worklist) = 2
#
# # Iteration with node 5
# node = 5
# # We append nothing as the two child of 5 are empty
# # State of worklist = [19]
# num_node_level -= 1 # State num_node_level = 1
#
# # Iteration with node 19
# node = 19
# worklist.append(17)
# # We do not append the right child as it is empty
# # State of worklist = [17]
# num_node_level -= 1
# # num_node_level == 0 --> True
# levels += 1 # State levels = 2
# num_node_level = len(worklist) = 1
#
# # Iteration with node 17
# node  = 17
# # We append nothing as the two child of 5 are empty
# # State of worklist = [] -> Empty
# num_node_level -= 1
# # num_node_level == 0 --> True
# levels += 1 # State levels = 3
# num_node_level = len(worklist) = 0
#
# # No more nodes we exit the while loop
#
# return levels # levels = 3
#
# **************************************************************************
# Complexity Analysis
# **************************************************************************
# Time Complexity: O(N)
# **************************************************************************
# Let us see different corner cases.
# Complexity function T(n) — for all problem where tree traversal is involved — can be defined as:
# (n) = T(k) + T(n – k – 1) + c
#
# Where k is the number of nodes on one side of root and n-k-1 on the other side.
#
# Let’s do an analysis of boundary conditions
#
# Case 1: Skewed tree (One of the subtrees is empty and other subtree is non-empty )
#
# k is 0 in this case.
# T(n) = T(0) + T(n-1) + c
# T(n) = 2T(0) + T(n-2) + 2c
# T(n) = 3T(0) + T(n-3) + 3c
# T(n) = 4T(0) + T(n-4) + 4c
#
# …………………………………………
# ………………………………………….
# T(n) = (n-1)T(0) + T(1) + (n-1)c
# T(n) = nT(0) + (n)c
#
# Value of T(0) will be some constant say d. (traversing a empty tree will take some constants time)
#
# T(n) = n(c+d)
# T(n) = Θ(n) (Theta of n)
#
# Case 2: Both left and right subtrees have equal number of nodes.
#
# T(n) = 2T(|_n/2_|) + c
#
# This recursive function is in the standard form (T(n) = aT(n/b) + (-)(n) ) for master method http://en.wikipedia.org/wiki/Master_theorem. If we solve it by master method we get (-)(n)
#
# **************************************************************************
# Space Complexity/Auxiliary Space: O(1)
# **************************************************************************
# If we don’t consider size of stack for function calls then O(1) otherwise O(N).
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
    # Recursive solution
    def maxDepthRecursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        return (
            max(self.maxDepthRecursive(root.left), self.maxDepthRecursive(root.right))
            + 1
        )

    # Iterative solution using Level-Order Tree Traversal using the Python deque datastructure - takes advantage of deque O(1) popleft operation
    def maxDepthIterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        worklist = deque([root])
        num_node_level = 1
        levels = 0
        while worklist:
            node = worklist.popleft()
            if node.left:
                worklist.append(node.left)
            if node.right:
                worklist.append(node.right)
            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)

        return levels


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_maxDepthRecursive(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(3, s.maxDepthRecursive(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(2, s.maxDepthRecursive(root))
        root = TreeNode(2)
        root.right = TreeNode(1)
        root.right.left = TreeNode(3)
        self.assertEqual(3, s.maxDepthRecursive(root))

    def test_maxDepthIterative(self) -> None:
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(3, s.maxDepthIterative(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(2, s.maxDepthIterative(root))
        root = TreeNode(2)
        root.right = TreeNode(1)
        root.right.left = TreeNode(3)
        self.assertEqual(3, s.maxDepthIterative(root))


if __name__ == "__main__":
    unittest.main()
