#
# Time : O(NlogN); Space: O(N)
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 987: Vertical Order Traversal of a Binary Tree
#
# Description:
#
# Given a binary tree, return the vertical order traversal of its nodes values.
#
# For each node at position (X, Y), its left and right children respectively will be at
# positions (X-1, Y-1) and (X+1, Y-1).
#
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
#
#
# Examples:
# Refer to Problem_Description.md.
#
# **************************************************************************
# Source: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/ (Leetcode - Problem 987 - Vertical Order Traversal of a Binary Tree)
#         https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1 (GeeksForGeeks - Vertical Traversal of Binary Tree)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md.
#
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


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        verticals = collections.defaultdict(list)
        queue = collections.deque([[root, 0, 0]])  # node, x, y

        while queue:
            for i in range(len(queue)):
                node, x, y = queue.popleft()
                verticals[x].append((y, node.val))

                if node.left:
                    queue.append(
                        [node.left, x - 1, y + 1]
                    )  # going down = +1 (instead of -1 like in the description)
                if node.right:
                    queue.append([node.right, x + 1, y + 1])

        output = []
        for x in sorted(verticals.keys()):
            column = [i[1] for i in sorted(verticals[x])]
            output.append(column)

        return output


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_verticalTraversal(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual([[9], [3, 15], [20], [7]], s.verticalTraversal(root))
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual([[4], [2], [1, 5, 6], [3], [7]], s.verticalTraversal(root))


if __name__ == "__main__":
    unittest.main()
