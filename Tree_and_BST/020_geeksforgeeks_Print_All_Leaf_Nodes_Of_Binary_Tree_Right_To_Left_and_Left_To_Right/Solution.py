#
# Time : O(N); Space: O(H), where H is height of the tree
# @tag : Tree and BST
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks for Geeks - Print All Leaf Nodes of a Binary Tree from left to right
#
# Description:
# Given a Binary Tree, the task is to print the leaf nodes from left to right. The nodes must be printed in the order they appear from left to right.
#
# Examples:
#
# Input :
#            1
#           /  \
#          2    3
#         / \  / \
#        4  5  6  7
#
# Output :4 5 6 7
#
# Input :
#             4
#            /  \
#           5    9
#          / \  / \
#         8   3 7  2
#        /         / \
#       12        6   1
#
# Output :12 3 7 6 1
#
# **************************************************************************
# Geeks for Geeks - Print All Leaf Nodes of a Binary Tree from right to left
#
# Description:
#
# Given a binary tree, the task is to print all the leaf nodes of the binary tree from right to left.
#
# Examples:
#
# Input :
#        1
#       /  \
#      2    3
#     / \  / \
#    4   5 6  7
# Output : 7 6 5 4
#
# Input :
#         1
#        /  \
#       2    3
#      / \    \
#     4   5    6
#         /   / \
#        7    8  9
# Output : 9 8 7 4
#
# **************************************************************************
# Source:   https://www.geeksforgeeks.org/print-leaf-nodes-left-right-binary-tree/ (GeeksForGeeks - Print all leaf nodes of a binary tree from left to right)
#           https://www.geeksforgeeks.org/print-all-leaf-nodes-of-a-binary-tree-from-right-to-left/ (GeeksForGeeks - Print all leaf nodes of a binary tree from right to left)
#
#
from typing import List

import unittest

