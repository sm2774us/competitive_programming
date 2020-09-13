#
# Time : O(N)   => The two solutions are both O(N), we visit every node in the Linked List just once
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 61: Rotate List
#
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
#   Input: 1->2->3->4->5->NULL, k = 2
#   Output: 4->5->1->2->3->NULL
#   Explanation:
#   rotate 1 steps to the right: 5->1->2->3->4->NULL
#   rotate 2 steps to the right: 4->5->1->2->3->NULL
#
# Example 2:
#
#   Input: 0->1->2->NULL, k = 4
#   Output: 2->0->1->NULL
#   Explanation:
#   rotate 1 steps to the right: 2->0->1->NULL
#   rotate 2 steps to the right: 1->2->0->NULL
#   rotate 3 steps to the right: 0->1->2->NULL
#   rotate 4 steps to the right: 2->0->1->NULL
#
# **************************************************************************
# Source: https://leetcode.com/problems/rotate-list/ (Leetcode - Problem 61 - Rotate List)
#         https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1 (GeeksForGeeks - Rotate a Linked List)
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


class Solution:
    # rotateRight or rotateClockwise
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if k == 0:
            return head

        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while lastElement.next:
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length

        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head

        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next

        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None

        return answer

    # This function rotates a linked list left or counter-clockwise and
    # updates the head. The function assumes that k is smaller
    # than size of linked list. It doesn't modify the list if
    # k is greater than of equal to size
    def rotateLeft(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        if k == 0:
            return head

        listNode = ListNode()
        if k >= listNode.length(head):
            return head

        # Let us understand the below code for example k = 4
        # and list = 10->20->30->40->50->60
        current = head

        # current will either point to kth or NULL after
        # this loop
        # current will point to node 40 in the above example
        count = 1
        while count < k and current is not None:
            current = current.next
            count += 1

        # If current is None, k is greater than or equal
        # to count of nodes in linked list. Don't change
        # the list in this case
        if current is None:
            return

        # current points to kth node. Store it in a variable
        # kth node points to node 40 in the above example
        tempNode = current

        # current will point to lsat node after this loop
        # current will point to node 60 in above example
        while current.next is not None:
            current = current.next

        # Change next of last node to previous head
        # Next of 60 is now changed to node 10
        current.next = head

        # Change head to (k + 1)th node
        # head is not changed to node 50
        answer = tempNode.next

        # change next of kth node to NULL
        # next of 40 is not NULL
        tempNode.next = None

        return answer


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # test cases for - Linked List rotation - right or clockwise - by k places
    def test_rotateRight(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, k, solution in (
            [listNode.initList([1, 2, 3, 4, 5]), 2, listNode.initList([4, 5, 1, 2, 3])],
            [listNode.initList([0, 1, 2]), 4, listNode.initList([2, 0, 1])],
            [
                listNode.initList([1, 2, 3, 4, 5, 6, 7, 8]),
                4,
                listNode.initList([5, 6, 7, 8, 1, 2, 3, 4]),
            ],
            [listNode.initList([2, 4, 7, 8, 9]), 2, listNode.initList([8, 9, 2, 4, 7])],
        ):
            self.assertEqual(
                solution,
                s.rotateRight(head, k),
                "Should rotate the linked list right (clockwise) by k places",
            )

    # test cases for - Linked List rotation - left or counter-clockwise - by k places
    # where, k is a given positive integer smaller than or equal to length of the linked list
    #        k is greater than of equal to size then return the linked list as is
    def test_rotateLeft(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, k, solution in (
            [listNode.initList([1, 2, 3, 4, 5]), 2, listNode.initList([3, 4, 5, 1, 2])],
            [listNode.initList([0, 1, 2]), 2, listNode.initList([2, 0, 1])],
            [listNode.initList([0, 1, 2]), 4, listNode.initList([0, 1, 2])],
            [listNode.initList([0, 1, 2]), 5, listNode.initList([0, 1, 2])],
            [
                listNode.initList([1, 2, 3, 4, 5, 6, 7, 8]),
                4,
                listNode.initList([5, 6, 7, 8, 1, 2, 3, 4]),
            ],
            [listNode.initList([2, 4, 7, 8, 9]), 3, listNode.initList([8, 9, 2, 4, 7])],
        ):
            self.assertEqual(
                solution,
                s.rotateLeft(head, k),
                "Should rotate the linked list left (counter-clockwise) by k places",
            )


if __name__ == "__main__":
    unittest.main()
