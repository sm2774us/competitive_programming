# 1) Heap/PriorityQueue Method:
# Time : O(N * log(K))
# Space: O(K)
#
# 2) Divide and Conquer Method:
# Time : O(N * log(K)) where n is total number of nodes in lists and k is the length of lists. Because the merge sort mechanism is running in O(logk) time and for every time you have n nodes to deal with.
# Space: O(1)
# **************************************************************************
# Where: K is the length of lists
#        N is the total number of nodes in lists [ or N entries ]
# **************************************************************************
# @tag : Heap ; Divide And Conquer ; Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 23: Merge k Sorted Lists
#
# Description:
#
# You are given an array of k linked-lists lists, each linked-list is sorted
# in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
#
# Input: lists = []
# Output: []
#
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
# Constraints:
#   * k == lists.length
#   * 0 <= k <= 10^4
#   * 0 <= lists[i].length <= 500
#   * -10^4 <= lists[i][j] <= 10^4
#   * lists[i] is sorted in ascending order.
#   * The sum of lists[i].length won't exceed 10^4.
#
# **************************************************************************
# Source: https://leetcode.com/problems/merge-k-sorted-lists/ (Leetcode - Problem 23 - Merge k Sorted Lists)
#         https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1 (GeeksForGeeks - Merge K sorted linked lists)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# LeetCode - Problem - 23: Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# **************************************************************************
# 1) Heap/PriorityQueue Method:
# **************************************************************************
# Explanation
# The idea is to use a heap (min priority queue) to keep track of which lists to
# pull entries of off next.
# The heap stores entries of the form (val, idx), where idx is a location in lists,
# and val is lists[dx].val.
#
# Time complexity
# =========================
# * Assume K lists.
# * Assume total N entries.
#
#       +> Create a heap of size K: O(K)
#       +> Each heap insertion and extraction is O(log(K)). This must occur N times overall.
# Hence:
#
# Time complexity = O(K) + O(N * log(K)) = O(N * log(K)).
#
# Space complexity
# =========================
# Space complexity = O(N + K) = O(K), since the heap takes space O(K) and N ≥ K.
# **************************************************************************
# 2) Divide and Conquer Method:
# **************************************************************************
# 1. Think of divide and conquer technique
#
# 2. Divide:
# If k > 2 the n, in general case, keep dividing k lists into first half of size k/2, and second half of size k/2.
#
# 3. Conquer:
# When they return from base case k = 0 or k = 1, then start merging,
# merging process is the same as we did in Leetcode #21 Merge Two Sorted Lists
#
# 4. Finally, the merging result of first half and second half is the answer.
#
# Time complexity
# =========================
# * Assume K lists.
# * Assume total N entries.
#
# O(NlogK). Because the merge sort mechanism is running in O(logK) time
# and for every time you have N nodes to deal with.
#
# Space complexity
# =========================
# O(1)
from typing import List
import heapq

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
    def mergeKListsUsingHeap(self, lists: List[ListNode]) -> ListNode:
        """
        input: k sorted list
        output: merged result of k sorted list
        """
        if not lists:
            return None
        # store the indices of the linked lists in order of decreasing first element
        pq = [(node.val, idx) for idx, node in enumerate(lists) if node]
        heapq.heapify(pq)

        head = ListNode()
        tail = head

        while pq:
            # get smallest element
            _, next_idx = heapq.heappop(pq)
            next_node = lists[next_idx]

            if next_node.next:
                lists[next_idx] = next_node.next
                heapq.heappush(pq, (next_node.next.val, next_idx))

            tail.next = next_node
            tail = next_node

        return head.next

    def mergeKListsUsingDivideAndConquer(self, lists: List[ListNode]) -> ListNode:
        """
        input: k sorted list
        output: merged result of k sorted list
        """
        if not lists:
            return None
        # ----------------------------------
        def merge(l1, l2) -> ListNode:
            """
            input: two sorted list l1, l2
            output: merged sorted list
            """

            dummy_head = ListNode("#")
            cur = dummy_head

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    cur, l1 = cur.next, l1.next
                else:
                    cur.next = l2
                    cur, l2 = cur.next, l2.next

            if l1:
                cur.next = l1
            else:
                cur.next = l2

            return dummy_head.next

        # ----------------------------------

        if not lists:
            # base case:
            # empty list
            return None

        elif len(lists) == 1:
            # base case:
            # only one list
            return lists[0]

        # general case:
        # divide-and-conquer

        # divide:
        mid = len(lists) // 2
        left = self.mergeKListsUsingDivideAndConquer(lists[:mid])
        right = self.mergeKListsUsingDivideAndConquer(lists[mid:])

        # conquer:
        return merge(left, right)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mergeKListsUsingHeap(self) -> None:
        listNode = ListNode()
        s = Solution()
        self.assertEqual(
            listNode.initList([1, 1, 2, 3, 4, 4, 5, 6]),
            s.mergeKListsUsingHeap(
                [
                    listNode.initList([1, 4, 5]),
                    listNode.initList([1, 3, 4]),
                    listNode.initList([2, 6]),
                ]
            ),
        )
        self.assertEqual(listNode.initList([]), s.mergeKListsUsingHeap([]))
        self.assertEqual(
            listNode.initList([]), s.mergeKListsUsingHeap(listNode.initList([]))
        )

    def test_mergeKListsUsingDivideAndConquer(self) -> None:
        listNode = ListNode()
        s = Solution()
        self.assertEqual(
            listNode.initList([1, 1, 2, 3, 4, 4, 5, 6]),
            s.mergeKListsUsingDivideAndConquer(
                [
                    listNode.initList([1, 4, 5]),
                    listNode.initList([1, 3, 4]),
                    listNode.initList([2, 6]),
                ]
            ),
        )
        self.assertEqual(listNode.initList([]), s.mergeKListsUsingDivideAndConquer([]))
        self.assertEqual(
            listNode.initList([]),
            s.mergeKListsUsingDivideAndConquer(listNode.initList([])),
        )


if __name__ == "__main__":
    unittest.main()
