#
# Time : O(N)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 24: Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# **************************************************************************
# Source: https://leetcode.com/problems/swap-nodes-in-pairs/ (LeetCode - Problem 24 - Swap Nodes in Pairs)
#         https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1 (GeeksForGeeks - Pairwise swap elements of a linked list)
#
# **************************************************************************
# Visual Explanation of Solution: ( using dummy sentinel nodes )
# *************************************************************************
# Sentinel Node (https://en.wikipedia.org/wiki/Sentinel_node)
# *************************************************************************
# In computer programming, a sentinel node is a specifically designated node used with linked lists and trees
# as a traversal path terminator. This type of node does not hold or reference any data managed by the data structure.
#
# Sentinels are used as an alternative over using NULL as the path terminator in order to get one or more of the following benefits:
# *************************************************************************
#   * Marginally increased speed of operations
#   * Increased data structure robustness (arguably)
# *************************************************************************
#   cur
#   dummy         1st          2nd
#  +-----+      +-----+      +-----+      +------+
#  |  x  |----->|  1  |----->|  2  |----->| null |
#  +-----+      +-----+      +-----+      +------+
#
#  (1) cur.next = sec
#
#   cur           1st          2nd
#  +-----+      +-----+      +-----+      +------+
#  |  x  |--X-->|  1  |----->|  2  |----->| null |
#  +-----+      +-----+      +--+--+      +------+
#     \                         /
#      \_______________________/
#
#  (2) fist.next = sec.next
#                        __________________
#   cur           1st   /      2nd         \
#  +-----+      +-----+/     +-----+      +-+----+
#  |  x  |      |  1  |--X-->|  2  |----->| null |
#  +-----+      +-----+      +--+--+      +------+
#     \                        /
#      \______________________/
#
#  (3) sec.next = first
#                        __________________
#   cur           1st   /      2nd         \
#  +-----+      +-----+/     +-----+      +-+----+
#  |  x  |      |  1  |<-----|  2  |      | null |
#  +-----+      +-----+      +--+--+      +------+
#     \                        /
#      \______________________/
#
#  (4) cur = cur.next.next
#                            +-----+
#                            | cur |-----
#                            +-----+   /
#   dummy         2nd          1st <--/
#  +-----+      +-----+      +-----+      +------+
#  |  x  |----->|  2  |----->|  1  |----->| null |
#  +-----+      +-----+      +-----+      +------+
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_swapPairs(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, solution in (
            [listNode.initList([1, 2, 3, 4]), listNode.initList([2, 1, 4, 3])],
            [
                listNode.initList([1, 2, 2, 4, 5, 6, 7, 8]),
                listNode.initList([2, 1, 4, 2, 6, 5, 8, 7]),
            ],
        ):
            self.assertEqual(
                solution,
                s.swapPairs(head),
                "Should swap every two adjacent nodes and return its head",
            )


if __name__ == "__main__":
    unittest.main()
