#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks for Geeks - Mirror Tree
#
# Description: Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/mirror-tree/1 (Geeks for Geeks - Mirror Tree)
# **************************************************************************
#
from typing import List
from collections import deque

import unittest


# Python3 program to convert a binary
# tree to its mirror

# Utility function to create a new
# tree node
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
    """ Change a tree so that the roles of the
        left and right pointers are swapped at
        every node.

    So the tree...
            4
           / \
          2   5
         / \
        1   3

    is changed to...
        4
        / \
       5   2
          / \
         3   1
    """

    # Algorithm Description:
    #
    # (1)  Call Mirror for left-subtree    i.e., Mirror(left-subtree)
    # (2)  Call Mirror for right-subtree  i.e., Mirror(right-subtree)
    # (3)  Swap left and right subtrees.
    #           temp = left-subtree
    #           left-subtree = right-subtree
    #           right-subtree = temp
    #
    def mirror_solution_1_recursive(self, node):
        if node == None:
            return
        else:

            temp = node

            """ do the subtrees """
            self.mirror_solution_1_recursive(node.left)
            self.mirror_solution_1_recursive(node.right)

            """ swap the pointers in this node """
            temp = node.left
            node.left = node.right
            node.right = temp

    # Algorithm Description:
    #
    # The idea is to do queue based level order traversal.
    # While doing traversal, swap left and right children of every node.
    #
    def mirror_solution_2_iterative(self, root):

        if root == None:
            return

        q = []
        q.append(root)

        # Do BFS. While doing BFS, keep swapping
        # left and right children
        while len(q):

            # pop top node from queue
            curr = q[0]
            q.pop(0)

            # swap left child with right child
            curr.left, curr.right = curr.right, curr.left

            # append left and right children
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    """ Helper function to print Inorder traversal."""

    def inOrder(self, node):
        if node == None:
            return

        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mirror_recursive(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        """ Print inorder traversal of 
                the input tree """
        # print("Inorder traversal of the",
        #       "constructed tree is")
        # s.inOrder(root)

        """ Convert tree to its mirror """
        s.mirror_solution_1_recursive(root)
        treeNodesAsList = Node.treeToList(root)
        self.assertEqual([[1], [3, 2]], treeNodesAsList)

        """ Print inorder traversal of  
            the mirror tree """
        # print("\nInorder traversal of",
        #       "the mirror treeis ")
        # s.inOrder(root)

        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.left.left = Node(40)
        root.left.right = Node(60)

        """ Print inorder traversal of 
                the input tree """
        # print("Inorder traversal of the",
        #       "constructed tree is")
        # s.inOrder(root)

        """ Convert tree to its mirror """
        s.mirror_solution_1_recursive(root)
        treeNodesAsList = Node.treeToList(root)
        self.assertEqual([[10], [30, 20], [60, 40]], treeNodesAsList)

    def test_mirror_iterative(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)

        """ Print inorder traversal of 
                the input tree """
        # print("Inorder traversal of the",
        #       "constructed tree is")
        # s.inOrder(root)

        """ Convert tree to its mirror """
        s.mirror_solution_2_iterative(root)
        treeNodesAsList = Node.treeToList(root)
        self.assertEqual([[1], [3, 2]], treeNodesAsList)

        """ Print inorder traversal of  
            the mirror tree """
        # print("\nInorder traversal of",
        #       "the mirror treeis ")
        # s.inOrder(root)

        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.left.left = Node(40)
        root.left.right = Node(60)

        """ Print inorder traversal of 
                the input tree """
        # print("Inorder traversal of the",
        #       "constructed tree is")
        # s.inOrder(root)

        """ Convert tree to its mirror """
        s.mirror_solution_2_iterative(root)
        treeNodesAsList = Node.treeToList(root)
        self.assertEqual([[10], [30, 20], [60, 40]], treeNodesAsList)


if __name__ == "__main__":
    unittest.main()
