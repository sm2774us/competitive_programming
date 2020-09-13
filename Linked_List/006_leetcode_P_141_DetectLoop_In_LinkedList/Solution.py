#
# Time : O(N)   ; Only one traversal of the loop is needed.
# Space: O(1)   ; There is no space required.
# @tag : Linked List, Floyd's Cycle Detection Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 141: Linked List Cycle
#
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next
# pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
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
# Output: true
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
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
#    ___
#  /     \
# |   1   |
#  \ ___ /
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Constraints:
#
#   * The number of the nodes in the list is in the range [0, 104].
#   * -105 <= Node.val <= 105
#   * pos is -1 or a valid index in the linked-list.
#
# **************************************************************************
# Source: https://leetcode.com/problems/linked-list-cycle/ (LeetCode - Problem 141 - Linked List Cycle)
#         https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1 (GeeksForGeeks - Detect Loop in linked list)
#
# Floyd's Cycle Detection Algorithm:
# Source: https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
#         [ Floyd's Cycle detection algorithm | Determining the starting point of cycle ]
#         https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
#         https://en.wikipedia.org/wiki/Cycle_detection
#         http://blog.ostermiller.org/find-loop-singly-linked-list
#
# Youtube:  https://www.youtube.com/watch?v=zbozWoMgKW0 [ Detect loop in linked list(floyd algo / Tortoise and hare algo) ]
#           https://www.youtube.com/watch?v=LUm2ABqAs1w [ Why Floyd's cycle detection algorithm works? Detecting loop in a linked list. ]
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Floyd's Cycle Detection Algorithm
# **************************************************************************
# This is the fastest method to solve this problem and has been described below:
#   * Traverse linked list using two pointers.
#   * Move one pointer(slow) by one and another pointer(fast) by two.
#   * If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list
#     doesn’t have a loop.
#   * Below image shows how the detectloop function works in the code :
#
#                                 slow   fast
#                                 \|/    \|/
#   Initially :   +------+       +-+------+---+     +--------+---+
#                 | Head | ----->| 10     |  -|---->| 15     |   |
#                 +------+       +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                +--------+-|-+     +--------+-+-+
#                                | 20     |   |     | 4      |   |
#                                +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                           +------------------+
#
#                                                    slow
#                                                    \|/
#   Step 1    :   +------+       +--------+---+     +-+------+---+
#                 | Head | ----->| 10     |  -|---->| 15     |   |
#                 +------+       +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                +--------+-|-+     +--------+-+-+
#                                | 20     |   |     | 4      |   |<--- fast
#                                +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                           +------------------+
#
#                                 fast
#                                 \|/
#   Step 2    :   +------+       +-+------+---+     +--------+---+
#                 | Head | ----->| 10     |  -|---->| 15     |   |
#                 +------+       +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                +--------+-|-+     +--------+-+-+
#                                | 20     |   |     | 4      |   |<--- slow
#                                +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                           +------------------+
#
#
#
#   Step 3    :   +------+       +--------+---+     +--------+---+
#                 | Head | ----->| 10     |  -|---->| 15     |   |
#                 +------+       +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                +--------+-|-+     +--------+-+-+
#                                | 20     |   |     | 4      |   |<--- fast
#                                +-+------+-+-+     +--------+-|-+
#                                 /|\      /|\                \|/
#                                 slow      +------------------+
#
#                                 slow   fast
#                                 \|/    \|/
#   Step 4    :   +------+       +-+------+---+     +--------+---+
#                 | Head | ----->| 10     |  -|---->| 15     |   |
#                 +------+       +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                +--------+-|-+     +--------+-+-+
#                                | 20     |   |     | 4      |   |
#                                +--------+-+-+     +--------+-|-+
#                                          /|\                \|/
#                                           +------------------+
#
#                 LOOP DETECTED
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
    # The "trick" is to not check all the time whether we have reached the end but to handle it via an exception.
    # "Easier to ask for forgiveness than permission." [ https://docs.python.org/3/glossary.html#term-eafp ]
    #
    # The algorithm is of course "Tortoise and hare" [https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare].
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while slow != fast:
            if slow is None or fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
        return True
        # try:
        #     while slow != fast:
        #         if slow is None or fast is None or fast.next is None:
        #             return None
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except AttributeError as e:
        #     return False


# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hasCycle(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, solution in (
            [listNode.initList([3, 2, 0, -4]), True],
            [listNode.initList([1, 2]), True],
            [ListNode(1), False],
        ):
            self.assertEqual(
                solution,
                s.hasCycle(head),
                "Should determine if the linked list has a cycle in it",
            )


if __name__ == "__main__":
    unittest.main()
