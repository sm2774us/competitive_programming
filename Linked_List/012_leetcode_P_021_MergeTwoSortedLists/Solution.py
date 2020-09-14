#
# Time : O(N+M) ; Only one traversal of the loop is needed.
# Space: O(1)   ; There is no additional space required.
# @tag : Linked List
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 20: Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing
# together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
# **************************************************************************
# Source: https://leetcode.com/problems/merge-two-sorted-lists/ (LeetCode - Problem 20 - Merge Two Sorted Lists)
#         https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1 (GeeksForGeeks - Merge two sorted linked lists)
#
# Youtube video: https://www.youtube.com/watch?v=3O_f_sk3mFc - Linked Lists with Dummy Nodes
#                https://www.youtube.com/watch?v=GfRQvf7MB3k - Merge 2 Sorted Lists - A Fundamental Merge Sort Subroutine ("Merge Two Sorted Lists" on LeetCode)
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Linkedlists can be confusing especially if you've recently started to code but (I think)
# once you understand it fully, it should not be that difficult.
#
# For this problem, I'm going to explain several ways of solving it BUT I want to make something clear.
# Something that you've seen a lot of times in the posts on this website but probably haven't
# fully understood. dummy variable!
#
# It has been used significantly in the solutions of this problem and not well explained for a newbie level coder!
# The idea is we're dealing with pointers that point to a memory location! Think of it this way!
# You want to find gold that is hidden somewhere. Someone has put a set of clues in a sequence!
# Meaning, if you find the first clue and solve the problem hidden in the clue, you will get to the second clue!
# Solving the hidden problem of second clue will get you to the thrid clue, and so on!
# If you keep solving, you'll get to the gold! dummy helps you to find the first clue!!!!
#
# Throughout the solution below, you'll be asking yourself why dummy is not changing and
# we eventually return dummy.next????
#
# It doesn't make sense, right?
#
# However, if you think that dummy is pointing to the start and there is another variable (temp)
# that makes the links from node to node, you'll have a better feeling !
# Similar to the gold example if I tell you the first clue is at location X, then, you can solve clues
# sequentially (because of course you're smart) and bingo! you find the gold!
# Watch this ==> ( https://www.youtube.com/watch?v=3O_f_sk3mFc - Linked Lists with Dummy Nodes )
#
# This video shows why we need the dummy! Since we're traversing using temp but once temp gets to the tail
# of the sorted merged linkedlist, there's no way back to the start of the list to return as a result!
# So dummy to the rescue! it does not get changed throughout the list traversals temp is doing!
# So, dummy makes sure we don't loose the head of the thread (result list).
# Does this make sense? Alright! Enough with dummy!
#
# I think if you get this, the first solution feels natural!
# Now, watch this. ==> [ https://www.youtube.com/watch?v=GfRQvf7MB3k - Merge 2 Sorted Lists - A Fundamental Merge Sort Subroutine ("Merge Two Sorted Lists" on LeetCode) ]
# You got the idea?? Nice!
#
# First you initialize dummy and temp. One is sitting at the start of the linkedlist and the other (temp)
# is going to move forward find which value should be added to the list.
# Note that it's initialized with a value 0 but it can be anything! You initialize it with your value of choice!
# Doesn't matter since we're going to finally return dummy.next which disregards 0 that we used to start the linkedlist.
# Line #1 makes sure none of the l1 and l2 are empty! If one of them is empty, we should return the other!
# If both are nonempty, we check val of each of them to add the smaller one to the result linkedlist!
# In line #2, l1.val is smaller and we want to add it to the list. How?
# We use temp POINTER (it's pointer, remember that!).
# Since we initialized temp to have value 0 at first node, we use temp.next to point 0 to the next value we're going
# to add to the list l1.val (line #3). Once we do that, we update l1 to go to the next node of l1.
# If the if statement of line #2 doesn't work, we do similar stuff with l2. And finally, if the length of l1 and l2
# are not the same, we're going to the end of one of them at some point! Line #5 adds whatever left from
# whatever linkedlist to the temp.next (check the above video for a great explanation of this part).
# Note that both linkedlists were sorted initially. Also, this line takes care of when one of the linkedlists are empty.
# Finally, we return dummy.next since dummy is pointing to 0 and next to zero is what we've added throughout the process.
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        dummy = temp = ListNode(0)
        # while l1 != None and l2 != None:  # 1
        while l1 and l2:  # 1
            if l1.val < l2.val:  # 2
                temp.next = l1  # 3
                l1 = l1.next  # 4
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2  # 5
        return dummy.next  # 6


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mergeTwoLists(self) -> None:
        listNode = ListNode()
        s = Solution()
        for l1, l2, solution in (
            [
                listNode.initList([1, 2, 4]),
                listNode.initList([1, 3, 4]),
                listNode.initList([1, 1, 2, 3, 4, 4]),
            ],
            [
                listNode.initList([5, 10, 15, 40]),
                listNode.initList([2, 3, 20]),
                listNode.initList([2, 3, 5, 10, 15, 20, 40]),
            ],
            [
                listNode.initList([1, 1]),
                listNode.initList([2, 4]),
                listNode.initList([1, 1, 2, 4]),
            ],
        ):
            self.assertEqual(
                solution,
                s.mergeTwoLists(l1, l2),
                "Should merge two sorted linked lists and return it as a new sorted list",
            )


if __name__ == "__main__":
    unittest.main()
