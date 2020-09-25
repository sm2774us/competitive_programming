#
# Time : O(N); Space: O(N)
# @tag : Stack and Queue ; Euler Tour ; Range Minimum Query Problem
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem - 236: Lowest Common Ancestor of a Binary Tree
#
# Description:
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."
#
# Examples:
# Refer to Problem_Description.md.
#
# **************************************************************************
# Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ (Leetcode - Problem 236 - Lowest Common Ancestor of a Binary Tree)
#         https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1 (GeeksForGeeks - Lowest Common Ancestor in a BST)
#
# References: https://en.wikipedia.org/wiki/Euler_tour_technique [ Euler Tour ]
#             https://en.wikipedia.org/wiki/Range_minimum_query [ Range Minimum Query ]
#             https://en.wikipedia.org/wiki/Lowest_common_ancestor [ Lowest Common Ancestor ]
# **************************************************************************
# Solution Explanation
# **************************************************************************
# First convert LCA problem to RMQ (range minimum query) problem by generating Euler tour.
# LCA must occur in between the two query nodes in the Euler tour, and LCA has the smallest level (distance to root).
# Therefore LCA problem is reduced to finding smallest element in an array with specified range.
#
# Reference: Bender, Michael A., and Martin Farach-Colton. "The LCA problem revisited." Latin American Symposium on Theoretical Informatics. Springer Berlin Heidelberg, 2000.
# https://www3.cs.stonybrook.edu/~bender/newpub/BenderFa00-lca.pdf
#
# **************************************************************************
# Detailed Explanation:
# **************************************************************************
#
# LCA algorithm using RMQ works as follows:
#
# Suppose we wanted to find LCA(u, v)
#
# 1) Perform euler tour on tree T starting at the root. This could be done using DFS and recording the
#    visited node in pre order. Also at each step of the euler tour record the depth of the current node
#    (depth of the node within the given tree). Store this tour and depth in an array.
#
# 2) Now create a segment tree of the depth array.
#
# 3) LCA is the node with minimum depth that was encountered while performing a walk from u to v (or from v to u).
#    WLOG assume u was visited first during the euler tour, than RMQ on the range (first time visting u,
#    first time visiting v) on the depth array gives us the LCA(u, v)
#
# * RMQ query to segment tree should return a node corresponding to the minimum depth and not the value.
#
# More detail (with graphics) can be found on the Topcoder tutorial link below:
# http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=lowestCommonAncestor#Lowest%2BCommon%2BAncestor%2B(LCA)
#
# **************************************************************************
# Complexity Analysis:
# **************************************************************************
# Runtime:
#
# Suppose n = |V| and m = |E|
#
# (1) takes O(n), since runtime of DFS is O(n+m), and since for tree m = n-1
# (2) takes O(n), since initialization of segment tree takes O(n)
# * Note: You might think it is O(n log(n)), since it performs n updates, and each update takes O(log(n)),
#         but it is in fact O(n) since the total number of vertex in segment tree is n + n/2 + n/4 + ... = 2n.
# (3) takes O(log(n)) for the RMQ query
#
# So overall runtime of this algorithm is O(n). If we were to perform multiple query,
# DFS and segment tree initialization could be done before hand in O(n) time,
# and each LCA query will take O(log(n)) time.
#
import math

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Breaking this down: first, we check that the second tree is not None; then, we check that our values match;
    # then we recursively call __eq__ for both the left and right subtrees. Since __eq__
    # has a sensible default definition for None, we don't need to do any other edge case checking for those.
    # one major shortcoming is that since it relies on recursion, it is possible to cause a stack overflow
    # if you pass it a binary tree of too much height
    # (specifically, ~1000 nodes tall for CPython).
    # def __eq__(self, other):
    #     return (other is not None and self.value == other.value and
    #             self.left == other.left and self.right == other.right)

    # To avoid this, you'll need to manually simulate recursion using a stack;
    # this gets a lot messier, but doesn't suffer from stack overflow:
    # def __eq__(self, other):
    #     from collections import deque
    #
    #     pairs = deque()
    #     pairs.append((self, other))
    #
    #     while len(pairs) > 0:
    #         s, o = pairs.pop()
    #         if (s is None) != (o is None) or s.val != o.val:
    #             return False
    #         else:
    #             pairs.append((s.left, o.left))
    #             pairs.append((s.right, o.right))
    #
    #     return True

    def treeToList(self, root):
        from collections import deque

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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        euler = []
        levels = []
        first_occurence = {}

        def euler_tour(node, lvl):
            if not node:
                return
            nonlocal euler
            nonlocal levels
            nonlocal first_occurence
            euler.append(node)
            levels.append(lvl)
            first_occurence[node.val] = len(euler) - 1
            if node.left:
                euler_tour(node.left, lvl + 1)
                euler.append(node)
                levels.append(lvl)
            if node.right:
                euler_tour(node.right, lvl + 1)
                euler.append(node)
                levels.append(lvl)
            return

        euler_tour(root, 0)

        i_len = len(euler)
        j_len = math.floor(math.log2(i_len)) + 1
        sparse_matrix = [[None] * j_len for _ in range(i_len)]

        def gen_sparse_matrix(levels, sparse_matrix, i_len, j_len):
            for i in range(i_len):
                sparse_matrix[i][0] = i
            for j in range(1, j_len):
                for i in range(i_len - 2 ** j + 1):
                    if (
                        levels[sparse_matrix[i][j - 1]]
                        < levels[sparse_matrix[i + 2 ** (j - 1)][j - 1]]
                    ):
                        sparse_matrix[i][j] = sparse_matrix[i][j - 1]
                    else:
                        sparse_matrix[i][j] = sparse_matrix[i + 2 ** (j - 1)][j - 1]

        gen_sparse_matrix(levels, sparse_matrix, i_len, j_len)

        def lca(p, q, euler, sparse_matrix, first_occurence):
            p_occur = first_occurence[p.val]
            q_occur = first_occurence[q.val]
            if p_occur > q_occur:
                p_occur, q_occur = q_occur, p_occur
            l = q_occur - p_occur + 1
            k = math.floor(math.log2(l))
            if (
                levels[sparse_matrix[p_occur][k]]
                < levels[sparse_matrix[p_occur + l - 2 ** k][k]]
            ):
                return euler[sparse_matrix[p_occur][k]]
            else:
                return euler[sparse_matrix[p_occur + l - 2 ** k][k]]

        return lca(p, q, euler, sparse_matrix, first_occurence)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_connect(self) -> None:
        s = Solution()
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        # self.assertEqual(TreeNode(3), s.lowestCommonAncestor(root, TreeNode(5), TreeNode(1)))
        # self.assertEqual(TreeNode(5), s.lowestCommonAncestor(root, TreeNode(5), TreeNode(4)))
        self.assertEqual(root, s.lowestCommonAncestor(root, root.left, root.right))
        self.assertEqual(
            root.left, s.lowestCommonAncestor(root, root.left, root.left.right.right)
        )


if __name__ == "__main__":
    unittest.main()
