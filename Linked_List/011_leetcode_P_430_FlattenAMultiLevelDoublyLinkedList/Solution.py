#
# Time : O(N); Space: O(N)
# @tag : Linked List, DFS, Stack, Recursive
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# LeetCode - Problem 430: Flatten a Multilevel Doubly Linked List
#
# You are given a doubly linked list which in addition to the next and previous pointers, it could have a
# child pointer, which may or may not point to a separate doubly linked list. These child lists may have one
# or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
#
# Flatten the list so that all the nodes appear in a single-level, doubly linked list.
# You are given the head of the first level of the list.
#
# Example 1:
#
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
#
# The multilevel linked list in the input is as follows:
#
# +--------+         +--------+         +--------+         +--------+         +--------+         +--------+
# |    1   <--+  +--->    2   <--+  +--->    3   <--+  +--->    4   <--+  +--->    5   <--+  +--->    5   |
# +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+
# |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |
# +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+
# |  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |
# +--------+         +--------+         +--------+         +--------+         +--------+         +--------+
# | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |
# +--------+         +--------+         +----+---+         +--------+         +--------+         +--------+
#                                            |
#                                           \ /
#                                       +----+---+         +--------+         +--------+         +--------+
#                                       |    7   <--+  +--->    8   <--+  +--->    9   <--+  +--->   10   |
#                                       +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+
#                                       |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |
#                                       +--------+  |      +--------+  |      +--------+  |      +--------+
#                                       |  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |
#                                       +--------+         +--------+         +--------+         +--------+
#                                       | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |
#                                       +--------+         +---+----+         +--------+         +--------+
#                                                              |
#                                                             \ /
#                                                          +---+----+         +--------+
#                                                          |   11   <--+  +--->   12   |
#                                                          +--------+  |  |   +--------+
#                                                          |  NEXT  |--|--+   |  NEXT  |
#                                                          +--------+  |      +--------+
#                                                          |  PREV  |  +------+  PREV  |
#                                                          +--------+         +--------+
#                                                          | CHILD  |         | CHILD  |
#                                                          +--------+         +--------+
#
# After flattening the multilevel linked list it becomes:
#
# +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+
# |    1   <--+  +--->    2   <--+  +--->    3   <--+  +--->    7   <--+  +--->    8   <--+  +--->   11   <--+  +--->   12   <--+  +--->    9   <--+  +--->   10   <--+  +--->    4   <--+  +--->    5   <--+  +--->    6   |
# +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+  |  |   +--------+
# |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |--|--+   |  NEXT  |
# +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+  |      +--------+
# |  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |  +------+  PREV  |
# +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+
# | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |         | CHILD  |
# +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+         +--------+
#
# Example 2:
#
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
#
# The input multilevel linked list is as follows:
#
#   1---2---NULL
#   |
#   3---NULL
# Example 3:
#
# Input: head = []
# Output: []
#
# How multilevel linked list is represented in test case:
#
# We use the multilevel linked list from Example 1 above:
#
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
# The serialization of each level is as follows:
#
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
# To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
#
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
# Merging the serialization of each level and removing trailing nulls we obtain:
#
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#
#
# Constraints:
#
#   * Number of Nodes will not exceed 1000.
#   * 1 <= Node.val <= 10^5
#
# **************************************************************************
# Source: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/ (LeetCode - Problem 430 - Flatten a Multilevel Doubly Linked List)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Solution_1> Iterative Solution (using DFS and Stack)
# **************************************************************************
# In this problem we need to traverse our multilevel doubly linked list in some special order and rebuild
# some connections. We can consider our list as graph, which we now need to traverse.
# What graph traversal algorighms do we know? We should think about DFS (Depth-First Search) and BFS (Breadth-First Search).
# Why I choose DFS? Because we need to traverse as deep as possible, before we traverse neibhour nodes,
# and that is what DFS does exactly!
# When you realise this, problem becomes much more easier.
#
# So, algorighm look like:
#
#   1) Put head of our list to stack and start to traverse it: pop element from it and add two two elements instead:
#      its next and its child. The order is important: we first want to visit child and then next,
#      that is why we put child to the top of our stack.
#   2) Each time we pop last element from stack, I write it to auxilary order list.
#   3) Last step is to rebuild from our order list flattened doubly linked list.
#
# Complexity: Time complexity is O(n), where n is number of nodes in our list.
#             In this approach we also use O(n) additional space, because I keep order list.
#             This can be avoid, if we make connections on the fly, but it is a bit less intuitive in my opinion,
#             but of course, more optimal in space complexity.

