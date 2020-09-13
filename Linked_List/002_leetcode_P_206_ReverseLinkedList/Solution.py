#
# Time : O(N)   => The two solutions are both O(N), we visit every node in the Linked List just once
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 206: Reverse Linked List
#
# Description:
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# **************************************************************************
# Source: https://leetcode.com/problems/reverse-linked-list/ (Leetcode - Problem 206 - Reverse Linked List)
#         https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1 (GeeksForGeeks - Reverse a linked list)
#
# Youtube Explanation: https://www.youtube.com/watch?v=XDO6I8jxHtA
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# 1) Iterative Approach
# **************************************************************************
# To reverse a linked list, we actually reverse the direction of every next pointer.
# For example, we reverse a linked list 1->2->3->4->5 by changing every -> to <- and
# get the result as 1<-2<-3<-4<-5. And we need to return the pointer to 5 instead of to 1.
# To solve it efficiently, we can do it in one loop iteration or recursion.
#
# For iteration, we create a ListNode rev to keep track of what we have reversed otherwise we would lose it.
# Then we iterate linked list and make head point to the current node.
# We change a -> to <- by calling head.next = rev, update rev by calling rev = head,
# move to next node by calling head = head.next. To save a temporary variable,
# we could assign these variables in one line, but head.next and rev should be updated before
# head is updated otherwise direction would not be reversed and rev would keep pointing to itself.
#
# For example, 1->2->3, 1 is current node head, what we have reversed rev is None, 2 is head.next.
# Calling head.next = rev leads to None<-1.
# Calling head = head.next concurrently to make head pointing to 2->3.
# Updating rev as 1->None. And in next iteration, we will change 2->3 to 1<-2 and keep changing -> to <- so on so forth.
#
# **************************************************************************
# 1) Recursive Approach
# **************************************************************************
# For recursion, the bottom layer is the end of the origin linked list so we just return it.
# For the outer layer, for example, 4->5, we change -> to <- by calling head.next.next = head where head points at 4
# and head.next points at 5. node, which is self.reverseList(head.next) also points at 5 or 5->4,
# is what we need to return in this layer. So when we keep returning to the outer layer,
# reversed linked list keep growing (a -> b becomes a <- b as head.next.next = head)
#
# Another example, in some recursion, you have linked list 1->2->3->null, reversed linked list 5->4->3->null.
# head points at 2, head.next points at 3, 5->4->3->null is what you have reversed and stored in
# node=reversedList(head.next). Now you need to place 2 to the end of 5->4->3. So you call head.next.next = head
# or 3.next = 2, and head.next = null or 2.next = null. Then you have original linked list 1->2->null,
# and reversed linked list (head node 5 stored in node) 5->4->3->2->null.
# Then you return these to outer recursion.
#
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


class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            head.next, rev, head = rev, head, head.next
        return rev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node, head.next.next, head.next = (
            self.reverseListRecursive(head.next),
            head,
            None,
        )
        return node


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_reverseListIterative(self) -> None:
        listNode = ListNode()
        head = listNode.initList([1, 2, 3, 4, 5, None])
        s = Solution()
        solution = listNode.initList([None, 5, 4, 3, 2, 1])
        reversedList = s.reverseListIterative(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )

        head = listNode.initList([1, 2, 3, 4, 5, 6])
        s = Solution()
        solution = listNode.initList([6, 5, 4, 3, 2, 1])
        reversedList = s.reverseListIterative(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )

        head = listNode.initList([2, 7, 8, 9, 10])
        s = Solution()
        solution = listNode.initList([10, 9, 8, 7, 2])
        reversedList = s.reverseListIterative(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )

    def test_reverseListRecursive(self) -> None:
        listNode = ListNode()
        head = listNode.initList([1, 2, 3, 4, 5, None])
        s = Solution()
        solution = listNode.initList([None, 5, 4, 3, 2, 1])
        reversedList = s.reverseListRecursive(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )

        head = listNode.initList([1, 2, 3, 4, 5, 6])
        s = Solution()
        solution = listNode.initList([6, 5, 4, 3, 2, 1])
        reversedList = s.reverseListRecursive(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )

        head = listNode.initList([2, 7, 8, 9, 10])
        s = Solution()
        solution = listNode.initList([10, 9, 8, 7, 2])
        reversedList = s.reverseListRecursive(head)
        self.assertEqual(
            solution, reversedList, "Should return the reversal of the linked list"
        )


if __name__ == "__main__":
    unittest.main()
