#
# Time :
# Space:
#
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks For Geeks: Most frequent word in an array of strings
#
# Description:
#
# Given an array arr containing N words consisting of lowercase characters.
# Your task is to find the most frequent word in the array. If multiple words have same frequency,
# then print the word whose first occurence occurs last in the array as compared to the other strings
# with same frequency.
#
# Example 1:
#
# Input:
# N = 3
# words[] = {geeks,for,geeks}
# Output: geeks
# Explanation: "geeks" comes 2 times.
# Example 2:
#
# Input:
# N = 2
# words[] = {hello,world}
# Output: world
# Explanation: "hello" and "world" both
# have 1 frequency. We print world as
# its first occurrence comes last in the
# input array.
# Your Task:
# Complete mostFrequentWord function which takes array of strings and its length as arguments
# and returns the most frequent word. The printing is done by the driver code.
#
# Expected Time Complexity: O(N * WORD_LEN).
# Expected Auxiliary Space: O(N * WORD_LEN).
#
# Constraints:
# 1 <= N <= 5000
# 1 <= |each string| <= 50
#
# **************************************************************************
# Source    : https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings3528/1 (GeeksForGeeks - Most frequent word in an array of strings)

#
from typing import List
from collections import defaultdict
from collections import Counter
from itertools import chain

import unittest


class Solution:

    # Solution 1
    #
    # Using Counter
    #
    # TC: O(NlogN)
    #
    def mostFrequentWord_solution_1_using_lambda(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        # Our counter pairs are sorted in ascending order in terms of their frequency
        counter = sorted(Counter(strs).items(), key=lambda pair: pair[1])
        # return the last element
        return counter[-1][0]

    #
    # Solution 2:
    #
    # #### Bucket Sort
    #
    # Bucket Sort is a comparison-type algorithm which assigns elements of a list we want to sort in Buckets, or Bins.
    # The contents of these buckets are then sorted, typically with another algorithm.
    # After sorting, the contents of the buckets are appended, forming a sorted collection.
    #
    # Bucket Sort can be thought of as a scatter-order-gather approach towards sorting a list,
    # due to the fact that the elements are first scattered in buckets, ordered within them,
    # and finally gathered into a new, sorted list.
    #
    # ##### How does Bucket Sort Work?
    #
    # Before jumping into its exact implementation, let's walk through the algorithm's steps:
    #
    # 1. Set up a list of empty buckets. A bucket is initialized for each element in the array.
    # 2. Iterate through the bucket list and insert elements from the array.
    #    Where each element is inserted depends on the input list and the largest element of it.
    #    We can end up with 0..n elements in each bucket.
    # 3. Sort each non-empty bucket. You can do this with any sorting algorithm.
    #    Since we're working with a small dataset, each bucket
    #    won't have many elements so Insertion Sort works wonders for us here.
    # 4. Visit the buckets in order. Once the contents of each bucket are sorted, when concatenated,
    #    they will yield a list in which the elements are arranged based on your criteria.
    #
    #
    def mostFrequentWord_solution_2_using_bucket_sort(self, strs: List[str]) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        bucket = [[] for _ in range(len(strs) + 1)]
        Count = Counter(strs).items()
        for num, freq in Count:
            bucket[freq].append(num)
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:1][0]

    # Solution 3
    #
    # Python O(n) solution without sort, without heap, without quickselect
    #
    # TC: O(N)
    #
    def mostFrequentWord_solution_3(self, strs: List[str]) -> str:
        frequency = defaultdict(list)
        bigger = 0
        for str, count in Counter(strs).items():
            frequency[count].append(str)
            bigger = max(bigger, count)
        return frequency[bigger][-1]


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_mostFrequentWord(self) -> None:
        s = Solution()
        for strs, solution in (
            [["geeks", "for", "geeks"], "geeks"],
            [["hello", "world"], "world"],
        ):
            self.assertEqual(solution, s.mostFrequentWord_solution_1_using_lambda(strs))
            self.assertEqual(
                solution, s.mostFrequentWord_solution_2_using_bucket_sort(strs)
            )
            self.assertEqual(solution, s.mostFrequentWord_solution_3(strs))


if __name__ == "__main__":
    unittest.main()
