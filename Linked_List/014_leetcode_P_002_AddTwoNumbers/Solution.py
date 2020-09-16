#
# Time : O(N+M)
# Space: O(N+M)
# @tag : Linked List, Two Pointers
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 2: Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# **************************************************************************
# Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ (LeetCode - Problem 19 - Remove Nth Node From End of List)
#         https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1 (GeeksForGeeks - Nth node from end of linked list)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# If you're struggling to visualize it, I think just drawing out a simple case would help. Say 1 + 1.
#
# Before loop:
# (0) -> None
#  ^
#  |
# root, n
#
# After 1 iteration of loop
#
# (0) -> (2) -> None
#  ^      ^
#  |      |
# root    n
# Now we want to return (2) -> None so we return root.next
#
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        while head.next:
            if head.val is None:
                string += "%s->" % str(head.val)
            else:
                string += "%d->" % head.val
            head = head.next
        if head.val is None:
            string += "%s->" % str(head.val)
        else:
            string += "%d" % head.val
        return string

    # length of linked list => recursive function
    def length(self, head):
        if head is None:
            return 0
        else:
            return 1 + self.length(head.next)

    # length of linked list => iterative function
    # def length(self, head):
    #     temp = head
    #     count = 0
    #     while(temp):
    #         count += 1
    #         temp = temp.next
    #     return count

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_addTwoNumbers(self) -> None:
        listNode = ListNode()
        s = Solution()
        for l1, l2, solution in (
            [
                listNode.initList([2, 4, 3]),
                listNode.initList([5, 6, 4]),
                listNode.initList([7, 0, 8]),
            ],
            [
                listNode.initList([5, 4]),
                listNode.initList([5, 4, 3]),
                listNode.initList([0, 9, 3]),
            ],
            [listNode.initList([3, 6]), ListNode(7), listNode.initList([0, 7])],
        ):
            self.assertEqual(
                solution,
                s.addTwoNumbers(l1, l2),
                "Should return the sum of the 2 linked lists",
            )


if __name__ == "__main__":
    unittest.main()