# Solution_2> Recursive Solution
# **************************************************************************
# The key idea is to recursively flatten sublists, given the head. Flattening a child sublist and
# flattening a tail (contents of head.next) sublist is the same procedure.
# Once we've made the recursive calls, we need to assemble the list so that it's of the form
# head->[result of child flattening]->[result of tail flattening].
#
# Analysis
# If n is the number of nodes...
#
# The algorithm only requires O(1) extra space on the heap,
# BUT, in the worst case, it requires O(n) extra space on the stack, as we could need to put the entire list on.
#
# The amount of space required is dependent on:
#
#   1) The length of the longest stretch of nodes that only have child or next pointers.
#   2) The percentage of nodes which have both a child and a next pointer on them (the higher the percentage,
#      the better the performance, because we have nearer to a balanced tree structure).
#
# Due to this structure being equivalent to a (rather stringy in a lot of cases I suspect) binary tree,
# I'm pretty sure it's impossible to write an iterative algorithm that uses O(1) space.
# The stack/ queue you use to keep track of the work still to do could potentially grow to O(n) in the worst case,
# and like I said, this worst case is probably common.
#
# The time complexity is O(n) . We handle each node once. It is impossible to do better than O(n) time,
# because we need to actually check the child and next pointers of every node, otherwise
# we could miss some parts of the structure out!
#
import unittest

# Definition for a Node.
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __eq__(self, other):
        if not self.equal(other):
            return False
        else:
            return True

    def equal(self, other):
        if other is not None:
            return self.val == other.val and self.next == other.next
        else:
            return False

    def __repr__(self):
        lst = []
        p = self
        while p:
            lst.append(str(p.val))
            p = p.next

        return "List: [{}].".format(",".join(lst))

    def initList(self, nums):
        if not nums:
            return None
        head = None
        current = None

        for n in nums:
            if not head:
                head = Node(n)
                current = head
            else:
                node = Node(n)
                current.next = node
                current = node
        return head

    def linkedListToList(self, head):
        if not head:
            return []

        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.next
        return sll_list


