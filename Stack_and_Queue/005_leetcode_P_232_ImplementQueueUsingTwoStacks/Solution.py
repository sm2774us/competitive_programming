#
# Time : O(1); Space: O(1)
#
# push O(1),
# pop amortized O(1)
#
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 232: Implement Queue using Stacks
#
# Description:
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:
#
#   * You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
#   * Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
#   * You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
#
# **************************************************************************
# Source: https://leetcode.com/problems/implement-queue-using-stacks/ (Leetcode - Problem 232 - Implement Queue using Stacks)
#         https://practice.geeksforgeeks.org/problems/queue-using-two-stacks/1 (GeeksForGeeks - Queue using two Stacks)
#
#
import unittest


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2


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

    def test_queueImplementationUsingTwoStacks(self) -> None:
        queue = MyQueue()
        queue.push(1)
        queue.push(2)

        # Ensure -> queue.peek() -> returns 1
        self.assertEqual(1, queue.peek())

        # Ensure -> queue.pop() -> returns 1
        self.assertEqual(1, queue.pop())

        # Ensure -> queue.empty() -> returns False
        self.assertEqual(False, queue.empty())


if __name__ == "__main__":
    unittest.main()
