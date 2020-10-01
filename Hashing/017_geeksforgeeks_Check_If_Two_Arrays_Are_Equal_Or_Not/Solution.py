#
# Time : O(N); Space: O(N)
# @tag : Hashing ; HashMap
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Check if two arrays are equal or not
#
# Description:
#
# Given two arrays A and B of equal size, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
#
# Input:
# The first line of input contains an integer T denoting the no of test cases. Then T test cases follow.  Each test case contains 3 lines of input. The first line contains an integer N denoting the size of the array. The second line contains element of array A[]. The third line contains elements of the array B[].
#
# Output:
# For each test case, print 1 if the arrays are equal else print 0.
#
# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).
#
# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 1 <= A[],B[] <= 1018
#
# Example:
# Input:
# 2
# 5
# 1 2 5 4 0
# 2 4 5 0 1
# 3
# 1 2 5
# 2 4 15
# Output:
# 1
# 0
#
# Explanation:
# Testcase1:
# Input : A[] = {1, 2, 5, 4, 0}; B[] = {2, 4, 5, 0, 1}; Since all the array elements are same. So,
# Output : 1
# Testcase2:
# Input : A[] = {1, 2, 5}; B[] = {2, 4, 15}; Since all the array elements are not same. So,
# Output : 0
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not/0 (GeeksForGeeks - Check if two arrays are equal or not )
#
#
from typing import List
import collections
import functools

import unittest


class Solution:
    # This is a chance in the interview to display your knowledge of the Python language and
    # present multiple solutions with their tradeoffs.

    # Method 1 : Using list.sort() and == operator
    # sort() coupled with == operator can achieve this task. We first sort the list,
    # so that if both the lists are identical, then they have elements at the same position.
    #
    # Drawback: This method doesn’t take into account the ordering of elements in list.
    def checkListsEqualMethodOne(self, list1: List[int], list2: List[int]) -> bool:

        # in-place sort - avoid creating unnecessary copies
        list1.sort()
        list2.sort()

        return list1 == list2

    # Method 2 : Using collections.Counter()
    # Using Counter(), we usually are able to get frequency of each element in list, checking for it, for both the list,
    # we can check if two lists are identical or not.
    #
    # Drawback: This method also ignores the ordering of the elements in the list and only takes into
    #           account the frequency of elements.
    def checkListsEqualMethodTwo(self, list1: List[int], list2: List[int]) -> bool:
        return collections.Counter(list1) == collections.Counter(list2)

    # Method 3 : Using sum() + zip() + len()
    # Using sum() + zip(), we can get sum of one of the list as summation of 1 if both the index in two lists have
    # equal elements, and then compare that number with size of other list. This also requires first to check
    # if two lists are equal before this computation.
    #
    # Advantage: 1) This method checks for the order.
    #            2) Avoids making use of the collections library and an additional data structure.
    #
    def checkListsEqualMethodThree(self, list1: List[int], list2: List[int]) -> bool:
        return len(list1) == len(list2) and len(list1) == sum(
            [1 for i, j in zip(list1, list2) if i == j]
        )

    # Method 4 : Using reduce() + map()
    # Carefully coupling power of map() to hash values and utility of reduce(),
    # we can achieve this task of checking for equality of two lists to be identical.
    #
    # Advantage: 1) This method checks for the order.
    #            2) Avoids making use of the collections library and an additional data structure.
    #
    # Drawback: Requires that the two lists be of equal size.
    def checkListsEqualMethodFour(self, list1: List[int], list2: List[int]) -> bool:
        return functools.reduce(
            lambda b1, b2: b1 and b2, map(lambda e1, e2: e1 == e2, list1, list2), True
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_checkListsEqual(self) -> None:
        s = Solution()
        for list1, list2, solution in (
            [[1, 2, 5, 4, 0], [2, 4, 5, 0, 1], True],
            [[1, 2, 5], [2, 4, 15], False],
        ):
            self.assertEqual(
                solution,
                s.checkListsEqualMethodOne(list1, list2),
                "Should determine if the two lists are equal or not",
            )
            self.assertEqual(
                solution,
                s.checkListsEqualMethodTwo(list1, list2),
                "Should determine if the two lists are equal or not",
            )
            self.assertEqual(
                solution,
                s.checkListsEqualMethodThree(list1, list2),
                "Should determine if the two lists are equal or not",
            )
            self.assertEqual(
                solution,
                s.checkListsEqualMethodFour(list1, list2),
                "Should determine if the two lists are equal or not",
            )


if __name__ == "__main__":
    unittest.main()