class Solution:
    # Recursive solution to flatten doubly linked list
    def flattenRecursive(self, head: Node) -> Node:
        """
        :type head: Node
        :rtype: Node
        """
        self.recursively_flatten(head)
        return head

    # Takes the head of the list to be flattened, and returns the tail of the flattened list.
    def recursively_flatten(self, head: Node) -> Node:

        # Could happen if outer caller passes in an empty list.
        if head == None:
            return None

        # Base case - there is nothing left to flatten.
        if head.next == None and head.child == None:
            return head

        # Recursive case - we need to flatten the child and the tail.
        tail = head.next  # We need to store this as doing child first.
        current_end = head  # Where will we be attaching next?

        if head.child != None:
            child_end = self.recursively_flatten(head.child)
            self.link(current_end, head.child)
            current_end = child_end
            head.child = None

        if tail != None:
            tail_end = self.recursively_flatten(tail)
            self.link(current_end, tail)
            current_end = tail_end

        return current_end

    def link(self, node_1: Node, node_2: Node) -> None:
        node_1.next = node_2
        node_2.prev = node_1

    # Iterative function (using DFS and stack) to flatten doubly linked list
    def flattenIterative(self, head: Node) -> Node:
        if head:
            n_stack = []
            curr_node = head
            while curr_node:
                if curr_node.next:  # Push the "next" (if there's a "next") first.
                    n_stack.append(curr_node.next)
                if curr_node.child:  # Then push the "child" (if there's a child),
                    n_stack.append(
                        curr_node.child
                    )  # so that the "stack" would pop the immediate "child"
                    curr_node.child = None  # before any previous encountered "next".
                if n_stack:  # It will "recurse" down and bubble back up eventually.
                    next_node = (
                        n_stack.pop()
                    )  # Unless it has traversed through all the nodes,
                    curr_node.next = (
                        next_node
                    )  # there's always some node left in the stack to pop.
                    next_node.prev = (
                        curr_node
                    )  # Simply link up with whatever comes from the stack.
                curr_node = (
                    curr_node.next
                )  # To the next node, or None if there's no more
        return head


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_flatten(self) -> None:
        node = Node(None)
        node.next = Node(11)
        node.next.next = Node(12)
        node.next.next.next = Node(None)
        levelThree = node
        node = Node(None)
        node.next = Node(None)
        node.next.next = Node(7)
        node.next.next.next = Node(8)
        node.next.next.next.child = levelThree
        node.next.next.next.next = Node(9)
        node.next.next.next.next.next = Node(10)
        node.next.next.next.next.next.next = Node(None)
        levelTwo = node
        node = Node(1)
        node.next = Node(2)
        node.next.next = Node(3)
        node.next.next.child = levelTwo
        node.next.next.next = Node(4)
        node.next.next.next.next = Node(5)
        node.next.next.next.next.next = Node(6)
        node.next.next.next.next.next.next = Node(None)
        levelOne = node

        head = levelOne
        s = Solution()

        expected = Node(1)
        expected.next = Node(2)
        expected.next.next = Node(3)
        expected.next.next.next = Node(7)
        expected.next.next.next.next = Node(8)
        expected.next.next.next.next.next = Node(11)
        expected.next.next.next.next.next.next = Node(12)
        expected.next.next.next.next.next.next.next = Node(9)
        expected.next.next.next.next.next.next.next.next = Node(10)
        expected.next.next.next.next.next.next.next.next.next = Node(4)
        expected.next.next.next.next.next.next.next.next.next.next = Node(5)
        expected.next.next.next.next.next.next.next.next.next.next.next = Node(6)

        actual = s.flattenRecursive(head)
        actualList = Node().linkedListToList(actual)
        # actualList = [x for x in actualList if x is not None]
        actualList = list(filter(None.__ne__, actualList))
        actual = Node().initList(actualList)
        # print(actual)
        # print(expected)
        self.assertEqual(expected, actual, "Should flatten the doubly linked list")
        actual = s.flattenIterative(head)
        actualList = Node().linkedListToList(actual)
        # actualList = [x for x in actualList if x is not None]
        actualList = list(filter(None.__ne__, actualList))
        actual = Node().initList(actualList)
        # print(actual)
        # print(expected)
        self.assertEqual(expected, actual, "Should flatten the doubly linked list")

        node = Node(3)
        node.next = Node(None)
        levelTwo = node
        node = Node(1)
        node.next = Node(2)
        node.next.next = Node(None)
        levelOne = node
        levelOne.child = levelTwo

        head = levelOne
        s = Solution()

        expected = Node(1)
        expected.next = Node(3)
        expected.next.next = Node(2)

        actual = s.flattenRecursive(head)
        actualList = Node().linkedListToList(actual)
        # actualList = [x for x in actualList if x is not None]
        actualList = list(filter(None.__ne__, actualList))
        actual = Node().initList(actualList)
        # print(actual)
        # print(expected)
        self.assertEqual(expected, actual, "Should flatten the doubly linked list")
        actual = s.flattenIterative(head)
        actualList = Node().linkedListToList(actual)
        # actualList = [x for x in actualList if x is not None]
        actualList = list(filter(None.__ne__, actualList))
        actual = Node().initList(actualList)
        # print(actual)
        # print(expected)
        self.assertEqual(expected, actual, "Should flatten the doubly linked list")

        s = Solution()
        self.assertEqual(
            Node().initList([]),
            s.flattenRecursive(Node().initList([])),
            "Should flatten the doubly linked list",
        )
        self.assertEqual(
            Node().initList([]),
            s.flattenIterative(Node().initList([])),
            "Should flatten the doubly linked list",
        )


if __name__ == "__main__":
    unittest.main()
