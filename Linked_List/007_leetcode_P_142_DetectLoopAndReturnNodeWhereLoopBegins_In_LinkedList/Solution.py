#
# Time : O(N)   ; Only one traversal of the loop is needed.
# Space: O(1)   ; There is no space required.
# @tag : Linked List, Floyd's Cycle Detection Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 142: Linked List Cycle II
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Notice that you should not modify the linked list.
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
# Example 1:
#    ___         ___         ___         ___
#  /     \     /     \     /     \     /     \
# |   3   |-->|   2   |-->|   0   |-->|  -4   |
#  \ ___ /     \ ___ /     \ ___ /     \ ___ / \
#                 +                             |
#                /|\                            |
#                 +-----------------------------+
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
# Example 2:
#    ___         ___
#  /     \     /     \
# |   1   |-->|   2   |
#  \ ___ /     \ ___ / \
#     +                 |
#    /|\                |
#     +-----------------+
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
#    ___
#  /     \
# |   1   |
#  \ ___ /
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
# Constraints:
#
#   * The number of the nodes in the list is in the range [0, 104].
#   * -105 <= Node.val <= 105
#   * pos is -1 or a valid index in the linked-list.
#
# **************************************************************************
# Source: https://leetcode.com/problems/linked-list-cycle-ii/ (LeetCode - Problem 142 - Linked List Cycle II)
#         https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1  (GeeksForGeeks - Remove loop in Linked List)
#
# Floyd's Cycle Detection Algorithm:
# Source: https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
#         [ Floyd's Cycle detection algorithm | Determining the starting point of cycle ]
#         https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
#         https://en.wikipedia.org/wiki/Cycle_detection
#         http://blog.ostermiller.org/find-loop-singly-linked-list
#
#
# Youtube:  https://www.youtube.com/watch?v=zbozWoMgKW0 [ Detect loop in linked list(floyd algo / Tortoise and hare algo) ]
#           https://www.youtube.com/watch?v=LUm2ABqAs1w [ Why Floyd's cycle detection algorithm works? Detecting loop in a linked list. ]
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Floyd's Cycle Detection Algorithm
# **************************************************************************
# slow
# |
# v
# 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
# ^                        ^    |
# |                        |    v
# fast                     0 <- 0
#   * first we set the length of path before the entry point to be nC + D. where n is integer 0,1,2,3...
#     C is the circumference of cycle and D is the offset
#   * e.g. in the example, C = 4, so n = 1 and D = 1
#
# critical point 1:
#                         slow fast
#                          |    |
#                          v    V
# 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
#                          ^    |
#                          |    v
#                          0 <- 0
#  * when slow pointer reaches the entry point, slow traveled nC + D and fast is two times faster
#    so it traveled 2nC + 2D
#  * we know fast has been traveled 2nC+2D - (nC+D) in the cycle.
#  * so fast traveled nC + D in the cycle ( total distance - distance outside cycle: 2nC+2D - (nC+D) ).
#  * we can omit nC since it's a cycle, every C distance just go back to original position.
#  * so know fast is D beyond the entry point, when slow enters.
#  * we can imagine it as fast is C - D behind slow, so they will meet in C - D steps.
#
# critical point 2:
# 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
#                          ^    |
#                          |    v
#                  slow -> 0 <- 0
#                          ^
#                          |
#                         fast
#  * in C - D steps, slow traveled nC + D + (C - D) = (n+1)C and it's D away from entry point
#  * why? because slow traveled C - D in the cycle, and if it travels D more, it will travel C
#    which go back to entry point)
#
# critical point 3:
# slow2
# |
# v
# 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
#                          ^    |
#                          |    v
#                  slow -> 0 <- 0
#  * so we start another slow2 pointer at the beginning, and keeps incrementing both slow pointers.
#    When they meet, it must be the entry point.
#   * why? because when slow2 traveled nC + D, slow will travel nC + D,
#     (D for slow to go back to entry point and nC makes it cycling at entry point)
#     so they will meet at the entry point. and we found the answer!!
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


#
# P
# 3 -> 2 -> 0 -> -4
# q
#      q    P
# 3 -> 2 -> 0 -> -4
#
# P         q
# 3 -> 2 -> 0 -> -4
#
#           P     q
# 3 -> 2 -> 0 -> -4
#
# P
# 3 -> 2 -> 0 -> -4
# q
#
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # listNode = ListNode()
        if head is None or head.next is None:
            return None
        # slow = fast = head
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next
        # print(f'Output_1: [ {listNode.printList(slow)} ].')
        slow2 = head
        while slow and slow.next and slow2 != slow:
            # print(f'Output_3: [ {listNode.printList(slow)} ].')
            slow, slow2 = slow.next, slow2.next
        # print(f'Output_4: [ {listNode.printList(slow2)} ].')
        return slow2


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_detectCycle(self) -> None:
        listNode = ListNode()
        s = Solution()
        # head = listNode.initList([3, 2, 0, -4])
        # solution = s.detectCycle(head)
        # print(f'Output = [ {listNode.printList(solution) if solution else "NULL"} ].')
        for head, solution in (
            [listNode.initList([3, 2, 0, -4]), listNode.initList([2, 0, -4])],
            [listNode.initList([1, 2]), listNode.initList([1, 2])],
            [ListNode(1), None],
        ):
            self.assertEqual(
                solution,
                s.detectCycle(head),
                "Should return the node in the linked list where cycle begins",
            )


if __name__ == "__main__":
    unittest.main()
