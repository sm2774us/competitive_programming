#
# Time : O(N); Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 876: Middle of the Linked List
#
# Description:
#
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
#
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Note:
#   * The number of nodes in the given list will be between 1 and 100.
#
# **************************************************************************
# Source: https://leetcode.com/problems/middle-of-the-linked-list/ (Leetcode - Problem 876 - Middle of the Linked List)
#         https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1 (GeeksForGeeks - Finding middle element in a linked list)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# We need two pointers, one is slow with one step each iteration, and the other is fast with two steps each iteration.
# So when the fast reaches the end of the list, the slow will arrive right in the middle,
# which is exactly what we want.
#
# And one thing needs to be considered additionally is that the number of the node can be odd and even,
# which may affect the termination condition of the iteration. To solve this, my idea is to try the algorithm
# in some small set of the examples, like the examples provided by the official. And you will find that if the
# fast reaches Null or fast.next reaches Null, the head is the result.
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
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_middleNode(self) -> None:
        listNode = ListNode()
        head = listNode.initList([1, 2, 3, 4, 5])
        s = Solution()
        solution = listNode.initList([3, 4, 5])
        ret = s.middleNode(head)
        self.assertEqual(
            solution.val,
            ret.val,
            "Should return the middle node value of the linked list",
        )
        # print(listNode.printList(ret))
        # print(listNode.printList(solution))
        self.assertEqual(
            solution, ret, "Should return the middle list node of the linked list"
        )

        listNode = ListNode()
        head = listNode.initList([1, 2, 3, 4, 5, 6])
        s = Solution()
        solution = listNode.initList([4, 5, 6])
        ret = s.middleNode(head)
        self.assertEqual(
            solution.val,
            ret.val,
            "Should return the middle node value of the linked list",
        )
        # print(listNode.printList(ret))
        # print(listNode.printList(solution))
        self.assertEqual(
            solution, ret, "Should return the middle list node of the linked list"
        )


if __name__ == "__main__":
    unittest.main()
