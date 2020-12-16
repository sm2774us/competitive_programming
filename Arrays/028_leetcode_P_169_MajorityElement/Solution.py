#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 169: Majority Element
#
# Given an array of size n, find the majority element. The majority element is the element that
# appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
# **************************************************************************
# Source: https://leetcode.com/problems/majority-element/ (Leetcode - Problem 169 - Majority Element)
#         https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1 (GeeksForGeeks - Majority Element)
#
# **************************************************************************
#
from typing import List

import unittest

# NOTE: The main difference between LeetCode and GeeksForGeeks problems for "Majority Element" is the following:
# LeetCode - Problem 169 - Majority Element
# ------------------------------------------
# Assumption: You may assume that the array is non-empty and the majority element always exist in the array.
#
# GeeksForGeeks - Majority Element
# Assumption: If no majority element, then return -1.
#
class Solution(object):

    #
    # Boyer's Moore Algorithm --> O(1) Space
    #
    # This can be solved by Moore's voting algorithm.
    #
    # 1) Basic idea of the algorithm is if we cancel out each occurrence of an element e
    # with all the other elements that are different from e then e will exist till end
    # if it is a majority element.
    #
    # 2) Below code loops through each element and maintains a count of the element
    # that has the potential of being the majority element.
    # If next element is same then increments the count,
    # otherwise decrements the count.
    #
    # 3) If the count reaches 0 then update the potential index to the
    # current element and set count to 1.
    #
    # TC: O(N)
    # SC: O(1)
    #
    def majorityElement(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer's Moore Algorithm --> O(1) Space

        # We first assume that our first num is the majority element
        # So the count here is 1 as we have seen it 1 times, if the
        # count in the end is greater than 0 we are sure that this is majority element
        # as if you take count of majority element and subtract sum of all counts of non
        # Majority element, if that count is still positive that it proves that is
        # majority element. We do not need to check count in end over here as we are
        # sure that there exists a majority element.
        count = 1

        # Our Initial guess that this is the majority element
        result = nums[0]

        for num in nums[1:]:
            # If the next number is not same as prev
            # and count becomes 0 make this number as majority element and initialize
            # count to 1 again else just decrease the count
            if num != result:
                # decrease count by 1
                count -= 1
                # Make this element as majority element
                if count == 0:
                    result = num
                    count = 1
            else:
                # This is same element as previous one.
                count += 1
        return result

    def majorityElement_GFG(self, nums):
        dict = {}

        # store each element's frequency in a dict
        for i in nums:
            dict[i] = dict.get(i, 0) + 1

        # return the element if its count is more than n/2
        for key, value in dict.items():
            if value > len(nums) / 2:
                return key

        # no majority element is present
        return -1


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_majorityElement(self):
        s = Solution()
        for nums, solution in (
            [[3, 2, 3], 3],
            [[2, 2, 1, 1, 1, 2, 2], 2],
            [[3, 1, 3, 3, 2], 3],
        ):
            self.assertEqual(s.majorityElement(nums), solution)

    def test_majorityElement_GFG(self):
        s = Solution()
        for nums, solution in (
            [[3, 2, 3], 3],
            [[2, 2, 1, 1, 1, 2, 2], 2],
            [[1, 2, 3], -1],
            [[3, 1, 3, 3, 2], 3],
        ):
            self.assertEqual(s.majorityElement_GFG(nums), solution)


if __name__ == "__main__":
    unittest.main()
