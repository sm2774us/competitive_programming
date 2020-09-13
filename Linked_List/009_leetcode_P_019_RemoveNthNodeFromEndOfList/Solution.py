#
# Time : O(N)   ; Only one traversal of the loop is needed.
# Space: O(1)   ; There is no space required.
# @tag : Linked List, Two Pointers
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 19: Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#
# **************************************************************************
# Source: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/ (LeetCode - Problem 19 - Remove Nth Node From End of List)
#         https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1 (GeeksForGeeks - Nth node from end of linked list)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# The idea is to use two pointers, fast (Q) and slow (P).
#
# Move the fast pointer up first, N nodes.
#
# Then move P and Q together.
#
# Finally, p.next will point to the node to remove so we can remove it with p.next = p.next.next.
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


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next or not head:
            return None

        listNode = ListNode()
        llistSize = listNode.length(head)
        if n > llistSize:
            return None

        p = head
        q = head

        for _ in range(n):
            if not q.next:
                return head.next
            q = q.next

        if not q:
            return p.next

        while q.next:
            q = q.next
            p = p.next

        p.next = p.next.next

        return head

    def removeAndReturnNthFromEnd(self, head: ListNode, n: int) -> int:
        if not head.next or not head:
            return None

        listNode = ListNode()
        llistSize = listNode.length(head)
        if n > llistSize:
            return None

        p = head
        q = head

        for _ in range(n):
            if not q.next:
                return head.next
            q = q.next

        if not q:
            return p.next.val

        while q.next:
            q = q.next
            p = p.next

        return p.next.val


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_removeNthFromEnd(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, n, solution in (
            [listNode.initList([1, 2, 3, 4, 5]), 2, listNode.initList([1, 2, 3, 5])],
            [
                listNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                2,
                listNode.initList([1, 2, 3, 4, 5, 6, 7, 9]),
            ],
            [listNode.initList([10, 5, 100, 5]), 5, None],
        ):
            self.assertEqual(
                solution,
                s.removeNthFromEnd(head, n),
                "Should remove the n-th node from the end of list and return its head",
            )

    def test_removeAndReturnNthFromEnd(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, n, solution in (
            [listNode.initList([1, 2, 3, 4, 5]), 2, 4],
            [listNode.initList([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2, 8],
            [listNode.initList([10, 5, 100, 5]), 5, None],
        ):
            self.assertEqual(
                solution,
                s.removeAndReturnNthFromEnd(head, n),
                "Should remove the n-th node from the end of list and return its head",
            )


if __name__ == "__main__":
    unittest.main()
