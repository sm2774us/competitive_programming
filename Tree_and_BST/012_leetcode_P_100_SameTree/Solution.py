#
# Time : O(N); Space: O(N)
# @tag : Stack and Queue ; BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 100: Same Tree
#
# Description:
#
# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false
#
# **************************************************************************
# Source: https://leetcode.com/problems/same-tree/ (Leetcode - Problem 100 - Same Tree)
#         https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1 (GeeksForGeeks - Determine if Two Trees are Identical)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
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

    # BFS with pre-order traversal - Iterative Solution
    def isSameTreeBFS(self, p: TreeNode, q: TreeNode) -> bool:
        def bfs(node: TreeNode):
            cur_queue = [node] if node else [None]
            while cur_queue:
                next_queue = []
                for cur_node in cur_queue:
                    if cur_node:
                        yield cur_node.val
                        next_queue.append(cur_node.left)
                        next_queue.append(cur_node.right)
                    else:
                        yield None
                cur_queue = next_queue

        # -----------------------------------------------------
        iterator_p = bfs(p)
        iterator_q = bfs(q)

        while True:
            try:
                if next(iterator_p) != next(iterator_q):
                    return False
            except StopIteration:
                break

        return True

    # DFS with pre-order traversal - Recursive Solution
    def isSameTreeDFSRecursive(self, p, q):
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q

    # DFS with pre-order traversal - Recursive Solution - One Liner
    def isSameTreeDFSRecursiveOneLiner(self, p, q):
        return (
            p
            and q
            and p.val == q.val
            and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right)))
            or p is q
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isSameTree(self) -> None:
        s = Solution()
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        self.assertEqual(True, s.isSameTree(p, q))
        self.assertEqual(True, s.isSameTreeBFS(p, q))
        self.assertEqual(True, s.isSameTreeDFSRecursive(p, q))
        self.assertEqual(True, s.isSameTreeDFSRecursiveOneLiner(p, q))

        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(False, s.isSameTree(p, q))
        self.assertEqual(False, s.isSameTreeBFS(p, q))
        self.assertEqual(False, s.isSameTreeDFSRecursive(p, q))
        self.assertEqual(False, s.isSameTreeDFSRecursiveOneLiner(p, q))

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(False, s.isSameTree(p, q))
        self.assertEqual(False, s.isSameTreeBFS(p, q))
        self.assertEqual(False, s.isSameTreeDFSRecursive(p, q))
        self.assertEqual(False, s.isSameTreeDFSRecursiveOneLiner(p, q))


if __name__ == "__main__":
    unittest.main()
