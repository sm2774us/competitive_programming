#
# Time : O(N)
# Space: O(1)
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# **************************************************************************
# Source: https://leetcode.com/problems/palindrome-linked-list/ (LeetCode - Problem 234 - Palindrome Linked List)
#         https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1 (GeeksForGeeks - Check if Linked List is Palindrome)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Visualization of Solution 1 (s is slow, f is fast, r is rev)
#
#   1 -> 2 -> 3 -> 2 -> 1
#   s
#   f
# r
# After first loop is finished
#
# 1 <- 2 <- 3 -> 2 -> 1
#      r    s         f
# Since f is not null, that means the list is odd so increment s since the middle value is irrelevant in a palindrome
#
# 1 <- 2 <- 3 -> 2 -> 1
#      r         s    f
# After checking r and s nodes are equal while iterating through
#
#     1 <- 2 <- 3 -> 2 -> 1
# r                       f   s
# r is None so we broke out of the loop because it was None, so that means r and s nodes were always equal
# Since we know s and r will point to an equal number of nodes, either one can be used in the loop and return statement.
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

    def linkedListToList(self, head):
        if not head:
            return []

        pointer = head
        sll_list = []
        while pointer:
            sll_list.append(pointer.val)
            pointer = pointer.next
        return sll_list


class Solution:
    # Solution 1: Reversed first half == Second half?
    # Phase 1: Reverse the first half while finding the middle.
    # Phase 2: Compare the reversed first half with the second half.
    def isPalindrome(self, head: ListNode) -> bool:
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next

            # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False
        return not rev

    # Solution 2: Play Nice
    # Same as the above, but while comparing the two halves,
    # restore the list to its original state by reversing the first half back.
    def isPalindromeMaintainingTheOriginalState(self, head: ListNode) -> bool:
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_isPalindrome(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, solution in (
            [listNode.initList([1, 2]), False],
            [listNode.initList([1, 2, 2, 1]), True],
            [listNode.initList([1, 2, 1]), True],
            [listNode.initList([1, 2, 3, 4]), False],
        ):
            self.assertEqual(
                solution,
                s.isPalindrome(head),
                "Should determine if the linked list is a palindrome",
            )

    def test_isPalindromeMaintainingTheOriginalState(self) -> None:
        listNode = ListNode()
        s = Solution()
        for head, solution in (
            [listNode.initList([1, 2]), False],
            [listNode.initList([1, 2, 2, 1]), True],
            [listNode.initList([1, 2, 1]), True],
            [listNode.initList([1, 2, 3, 4]), False],
        ):
            self.assertEqual(
                solution,
                s.isPalindromeMaintainingTheOriginalState(head),
                "Should determine if the linked list is a palindrome",
            )


if __name__ == "__main__":
    unittest.main()
