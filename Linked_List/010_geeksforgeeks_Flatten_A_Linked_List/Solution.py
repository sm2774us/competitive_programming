#
# Time : O(N*M); Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given a Linked List of size N, where every node represents a linked list and contains two pointers of its type:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
#
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.
#
# Example 1:
#
# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     |
# 7    20    22    35
# |           |     |
# 8          50    40
# |                 |
# 30               45
# Output:  5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50.
#
# Note: | represents the bottom pointer.
# Your Task:
# You need to complete the function flatten() that takes head of the list as parameter and returns the root of flattened list. The printing is done by the driver code.
#
# Note: Try to solve the problem without using any extra space.
#
# Expected Time Complexity: O(N*M)
# Expected Auxiliary Space: O(1)
#
# Constraints:
# 0 <= N <= 50
# 1 <= Mi <= 20
# 1 <= Element of linked list <= 103
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1 ( Flattening a Linked List )
#
# Solution Hint: https://www.techiedelight.com/flatten-linked-list/#
#
# The way to think about the solution visually:
# **************************************************************************
#          +-----------------+  ===> Merging and Sorting
# 5 -> 10 ----> 19 -> 28     | /
# |     |  |     |     |     |/
# 7    20  |    22    35     |
# |        |     |     |     |
# 8        |    50    40     |
# |        |           |     |
# 30       |          45     |
#          +-----------------+
#
#     +------------------+  ===> Merging and Sorting
# 5 --|--> 10 ---> 19    | /
# |   |    |        |    |/
# 7   |    20      22    |
# |   |             |    |
# 8   |            28    |
# |   |             |    |
# 30  |            35    |
#     |             |    |
#     |            40    |
#     |             |    |
#     |            45    |
#     |             |    |
#     |            50    |
#     +------------------+
#
#     +----------+  ===> Merging and Sorting
# 5 --|--> 10    | /
# |   |    |     |/
# 7   |    19    |
# |   |    |     |
# 8   |    20    |
# |   |    |     |
# 30  |    22    |
#     |    |     |
#     |    28    |
#     |    |     |
#     |    35    |
#     |    |     |
#     |    40    |
#     |    |     |
#     |    45    |
#     |    |     |
#     |    50    |
#     +----------+
#
#     +----------+  ===> Merging and Sorting
#     |    5     | /
#     |    |     |/
#     |    7     |
#     |    |     |
#     |    8     |
#     |    |     |
#     |    10    |
#     |    |     |
#     |    19    |
#     |    |     |
#     |    20    |
#     |    |     |
#     |    22    |
#     |    |     |
#     |    28    |
#     |    |     |
#     |    30    |
#     |    |     |
#     |    35    |
#     |    |     |
#     |    40    |
#     |    |     |
#     |    45    |
#     |    |     |
#     |    50    |
#     +----------+
#
#
from typing import List
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down

    def __eq__(self, other):
        if not self.equal(other):
            # print("List1 != List2 where")
            # print("List1:")
            # print(str(self))
            # print("List2:")
            # print(str(other))
            # print("\n")
            return False
        else:
            return True

    def equal(self, other):
        if other is not None:
            return (
                self.val == other.val
                and self.next == other.next
                and self.down == other.down
            )
        else:
            return False

    def __repr__(self):
        lst = []
        p = self
        while p:
            lst.append(str(p.val))
            p = p.down

        return "List: [{}].".format(",".join(lst))

    def initVerticalList(self, nums):
        if not nums:
            return None
        head = None
        current = None

        for n in nums:
            if not head:
                head = ListNode(n)
                current = head
            else:
                node = ListNode(n)
                current.down = node
                current = node
        return head

    def initList(self, nums):
        if not nums:
            return None
        head = None
        current = None

        for n in nums:
            if not head:
                head = ListNode(n)
                current = head
            else:
                node = ListNode(n)
                current.next = node
                current = node
        return head

    def printList(self, head):
        string = ""
        if not head:
            return string
        while head.down:
            if head.val is None:
                string += "%s->" % str(head.val)
            else:
                string += "%d->" % head.val
            head = head.down
        if head.val is None:
            string += "%s->" % str(head.val)
        else:
            string += "%d" % head.val
        return string

    def linkedListToList(self, head):
        if not head:
            return []

        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.next
        return sll_list

    def verticalLinkedListToList(self, head):
        if not head:
            return []

        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.down
        return sll_list


class Solution:
    # Takes two lists sorted in increasing order, and merge their nodes
    # together to make one big sorted list which is returned
    def sortedMerge(self, a: ListNode, b: ListNode) -> ListNode:
        # Base cases
        if a is None:
            return b

        elif b is None:
            return a

        # Pick either a or b, and recur
        if a.val <= b.val:
            result = a
            result.down = self.sortedMerge(a.down, b)

        else:
            result = b
            result.down = self.sortedMerge(a, b.down)

        return result

    # Iterative function to flatten and sort a given list
    def flatten(self, head: ListNode) -> ListNode:
        # base case: an empty list
        if head is None:
            return head

        # Merge this list with the list on right side
        sorted = self.sortedMerge(head, self.flatten(head.next))

        # set next link to None after flattening
        head.next = None

        return sorted

    # # Python program to get transpose
    # # elements of two dimension list
    # def transpose(self, listA: List[int]) -> List[int]:
    #     # star operator will first
    #     # unpack the values of 2D list
    #     # and then zip function will
    #     # pack them again in opposite manner
    #     transposedList = listA(map(listA, zip(*listA)))
    #     return transposedList


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_flatten(self) -> None:
        listNode = ListNode()
        s = Solution()
        llistA = listNode.initVerticalList([1, 4, 6, 8])
        llistB = listNode.initVerticalList([2, 3, 7])
        llistC = listNode.initVerticalList([5, 9])
        llistD = listNode.initVerticalList([10, 11, 12])
        head = llistA
        head.next = llistB
        head.next.next = llistC
        head.next.next.next = llistD
        self.assertEqual(
            listNode.initVerticalList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
            s.flatten(head),
            "Should flatten the linked list",
        )
        self.assertEqual(
            listNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
            listNode.initList(listNode.verticalLinkedListToList(s.flatten(head))),
            "Should flatten the linked list",
        )

        llistA = listNode.initVerticalList([5, 7, 8, 30])
        llistB = listNode.initVerticalList([10, 20])
        llistC = listNode.initVerticalList([19, 22, 50])
        llistD = listNode.initVerticalList([28, 35, 40, 45])
        head = llistA
        head.next = llistB
        head.next.next = llistC
        head.next.next.next = llistD
        self.assertEqual(
            listNode.initVerticalList(
                [5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]
            ),
            s.flatten(head),
            "Should flatten the linked list",
        )
        self.assertEqual(
            listNode.initList([5, 7, 8, 10, 19, 20, 22, 28, 30, 35, 40, 45, 50]),
            listNode.initList(listNode.verticalLinkedListToList(s.flatten(head))),
            "Should flatten the linked list",
        )


if __name__ == "__main__":
    unittest.main()
