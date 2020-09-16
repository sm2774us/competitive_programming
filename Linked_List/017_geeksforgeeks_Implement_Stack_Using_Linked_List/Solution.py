#
# Time : O(1); Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Implement Stack using Linked List
#
# Let's give it a try! You have a linked list and you have to implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack.
#
# Example 1:
#
# Input:
# push(2)
# push(3)
# pop()
# push(4)
# pop()
# Output: 3, 4
# Explanation:
# push(2)    the stack will be {2}
# push(3)    the stack will be {2 3}
# pop()      poped element will be 3,
#            the stack will be {2}
# push(4)    the stack will be {2 4}
# pop()      poped element will be 4
# Example 2:
#
# Input:
# pop()
# push(4)
# push(5)
# pop()
# Output: -1, 5
# Your Task: You are required to complete two methods push() and pop(). The push() method takes one argument, an integer 'x' to be pushed into the stack and pop() which returns an integer present at the top and popped out from the stack. If the stack is empty then return -1 from the pop() method.
#
# Expected Time Complexity: O(1) for both push() and pop().
# Expected Auxiliary Space: O(1) for both push() and pop().
#
# Constraints:
# 1 <= Q <= 100
# 1 <= x <= 100
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1 ( Implement Stack using Linked List )
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
            string += "%s" % str(head.val)
        else:
            string += "%d" % head.val
        return string

    # length of linked list => recursive function
    def length(self, head):
        if head is None:
            return 0
        else:
            return 1 + self.length(head.next)

    def linkedListToList(self, head):
        if not head:
            return []

        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.next
        return sll_list


# A class to represent a stack
class Stack:
    def __init__(self, data=None):
        self.head = None
        if data:
            for datum in data:
                self.push(datum)

    def __eq__(self, other):
        if not self.equal(other):
            return False
        else:
            return True

    def equal(self, other):
        if other is not None:
            return self.head == other.head
        else:
            return False

    def __repr__(self):
        lst = []
        p = self.head
        while p:
            lst.append(str(p.val))
            p = p.next

        return "List: [{}].".format(",".join(lst))

    def isEmpty(self):
        return self.head == None

    # Method to add an item to the stack
    def push(self, item):
        temp = ListNode(item)
        if self.isEmpty():
            self.head = temp
            return
        self.head.next = temp
        self.head = temp

    # Method to remove an item from stack
    def pop(self):
        if self.isEmpty():
            return -1
        temp = self.head
        return temp


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_stackOps(self) -> None:
        stack = Stack()
        stack.push(2)
        self.assertEqual(stack, Stack([2]))
        stack.push(3)
        self.assertEqual(stack, Stack([2, 3]))
        stack.pop()
        self.assertEqual(stack, Stack([3]))
        stack.push(4)
        self.assertEqual(stack, Stack([3, 4]))
        stack.pop()
        self.assertEqual(stack, Stack([4]))

        stack = Stack()
        ret = stack.pop()
        self.assertEqual(ret, -1)
        stack.push(4)
        self.assertEqual(stack, Stack([4]))
        stack.push(5)
        self.assertEqual(stack, Stack([4, 5]))
        stack.pop()
        self.assertEqual(stack, Stack([5]))


if __name__ == "__main__":
    unittest.main()
