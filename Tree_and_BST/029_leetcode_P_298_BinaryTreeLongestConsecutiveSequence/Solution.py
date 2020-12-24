#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 298: Binary Tree Longest Consecutive Sequence
#
# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# For example,
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.
#
# **************************************************************************
# Source: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/ (LeetCode - Problem 298 - Binary Tree Longest Consecutive Sequence)
#         https://practice.geeksforgeeks.org/problems/longest-consecutive-sequence-in-binary-tree/1 (GeeksForGeeks - Longest consecutive sequence in Binary tree)
# **************************************************************************
# Reference:
#               Recursive Solution : https://github.com/criszhou/LeetCode-Python/blob/master/298.%20Binary%20Tree%20Longest%20Consecutive%20Sequence.py
#               Iterative Solution : https://codereview.stackexchange.com/questions/200916/binary-tree-longest-consecutive-sequence
#                                       [ https://codereview.stackexchange.com/a/200930 ]
#
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def longestConsecutiveHelper(self, root):
        """
        return a pair (longest, longestFromRoot)
        where longest is the longest in this tree, and longestFromRoot requires the path to start from root
        """
        if not root:
            return (0, 0)

        longest, longestFromRoot = 1, 1

        if root.left:
            leftLongest, leftLongestFromRoot = self.longestConsecutiveHelper(root.left)
            if root.left.val == root.val + 1:
                longestFromRoot = max(longestFromRoot, leftLongestFromRoot + 1)
            longest = max(longest, longestFromRoot, leftLongest)

        if root.right:
            rightLongest, rightLongestFromRoot = self.longestConsecutiveHelper(
                root.right
            )
            if root.right.val == root.val + 1:
                longestFromRoot = max(longestFromRoot, rightLongestFromRoot + 1)
            longest = max(longest, longestFromRoot, rightLongest)

        return longest, longestFromRoot

    # Solution_1: Recursive Solution
    #
    # We can solve above problem recursively.
    # 1) At each node we need information of its parent node, if current node has value one more than
    #    its parent node then it makes a consecutive path,
    #    at each node we will compare node’s value with its parent value and
    #    update the longest consecutive path accordingly.
    # 2) For getting the value of parent node, we will pass the (node_value + 1)
    #    as an argument to the recursive method and compare the node value
    #    with this argument value,
    #    if satisfied, update the current length of consecutive path
    #    otherwise reinitialize current path length by 1.
    #
    def longestConsecutive_solution_1_recursive(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        longest, longestFromRoot = self.longestConsecutiveHelper(root)
        return longest

    # Solution_2 : Iterative Solution
    #
    def invertTree_solution_2_iterative(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return 0
        longest_sequence = 0
        nodes = dict()
        nodes[root] = 1
        while True:
            new_nodes = dict()
            for node, length in nodes.items():
                for subnode in (node.left, node.right):
                    if subnode:
                        if subnode.val - node.val == 1:
                            new_nodes[subnode] = length + 1
                        else:
                            new_nodes[subnode] = 1
                longest_sequence = max(longest_sequence, length)
            nodes = new_nodes
            if not nodes:
                break
        return longest_sequence


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_invertTree(self) -> None:
        sol = Solution()
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)

        self.assertEqual(3, sol.longestConsecutive_solution_1_recursive(root))
        self.assertEqual(3, sol.longestConsecutive_solution_1_recursive(root))

        root = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.left.left = TreeNode(1)

        self.assertEqual(2, sol.longestConsecutive_solution_1_recursive(root))
        self.assertEqual(2, sol.longestConsecutive_solution_1_recursive(root))


# main
if __name__ == "__main__":
    unittest.main()
