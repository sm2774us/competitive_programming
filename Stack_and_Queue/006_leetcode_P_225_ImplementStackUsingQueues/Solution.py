#
# Time : O(1) for push() and O(N) for pop() ( or vice-versa )
# Space: O(1) for push() and pop()
#
# push O(1),
# pop amortized O(1)
#
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 225: Implement Stack using Queues
#
# Description:
#
# Implement the following operations of a stack using queues.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Example:
#
# MyStack stack = new MyStack();
#
# stack.push(1);
# stack.push(2);
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
#
# Notes:
#
#     * You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size,
#       and is empty operations are valid.
#     * Depending on your language, queue may not be supported natively. You may simulate a queue by
#       using a list or deque (double-ended queue), as long as you use only standard
#       operations of a queue.
#     * You may assume that all operations are valid (for example, no pop or top operations will be called
#       on an empty stack).
#
# **************************************************************************
# Source: https://leetcode.com/problems/implement-stack-using-queues/ (Leetcode - Problem 225 - Implement Stack using Queues)
#         https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1 (GeeksForGeeks - Stacks using two Queues)
#
from collections import deque

import unittest

# Two Queues Approach
# Streamlining the push operation to O(1) and trading off pop to O(n).
class MyStackStreamlinedForPush:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self._top = self.q1.popleft()
            self.q2.append(self._top)
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

# Streamlining pop to O(1) and trading off push to O(n).
class MyStackStreamlinedForPop:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        self._top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        result = self.q1.popleft()
        if self.q1:
            self._top = self.q1[0]
        return result

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_stackImplementationUsingTwoQueues(self) -> None:
        stack = MyStackStreamlinedForPush()
        stack.push(1)
        stack.push(2)
        # Ensure -> stack.top() -> returns 2
        self.assertEqual(2, stack.top())

        # Ensure -> stack.pop() -> returns 2
        self.assertEqual(2, stack.pop())

        # Ensure -> queue.empty() -> returns False
        self.assertEqual(False, stack.empty())

        stack = MyStackStreamlinedForPop()
        stack.push(1)
        stack.push(2)
        # Ensure -> stack.top() -> returns 2
        self.assertEqual(2, stack.top())

        # Ensure -> stack.pop() -> returns 2
        self.assertEqual(2, stack.pop())

        # Ensure -> queue.empty() -> returns False
        self.assertEqual(False, stack.empty())


if __name__ == "__main__":
    unittest.main()
