#
# Time : O(m+n)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 160: Intersection of Two Linked Lists
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
#                   ___         ___
#                 /     \     /     \
# A:             |  a1   |-->|  a2   |    ____          ____          ____
#                 \ ___ /     \ ___ / \ /      \      /      \      /      \
#        ___         ___         __    +   c1   |--->|   c2   |--->|   c3   |
#      /     \     /     \     /    \  +        |     \ ____ /      \ ____ /
# B:  |  b1   |-->|  b2   |-->|  b3  |/ \ ____ /
#      \ ___ /     \ ___ /     \ ___/

# begin to intersect at node c1.
#
# Example 1:
#
#                   ___         ___
#                 /     \     /     \
# A:             |   4   |-->|   1   |    ____          ____          ____
#                 \ ___ /     \ ___ / \ /      \      /      \      /      \
#        ___         ___         __    +    8   |--->|    4   |--->|   5    |
#      /     \     /     \     /    \  +        |     \ ____ /      \ ____ /
# B:  |   5   |-->|   6   |-->|   1  |/ \ ____ /
#      \ ___ /     \ ___ /     \ ___/

#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
# There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
#
#
# Example 2:
#
#        ___         ___         ___
#      /     \     /     \     /     \
# A:  |   1   |-->|   9   |-->|   1  |    ____          ____
#      \ ___ /     \ ___ /     \ ___ /\ /      \      /      \
#                                __    +    2   |--->|    4   |
#                              /    \  +        |     \ ____ /
# B:                          |   3  |/ \ ____ /
#                              \ ___/

# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4].
# There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
#
#
# Example 3:
#
#        ___         ___         ___
#      /     \     /     \     /     \
# A:  |   2   |-->|   6   |-->|   4  |
#      \ ___ /     \ ___ /     \ ___ /
#
#                    ___         ___
#                  /     \     /     \
# B:              |   1   |-->|   5   |
#                  \ ___ /     \ ___ /
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
# Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
# Notes:
#
#   * If the two linked lists have no intersection at all, return null.
#   * The linked lists must retain their original structure after the function returns.
#   * You may assume there are no cycles anywhere in the entire linked structure.
#   * Each value on each linked list is in the range [1, 10^9].
#   * Your code should preferably run in O(n) time and use only O(1) memory.
#
# **************************************************************************
# Source: https://leetcode.com/problems/intersection-of-two-linked-lists/ (Leetcode - Problem 160 - Intersection of Two Linked Lists)
#         https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/ (GeeksForGeeks - Intersection Point in Y Shapped Linked Lists)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Two Pointers:
#   * Maintain two pointers pA and pB initialized at the head of A and B, respectively.
#     Then let them both traverse through the lists, one node at a time.
#   * When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.);
#     similarly when pB reaches the end of a list, redirect it the head of A.
#   * If at any point pA meets pB, then pA/pB is the intersection node.
#   * To see why the above trick would work, consider the following two lists:
#     A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'.
#     Since B.length (=4) < A.length (=6), pB would reach the end of the merged list first,
#     because pB traverses exactly 2 nodes less than pA does. By redirecting pB to head A, and pA to head B,
#     we now ask pB to travel exactly 2 more nodes than pA would. So in the second iteration,
#     they are guaranteed to reach the intersection node at the same time.
#   * If two lists have intersection, then their last nodes must be the same one.
#     So when pA/pB reaches the end of a list, record the last element of A/B respectively.
#     If the two last elements are not the same one, then the two lists have no intersections.
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
    # Suppose there are two linked lists A and B with an intersection I starting at node X.
    # The length of intersection is L, A's length is L1+L and B's is L2+L.
    #
    # And we have two pointers, pa and pb, walk through A and B in such way that pa first walks through A
    # then switch to B while pb first walks through B then switch to A.
    #
    # In such manner, when pa and pb have walked a distance of L1+L2+L, pa has walked through |A|+|B-I| (L1+L+L2)
    # and reaches X while pb has walked through |B|+|A-I| (L2+L+L1) and reaches X as well.
    # Therefore, both pa and pb points to the start node of intersection when they first meet each other (pa == pb).
    #
    # Meanwhile, if A and B has no intersection (L = 0), pa reaches the end of B and pb reaches the end of A.
    # Both of them point to None (pa==pb==None), which is also what to return.
    # So we can combine two cases in such way:
    #

    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        # listNode = ListNode()
        # print(listNode.printList(headA))
        # print(listNode.printList(headB))

        # 2 pointers
        pointerA, pointerB = headA, headB
        # listNode = ListNode()
        i = 0
        while pointerA != pointerB:
            i += 1
            # print(f'Iteration: [ {i} ].')
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pointerA = pointerA.next if pointerA else headB
            # print(listNode.printList(pointerA))
            pointerB = pointerB.next if pointerB else headA
            # print(listNode.printList(pointerB))
            # pointerA = headB if pointerA == None else pointerA.next
            # pointerB = headA if pointerB == None else pointerB.next
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        # print(listNode.printList(pointerA))
        return pointerA


# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_getIntersectionNode(self) -> None:
        listNode = ListNode()
        s = Solution()
        for headA, headB, solution in (
            [
                listNode.initList([4, 1, 8, 4, 5]),
                listNode.initList([5, 6, 1, 8, 4, 5]),
                listNode.initList([1, 8, 4, 5]),
            ],
            [
                listNode.initList([1, 9, 1, 2, 4]),
                listNode.initList([3, 2, 4]),
                listNode.initList([2, 4]),
            ],
            [
                listNode.initList([10, 20, 5, 10]),
                listNode.initList([30, 40, 50, 5, 10]),
                listNode.initList([5, 10]),
            ],
            [listNode.initList([2, 6, 4]), listNode.initList([1, 5]), None],
        ):
            self.assertEqual(
                solution,
                s.getIntersectionNode(headA, headB),
                "Should find the node at which the intersection of two singly linked lists begins",
            )

        for headA, headB, solution in (
            [
                listNode.initList([4, 1, 8, 4, 5]),
                listNode.initList([5, 6, 1, 8, 4, 5]),
                1,
            ],
            [listNode.initList([1, 9, 1, 2, 4]), listNode.initList([3, 2, 4]), 2],
            [
                listNode.initList([10, 20, 5, 10]),
                listNode.initList([30, 40, 50, 5, 10]),
                5,
            ],
            [listNode.initList([2, 6, 4]), listNode.initList([1, 5]), None],
        ):
            self.assertEqual(
                solution,
                s.getIntersectionNode(headA, headB).val
                if s.getIntersectionNode(headA, headB)
                else None,
                "Should find the node at which the intersection of two singly linked lists begins",
            )


if __name__ == "__main__":
    # listNode = ListNode()
    # s = Solution()
    # headA = listNode.initList([4, 1, 8, 4, 5])
    # headB = listNode.initList([5, 6, 1, 8, 4, 5])
    # print(f'output = [ {listNode.printList(s.getIntersectionNode(headA, headB))} ].')
    unittest.main()
