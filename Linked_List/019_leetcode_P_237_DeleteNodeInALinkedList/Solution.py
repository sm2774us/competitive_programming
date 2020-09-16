#
# Time : O(N)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 237: https://leetcode.com/problems/delete-node-in-a-linked-list/
#
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list,
# instead you will be given access to the node to be deleted directly.
#
# It is guaranteed that the node to be deleted is not a tail node in the list.
#
# Example 1:
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
#
# Example 2:
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
#
# Example 3:
#
# Input: head = [1,2,3,4], node = 3
# Output: [1,2,4]
#
# Example 4:
#
# Input: head = [0,1], node = 0
# Output: [1]
#
# Example 5:
#
# Input: head = [-3,5,-99], node = -3
# Output: [5,-99]
#
# Constraints:
#
#   * The number of the nodes in the given list is in the range [2, 1000].
#   * -1000 <= Node.val <= 1000
#   * The value of each node in the list is unique.
#   * The node to be deleted is in the list and is not a tail node
#
# **************************************************************************
# Source: https://leetcode.com/problems/delete-node-in-a-linked-list/ (LeetCode - Problem 237 - Delete Node in a Linked List)
#         https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1 (GeeksForGeeks - Delete without head pointer)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# "node" is just a reference, like a pointer. node =node.next just changes node from pointing to original
# node to next node. But the nodelist itself doesn't change.
#
# When node is None or node is the last node, you should consider them separately.
# If the node is the last one, we have no other way except scanning from the beginning to the end,
# so the complexity is O(n), while this is the only case, other nodes can be done by replacing values,
# so the average complexity is still O(1). In Python, we don't need to contact with memory directly,
# the underlying memory manager will handle this for us. Here you can see the detailed description.
#
#
# I somehow feel this question in itself is a hack , and confuses people solving l33tcode puzzles.
#  Unlike other problems where you legimately solve it by switching around pointers , we resort to
# copying over data . Though it explicitly says , we dont have access to the previous node - I find this to be an underarm ball.
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


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __eq__(self, other):
        if not self.equal(other):
            return False
        else:
            return True

    def equal(self, other):
        if other is not None:
            return self.head == other.head and self.length == other.length
        else:
            return False

    def addNode(self, value):
        temp = self.head
        node = ListNode(value)
        node.next = temp
        self.head = node
        self.length += 1

    def printList(self):
        string = ""
        node = self.head
        if not node:
            return string
        while node:
            if node.next is None:
                if node.val is None:
                    string += "%s" % str(node.val)
                else:
                    string += "%d" % node.val
            elif node.val is None:
                string += "%s->" % str(node.val)
            else:
                string += "%d->" % node.val
            node = node.next
        return string

    def deleteNode(self, index):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # node.val, node.next = node.next.val, node.next.next
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        if index == i:
            self.length -= 1
            if prev == None:
                self.head = node.next
            else:
                prev.next = node.next
        else:
            print("Index not found")


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next
        # if node and node.next:
        #     node_to_delete = node.next
        #     node.val = node_to_delete.val
        #     node.next = node_to_delete.next
        #     # del node_to_delete --> I see some people do this at the end of the solution
        #     # Never has leetcode mentioned the availability of 'del', should ponder into
        #     # this more


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_deleteNode(self) -> None:
        ll = LinkList()
        ll.addNode(9)
        ll.addNode(1)
        ll.addNode(5)
        ll.addNode(4)
        ll.deleteNode(1)
        # print(ll.printList())
        expected = LinkList()
        expected.addNode(9)
        expected.addNode(1)
        expected.addNode(4)
        self.assertEqual(expected, ll, "Should delete a node in a singly-linked list")

        ll = LinkList()
        ll.addNode(4)
        ll.addNode(3)
        ll.addNode(2)
        ll.addNode(1)
        ll.deleteNode(2)
        # print(ll.printList())
        expected = LinkList()
        expected.addNode(4)
        expected.addNode(2)
        expected.addNode(1)
        self.assertEqual(expected, ll, "Should delete a node in a singly-linked list")

        ll = LinkList()
        ll.addNode(1)
        ll.addNode(0)
        ll.deleteNode(0)
        # print(ll.printList())
        expected = LinkList()
        expected.addNode(1)
        self.assertEqual(expected, ll, "Should delete a node in a singly-linked list")

        ll = LinkList()
        ll.addNode(-99)
        ll.addNode(5)
        ll.addNode(-3)
        ll.deleteNode(0)
        # print(ll.printList())
        expected = LinkList()
        expected.addNode(-99)
        expected.addNode(5)
        self.assertEqual(expected, ll, "Should delete a node in a singly-linked list")


if __name__ == "__main__":
    unittest.main()