# A Binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Approach:
    #   The idea to do this is similar to DFS algorithm [https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/].
    #   Below is step by step algorithm to do this:
    #
    # 1. Check if given node is null. If null, then return from the function.
    # 2. Check if it is a leaf node. If the node is a leaf node, then print its data.
    # 3. If in above step, node is not a leaf node then check if left and right childs of node exists.
    #    If yes then call function for left and right childs of the node recursively.
    def printLeafNodesLeftToRightRecursively(self, root: Node) -> List[int]:
        rs = []
        # If node is null, return
        if root is None:
            return None

        # If node is leaf node,
        # print its data
        if root.left is None and root.right is None:
            rs.append(root.val)
            return rs

        # If left child exists,
        # check for leaf recursively
        if root.left:
            rs += self.printLeafNodesLeftToRightRecursively(root.left)

        # If right child exists,
        # check for leaf recursively
        if root.right:
            rs += self.printLeafNodesLeftToRightRecursively(root.right)

        return list(rs)

    # Approach:
    #   The idea is to use two stacks, one to store all the nodes of the tree and the other one to store all the leaf nodes.
    #   We will pop the top node of the first stack. If the node has a left child, we will push it on top of the first stack,
    #   if it has a right child then we will push it onto the top of the first stack, but if the node is a leaf node then
    #   we will push it onto the top of the second stack. We will do it for all the nodes until we have traversed the
    #   Binary tree completely.
    #
    #   Then we will start popping the second stack and print all its elements until the stack gets empty.
    def printLeafNodesLeftToRightIterativelyUsingTwoStacks(
        self, root: Node
    ) -> List[int]:
        # Stack to store all the nodes
        # of tree
        s1 = []

        # Stack to store all the
        # leaf nodes
        s2 = []

        # Push the root node
        s1.append(root)

        while s1:
            curr = s1.pop()

            # If current node has a left child
            # push it onto the first stack
            if curr.left:
                s1.append(curr.left)

            # If current node has a right child
            # push it onto the first stack
            if curr.right:
                s1.append(curr.right)

            # If current node is a leaf node
            # push it onto the second stack
            elif not curr.left and not curr.right:
                s2.append(curr.val)

        # # Print all the leaf nodes
        # while len(s2) != 0:
        #     print(s2.pop().val, end=" ")
        return list(s2)[::-1]

    # Approach:
    #   The idea is to perform iterative postorder traversal using one stack and print the leaf nodes.
    #
    # Below is the implementation of the above approach:
    def printLeafNodesLeftToRightIterativelyUsingOneStack(
        self, root: Node
    ) -> List[int]:
        # stack to store the nodes
        s = []

        # Stack to store all the
        # leaf nodes
        rs = []

        while 1:
            # If p is not None then push
            # it on the stack
            if root:
                s.insert(0, root)
                root = root.left

            else:
                # If stack is empty then come out
                # of the loop
                if len(s) == 0:
                    break

                else:
                    # If the node on top of the stack has its
                    # right subtree as None then pop that node
                    # and print the node only if its left
                    # subtree is also None
                    if s[0].right == None:
                        root = s[0]
                        s.pop(0)

                        # Print the leaf node
                        if root.left == None:
                            # print(root.val, end=" ")
                            rs.append(root.val)

                    while root == s[0].right:
                        root = s[0]
                        s.pop(0)

                        if len(s) == 0:
                            break

                    # If stack is not empty then assign p as
                    # the stack's top node's right child
                    if len(s):
                        root = s[0].right

                    else:
                        root = None

        return list(rs)

    # Approach:
    #   The idea to do this is similar to DFS algorithm [https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/].
    #   Below is step by step algorithm to do this:
    #
    # 1. Check if given node is null. If null, then return from the function.
    # 2. Check if it is a leaf node. If the node is a leaf node, then print its data.
    # 3. If in above step, node is not a leaf node then check if right and left childs of node exists.
    #    If yes then call function for right and left childs of the node recursively.
    def printLeafNodesRightToLeftRecursively(self, root: Node) -> List[int]:
        rs = []
        # If node is null, return
        if root is None:
            return None

        # If node is leaf node,
        # print its data
        if root.left is None and root.right is None:
            rs.append(root.val)
            return rs

        # If right child exists,
        # check for leaf recursively
        if root.right:
            rs += self.printLeafNodesRightToLeftRecursively(root.right)

        # If left child exists,
        # check for leaf recursively
        if root.left:
            rs += self.printLeafNodesRightToLeftRecursively(root.left)

        return list(rs)

    # Approach:
    #   The idea is to use two stacks, one to store all the nodes of the tree and the other one to store all the leaf nodes.
    #   We will pop the top node of the first stack. If the node has a right child, we will push it on top of the first stack,
    #   if it has a left child then we will push it onto the top of the first stack, but if the node is a leaf node then
    #   we will push it onto the top of the second stack. We will do it for all the nodes until we have traversed the
    #   Binary tree completely.
    #
    #   Then we will start popping the second stack and print all its elements until the stack gets empty.
    def printLeafNodesRightToLeftIterativelyUsingTwoStacks(
        self, root: Node
    ) -> List[int]:
        # Stack to store all the nodes
        # of tree
        s1 = []

        # Stack to store all the
        # leaf nodes
        s2 = []

        # Push the root node
        s1.append(root)

        while s1:
            curr = s1.pop()

            # If current node has a right child
            # push it onto the first stack
            if curr.right:
                s1.append(curr.right)

            # If current node has a left child
            # push it onto the first stack
            if curr.left:
                s1.append(curr.left)

            # If current node is a leaf node
            # push it onto the second stack
            elif not curr.left and not curr.right:
                s2.append(curr.val)

        # # Print all the leaf nodes
        # while len(s2) != 0:
        #     print(s2.pop().val, end=" ")
        return list(s2)[::-1]

    # Approach:
    #   The idea is to perform iterative postorder traversal using one stack and print the leaf nodes.
    #
    # Below is the implementation of the above approach:
    def printLeafNodesRightToLeftIterativelyUsingOneStack(
        self, root: Node
    ) -> List[int]:
        # stack to store the nodes
        s = []

        # Stack to store all the
        # leaf nodes
        rs = []

        while 1:
            # If p is not None then push
            # it on the stack
            if root:
                s.append(root)
                root = root.right

            else:
                # If stack is empty then come out
                # of the loop
                if len(s) == 0:
                    break

                else:
                    # If the node on top of the stack has
                    # its left subtree as None then pop
                    # that node and print the node only
                    # if its right subtree is also None
                    if s[-1].left == None:
                        root = s[-1]
                        s.pop()

                        # Print the leaf node
                        if root.right == None:
                            # print(root.val, end=" ")
                            rs.append(root.val)

                    while root == s[-1].left:
                        root = s[-1]
                        s.pop()

                        if len(s) == 0:
                            break

                    # If stack is not empty then assign p as
                    # the stack's top node's right child
                    if len(s) > 0:
                        root = s[-1].left
                    else:
                        root = None

        return list(rs)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_printLeafNodesLeftToRightRecursively(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.right.right.left = Node(9)
        root.left.left.left.right = Node(10)
        #            1
        #        /      \
        #       2        3
        #      / \      /  \
        #     4   5    6    7
        #    /             /
        #   8             9
        #    \
        #    10
        #  [10,5,6,9]
        self.assertEqual([10, 5, 6, 9], s.printLeafNodesLeftToRightRecursively(root))

    def test_printLeafNodesLeftToRightIteratively(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.right.right.left = Node(9)
        root.left.left.left.right = Node(10)
        #            1
        #        /      \
        #       2        3
        #      / \      /  \
        #     4   5    6    7
        #    /             /
        #   8             9
        #    \
        #    10
        #  [10,5,6,9]
        self.assertEqual(
            [10, 5, 6, 9], s.printLeafNodesLeftToRightIterativelyUsingTwoStacks(root)
        )
        self.assertEqual(
            [10, 5, 6, 9], s.printLeafNodesLeftToRightIterativelyUsingOneStack(root)
        )

    def test_printLeafNodesRightToLeftRecursively(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.right.right.left = Node(9)
        root.left.left.left.right = Node(10)
        #            1
        #        /      \
        #       2        3
        #      / \      /  \
        #     4   5    6    7
        #    /             /
        #   8             9
        #    \
        #    10
        #  [9,6,5,10]
        self.assertEqual([9, 6, 5, 10], s.printLeafNodesRightToLeftRecursively(root))

    def test_printLeafNodesRightToLeftIteratively(self) -> None:
        s = Solution()
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.right.right.left = Node(9)
        root.left.left.left.right = Node(10)
        #            1
        #        /      \
        #       2        3
        #      / \      /  \
        #     4   5    6    7
        #    /             /
        #   8             9
        #    \
        #    10
        #  [9,6,5,10]
        self.assertEqual(
            [9, 6, 5, 10], s.printLeafNodesRightToLeftIterativelyUsingTwoStacks(root)
        )
        self.assertEqual(
            [9, 6, 5, 10], s.printLeafNodesRightToLeftIterativelyUsingOneStack(root)
        )


if __name__ == "__main__":
    unittest.main()
