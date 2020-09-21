#
# Time : O(1) for all operations
# Space: O(1)
#
# @tag : Stack and Queue
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 155: Min Stack
#
# Description:
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
#
# Example 1:
#
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#
# **************************************************************************
# Source: https://leetcode.com/problems/min-stack/ (Leetcode - Problem 155 - Min Stack)
#         https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1 (GeeksForGeeks - Get minimum element from stack)
#
import unittest


class MinStack:
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x: int) -> None:
        currMin = self.getMin() if len(self.stack) != 0 else None
        if currMin is None or x < currMin:
            currMin = x
        self.stack.append([x, currMin])

    # @return nothing
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    # @return an integer
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    # @return an integer
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_minStack(self) -> None:
        minStack = MinStack()
        # Ensure -> stack is empty
        self.assertEqual(True, minStack.empty())
        minStack.push(-2)
        # Ensure -> stack.top() -> returns -2
        self.assertEqual(-2, minStack.top())
        minStack.push(0)
        # Ensure -> stack.top() -> returns 0
        self.assertEqual(0, minStack.top())
        minStack.push(-3)
        # Ensure -> stack.top() -> returns -3
        self.assertEqual(-3, minStack.top())
        # Ensure -> stack.getMin() -> returns -3
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        # Ensure -> stack.top() -> returns 0
        self.assertEqual(0, minStack.top())
        # Ensure -> stack.getMin() -> returns -2
        self.assertEqual(-2, minStack.getMin())


if __name__ == "__main__":
    unittest.main()
