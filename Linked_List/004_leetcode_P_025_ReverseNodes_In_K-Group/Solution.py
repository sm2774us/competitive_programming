#
# Time : O(N)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 25: Reverse Nodes in k-Group
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# **************************************************************************
# Source: https://leetcode.com/problems/reverse-nodes-in-k-group/ (Leetcode - Problem 25 - Reverse Nodes in k-Group)
#         https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1 (GeeksForGeeks - Reverse a Linked List in groups of given size)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# k = 3 for example:
#
# step 0: a -> b -> c -> (next k-group)
#
# step 1:      b -> c -> (next k-group)
#                   a ---^
#
# step 2:           c -> (next k-group)
#              b -> a ---^
#
# step 3:                (next k-group)
#         c -> b -> a ---^
#
# finish: c -> b -> a -> (next k-group)
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dummy = next_head = ListNode(None)
        dummy.next = head
        prev = curr = head

        while True:
            count = 0
            while curr and count < k:
                count += 1
                curr = curr.next
            if count == k:
                h, t = (
                    curr,
                    prev,
                )  # assign the first node of next k-group and the first node of current k-group to h(ead), t(ail)
                for _ in range(
                    k
                ):  # this is NOT a standard reversing by swapping arrows between adjacent nodes
                    tmp = (
                        t.next
                    )  # instead it poplefts a node successively (ref. Campanula's comment)
                    t.next = h
                    h = t
                    t = tmp
                    # one-line implementation: t.next, t, h = h, t.next, t
                next_head.next = (
                    h
                )  # connect the last node of the previous reversed k-group to the head of the current reversed k-group
                next_head = (
                    prev
                )  # prepare for connecting to the next to-be-reversed k-group
                prev = curr  # head of the next yet to be reversed k-group
            else:  # curr = None and count does not reach k i.e. list is exhausted
                return dummy.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # test cases for - Linked List rotation - right or clockwise - by k places
    def test_reverseKGroup(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, k, solution in (
            [listNode.initList([1, 2, 3, 4, 5]), 2, listNode.initList([2, 1, 4, 3, 5])],
            [listNode.initList([1, 2, 3, 4, 5]), 3, listNode.initList([3, 2, 1, 4, 5])],
            [
                listNode.initList([1, 2, 2, 4, 5, 6, 7, 8]),
                4,
                listNode.initList([4, 2, 2, 1, 8, 7, 6, 5]),
            ],
        ):
            self.assertEqual(
                solution,
                s.reverseKGroup(head, k),
                "Should reverse the nodes of a linked list k at a time and return its modified list",
            )


if __name__ == "__main__":
    unittest.main()
