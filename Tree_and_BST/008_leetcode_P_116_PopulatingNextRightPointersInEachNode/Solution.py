#
#
# Time : O(N); Space: O(N)
# @tag : Tree and BST ; BFS ( Breadth First Search )
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 116: Populating Next Right Pointers in Each Node
#
# Description:
#
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
# The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Follow up:
#
#   * You may only use constant extra space.
#   * Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
# Examples:
# Refer to Problem_Description.md.
#
# **************************************************************************
# Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ (Leetcode - Problem 116 - Populating Next Right Pointers in Each Node)
#         https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1 (GeeksForGeeks - Connect Nodes at Same Level)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
from collections import deque

import unittest

# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def treeToList(self, root):
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


class Solution:
    def connect(self, root: Node) -> Node:
        def helper(node: Node) -> Node:

            if node and node.left and node.right:

                # update next of left child
                node.left.next = node.right

                # update next of right child
                if node.next:
                    node.right.next = node.next.left

                helper(node.left)
                helper(node.right)

            return node

        # ----------------------------

        return helper(root)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_connect(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(7)
        solution = s.connect(root)
        node = Node()
        listOfConnectedNodes = node.treeToList(solution)
        self.assertEqual([[1], [2, 3], [4, 5, 6, 7]], listOfConnectedNodes)


if __name__ == "__main__":
    unittest.main()
