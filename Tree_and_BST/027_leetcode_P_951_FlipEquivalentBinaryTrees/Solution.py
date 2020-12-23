#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 951: Flip Equivalent Binary Trees
#
# Description: Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/flip-equivalent-binary-trees/ (LeetCode - Problem 951 - Flip Equivalent Binary Trees)
# **************************************************************************
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


# Complexity Analysis:
# ---------------------------------------------------------
# Update:
# For some time, I forgot the following constraint and changed the comlexity from O(n) to O(n ^ 2):
# Each value in each tree will be a unique integer in the range [0, 99]
#
# The follows are correct only without the above condition.
# Complexity analysis corrected from O(n) to O(n ^ 2).
# Analysis:
#
# In worst case, the recursion corresponds to a perfect quaternary (means 4-nary) tree, which has 4 ^ d = N ^ 2 nodes, and we have to traverse all nodes. d = logN is the depth of the binary tree.
#
# One worst case for input:
# two perfect binary trees: root1 & root2.
#
# Root1's nodes are all 0s;
# Root2's nodes are all 0s, with the exception that left and right bottoms are both 1s.
# Time & Space: O(n ^ 2).
# Thanks correction from @heruslu @coder_coder @Everestsky007
#
# Q & A:
#
# Q1:
# why it's N^2 and how it corresponds to a 4-nary tree? why it was initially considered O(N)?
# A1:
# Yes, because the return statement has 4 recursive calls.
#
# The problem states Each value in each tree will be a unique integer in the range [0, 99], hence we have the following deduction:
#
# ir1.left.val == r2.left.val and r1.left.val == r2.right.val,
#
# at most 1 of the 2 relations is true; otherwise r2.left.val == r2.right.val, this contradicts the above problem constraint.
# Therefore, at least 1 out of flipEquiv(r1.left, r2.left) and flipEquiv(r1.left, r2.right) will terminate; Similiarly, at least 1 out of flipEquiv(r1.right, r2.right) andflipEquiv(r1.right, r2.leftt) will terminate.
#
# Obviously at most 2 out of the 4 recursive calls could go all the way down to the bottom.
#
# That is why the time is O(N).
#
# Without the aforementioned constraint, all of the 4 recursive calls could expand the 4-nary tree to the bottom and result time O(N ^ 2).
#
# Q2: In iterative Python code, why there needs to be a comparison of node1.left == node2.left?
# A2: It is a short form of node1.left == node2.left == None.
#
class Solution(object):

    # Solution_1: Recursive Solution - DFS
    #
    # 1. If at least one of the two root nodes is null, are they equal? if yes, true; if no, false;
    # 2. otherwise, neither node is null; if the values of the two nodes are:
    #       2a) NOT equal, return false;
    #       2b) equal, compare their children recursively.
    #
    def flipEquiv_solution_1_recursive_DFS(
        self, root1: TreeNode, root2: TreeNode
    ) -> bool:
        if not root1 or not root2:
            return root1 == root2 == None
        return root1.val == root2.val and (
            self.flipEquiv_solution_1_recursive_DFS(root1.left, root2.left)
            and self.flipEquiv_solution_1_recursive_DFS(root1.right, root2.right)
            or self.flipEquiv_solution_1_recursive_DFS(root1.left, root2.right)
            and self.flipEquiv_solution_1_recursive_DFS(root1.right, root2.left)
        )

    # Solution_2 : Iterative - BFS
    #
    def flipEquiv_solution_2_iterative_BFS(
        self, root1: TreeNode, root2: TreeNode
    ) -> bool:
        dq1, dq2 = map(collections.deque, ([root1], [root2]))
        while dq1 and dq2:
            node1, node2 = dq1.popleft(), dq2.popleft()
            if node1 == node2 == None:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            if (
                node1.left == node2.left == None
                or node1.left
                and node2.left
                and node1.left.val == node2.left.val
            ):
                dq1.extend([node1.left, node1.right])
            else:
                dq1.extend([node1.right, node1.left])
            dq2.extend([node2.left, node2.right])
        return not dq1 and not dq2

    # Solution_3 : Iterative - DFS
    #
    def flipEquiv_solution_3_iterative_DFS(
        self, root1: TreeNode, root2: TreeNode
    ) -> bool:
        stk1, stk2 = [root1], [root2]
        while stk1 and stk2:
            node1, node2 = stk1.pop(), stk2.pop()
            if node1 == node2 == None:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            if (
                node1.left == node2.left == None
                or node1.left
                and node2.left
                and node1.left.val == node2.left.val
            ):
                stk1.extend([node1.left, node1.right])
            else:
                stk1.extend([node1.right, node1.left])
            stk2.extend([node2.left, node2.right])
        return not stk1 and not stk2


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_flipEquiv(self) -> None:
        sol = Solution()
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        root1.right.left = TreeNode(6)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(8)

        root2 = TreeNode(1)
        root2.left = TreeNode(3)
        root2.right = TreeNode(2)
        root2.left.right = TreeNode(6)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(5)
        root2.right.right.left = TreeNode(8)
        root2.right.right.right = TreeNode(7)

        self.assertEqual(True, sol.flipEquiv_solution_1_recursive_DFS(root1, root2))
        self.assertEqual(True, sol.flipEquiv_solution_2_iterative_BFS(root1, root2))
        self.assertEqual(True, sol.flipEquiv_solution_3_iterative_DFS(root1, root2))

        self.assertEqual(
            True, sol.flipEquiv_solution_1_recursive_DFS(TreeNode(), TreeNode())
        )
        self.assertEqual(
            True, sol.flipEquiv_solution_2_iterative_BFS(TreeNode(), TreeNode())
        )
        self.assertEqual(
            True, sol.flipEquiv_solution_3_iterative_DFS(TreeNode(), TreeNode())
        )

        self.assertEqual(
            False, sol.flipEquiv_solution_1_recursive_DFS(TreeNode(), TreeNode(1))
        )
        self.assertEqual(
            False, sol.flipEquiv_solution_2_iterative_BFS(TreeNode(), TreeNode(1))
        )
        self.assertEqual(
            False, sol.flipEquiv_solution_3_iterative_DFS(TreeNode(), TreeNode(1))
        )

        root1 = TreeNode(0)
        root1.right = TreeNode(1)
        self.assertEqual(
            False, sol.flipEquiv_solution_1_recursive_DFS(root1, TreeNode(1))
        )
        self.assertEqual(
            False, sol.flipEquiv_solution_2_iterative_BFS(root1, TreeNode(1))
        )
        self.assertEqual(
            False, sol.flipEquiv_solution_3_iterative_DFS(root1, TreeNode(1))
        )


# main
if __name__ == "__main__":
    unittest.main()
