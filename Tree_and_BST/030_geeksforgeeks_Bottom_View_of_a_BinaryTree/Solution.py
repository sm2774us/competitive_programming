#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks for Geeks - Bottom View of Binary Tree
#
# Description: Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1 (Geeks for Geeks - Bottom View of Binary Tree)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
#
from typing import List
from collections import deque

import unittest

# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    @classmethod
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


class Solution(object):
    # Recursive function to do a pre-order traversal of the tree and fill the dictionary
    # Here node has 'dist' horizontal distance from the root of the
    # tree and level represent level of the node
    def printBottom(self, root, dist, level, dict):

        # base case: empty tree
        if root is None:
            return

        # if current level is more than or equal to maximum level seen so far
        # for the same horizontal distance or horizontal distance is seen for
        # the first time, update the dictionary
        if dist not in dict or level >= dict[dist][1]:
            # update value and level for current distance
            dict[dist] = (root.key, level)

        # recur for left subtree by decreasing horizontal distance and
        # increasing level by 1
        self.printBottom(root.left, dist - 1, level + 1, dict)

        # recur for right subtree by increasing both level and
        # horizontal distance by 1
        self.printBottom(root.right, dist + 1, level + 1, dict)

    # Function to print the bottom view of given binary tree
    def printBottomView(self, root):

        # create a dictionary where
        # key -> relative horizontal distance of the node from root node and
        # value -> pair containing node's value and its level
        dict = {}

        # do pre-order traversal of the tree and fill the dictionary
        self.printBottom(root, 0, 0, dict)

        # traverse the dictionary in sorted order of their keys and
        # print the bottom view
        ans = []
        for key in sorted(dict.keys()):
            ans.append(dict.get(key)[0])
            # print(dict.get(key)[0], end=' ')
        return ans


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_bottomView(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(3)
        root.right = Node(2)
        self.assertEqual([3, 1, 2], s.printBottomView(root))

        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.left.left = Node(40)
        root.left.right = Node(60)
        self.assertEqual([40, 20, 60, 30], s.printBottomView(root))


if __name__ == "__main__":
    unittest.main()
