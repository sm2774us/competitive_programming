#
# Time : O(1); Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Implement a Queue using Linked List.
# A Query Q is of 2 Types
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop an element from the queue and print the poped element)
#
# Example 1:
#
# Input:
# Q = 5
# Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation: n the first testcase
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the
#     queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3.
#
# Example 2:
#
# Input:
# Q = 4
# Queries = 1 2 2 2 1 3
# Output: 2 -1
#
# Explanation: In the second testcase
# 1 2 the queue will be {2}
# 2   poped element will be {2} then
#     the queue will be empty.
# 2   the queue is empty and hence -1
# 1 3 the queue will be {3}.
# Your Task:
# Complete the function enqueue() which takes an integer as input parameter and dequeue() which will remove and return an element(-1 if queue is empty).
#
# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).
#
# Constraints:
# 1 <= Q <= 100
# 1 <= x <= 100
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1 ( Implement Queue using Linked List )
#
#
from typing import List
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


# A class to represent a queue

# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def __eq__(self, other):
        if not self.equal(other):
            return False
        else:
            return True

    def equal(self, other):
        if other is not None:
            return self.front == other.front and self.rear == other.rear
        else:
            return False

    def __repr__(self):
        lst = []
        p = self.front
        while p:
            lst.append(str(p.val))
            p = p.next

        return "List: [{}].".format(",".join(lst))

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def enqueue(self, item):
        temp = ListNode(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def dequeue(self):
        if self.isEmpty():
            return -1
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

    def initQueueFromList(self, nums):
        if not nums:
            return None
        self.front = None
        self.rear = None

        for n in nums:
            if not self.front:
                temp = ListNode(n)
                self.front = temp
                self.rear = self.front
            else:
                temp = ListNode(n)
                self.rear.next = temp
                self.rear = temp
        return self

    def toList(self):
        if self.isEmpty():
            return []

        pointer = self.front
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.next

        return sll_list


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_queueOps(self) -> None:
        q = Queue()
        q.enqueue(2)
        self.assertEqual(q, q.initQueueFromList([2]))
        q.enqueue(3)
        self.assertEqual(q, q.initQueueFromList([2, 3]))
        q.dequeue()
        self.assertEqual(q, q.initQueueFromList([3]))
        q.enqueue(4)
        self.assertEqual(q, q.initQueueFromList([3, 4]))
        q.dequeue()
        self.assertEqual(q, q.initQueueFromList([4]))

        q = Queue()
        q.enqueue(2)
        self.assertEqual(q, q.initQueueFromList([2]))
        q.dequeue()
        self.assertEqual(q, Queue())
        ret = q.dequeue()
        self.assertEqual(ret, -1)
        q.enqueue(3)
        self.assertEqual(q, q.initQueueFromList([3]))


if __name__ == "__main__":
    unittest.main()
