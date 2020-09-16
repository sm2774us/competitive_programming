#
# Time : O(N)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.
#
# Example 1:
#
# Input:
# N = 8
# value[] = {1,2,2,1,2,0,2,2}
# Output: 0 1 1 2 2 2 2 2
# Explanation: All the 0s are segregated
# to the left end of the linked list,
# 2s to the right end of the list, and
# 1s in between.
# Example 2:
#
# Input:
# N = 4
# value[] = {2,2,0,1}
# Output: 0 1 2 2
# Explanation: After arranging all the
# 0s,1s and 2s in the given format,
# the output will be 0 1 2 2.
# Your Task:
# The task is to complete the function segregate() which segregates the nodes in the linked list as asked in the problem statement and returns the head of the modified linked list. The printing is done automatically by the driver code.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 <= N <= 103
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1 ( Given a linked list of 0s, 1s and 2s, sort it )
# **************************************************************************
# Solution Explanation:
# **************************************************************************
#
# For example:
#
# Input     => 0 -> 1 -> 2 -> 2 -> 1 -> 0 -> 0 -> 2 -> 0 -> 1 -> 1 -> 0 -> NULL
# Output    => 0 -> 0 -> 0 -> 0 -> 0 -> 1 -> 1 -> 1 -> 1 -> 2 -> 2 -> 2 -> NULL
#
# Simple solution would be to count number of 0’s, 1’s and 2’s present in the linked list and traverse the
# linked list and put them back in correct order. The problem with this approach is that we need to
# do two traversals of the list which violates the problem constraints.
#
# We can solve this problem in single traversal of the list. The idea is to maintain three pointers
# zeros, ones and twos. Then, we traverse the list from head to end and move each node to the corresponding list
# depending on its value. Finally, we combine all three lists at the end and fix the head pointer.
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
    # Function to sort linked list containing 0’s, 1’s and 2’s in single traversal
    def sortList(self, head: ListNode) -> ListNode:
        # base case
        if head is None or head.next is None:
            return head

        # maintain three dummy nodes
        first = ListNode()
        second = ListNode()
        third = ListNode()

        # maintain three references
        zero = first
        one = second
        two = third

        # traverse the list
        curr = head
        while curr:
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        # combine lists containing 0's, 1's and 2's
        zero.next = second.next if second.next else third.next
        one.next = third.next
        two.next = None

        # change head and return
        return first.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sortList(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, solution in (
            [
                listNode.initList([1, 2, 2, 1, 2, 0, 2, 2]),
                listNode.initList([0, 1, 1, 2, 2, 2, 2, 2]),
            ],
            [listNode.initList([2, 2, 0, 1]), listNode.initList([0, 1, 2, 2])],
        ):
            self.assertEqual(
                solution,
                s.sortList(head),
                "Should sort the linked list containing 0's, 1's and 2's in single traversal",
            )


if __name__ == "__main__":
    unittest.main()
