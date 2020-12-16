#
# Time : O(N); Space: O(1)
# @tag : Arrays, Two Pointer
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 41: First Missing Positive
#
# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
#
# Example 1:
#
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#
# Constraints:
#
#   * 0 <= nums.length <= 300
#   * -231 <= nums[i] <= 231 - 1
#
# **************************************************************************
# Source: https://leetcode.com/problems/first-missing-positive/ (LeetCode - Problem 41 - First Missing Positive)
#         https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number/0 (GeeksForGeeks - Smallest Positive missing number)
# **************************************************************************
#
from typing import List
from math import inf

import unittest

# Presented below 3 Python Solutions with:
# TC : O(N)
# SC : O(1)
#
class Solution(object):

    # Solution 1:
    #
    # TC: O(N)
    # SC: O(1)
    #
    def firstMissingPositive_solution_1(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        i, count = 0, 1
        l = len(nums)

        while i < l:
            num = nums[i]
            # only swaps numbers within range [1, len(nums))
            # skips swap if number already valid in index

            if 1 <= num < l and nums[num - 1] != nums[i]:
                nums[num - 1], nums[i] = nums[i], nums[num - 1]
            else:
                i += 1

                # only iterates on next valid num
                # eg. swap [2, 1], now [1,2] needs iteration

                while count - 1 < l and nums[count - 1] == count:
                    count += 1
        return count

    # Solution 2:
    #
    # Notice, that first missing positive will always be in range 1,2,...n,n+1, where n is length of nums.
    # Let us rearrange numbers, putting each number on its place: number i on place i-1
    # (because indexes start with 0): let us iterate over our numbers and change two numbers
    # if one of them not on its place: we break if number not in range 1,...,n or
    # if we are trying to put number on the place, which is already occupied with this place
    # (because we have infinite loop in this case)
    #
    # When we iterate all numbers we find for number which is not on its place,
    # using i == nums[i] - 1. It can happen that all numbers between 1 and n are here,
    # so I add [0] to the end. Finally, I found index of False in this array: it will be our number.
    #
    # Complexity: even though we have while loop inside for loop, complexity will be O(n):
    # on each step we put at least one number to its proper place.
    #
    # Additional space complexity is O(1), however we modify our nums.
    #
    # This solution is very similar to problem 442.
    # Find All Duplicates in an Array, see my detailed solution here
    # https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
    #
    #
    # TC: O(N)
    # SC: O(1)
    #
    def firstMissingPositive_solution_2(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 in range(n) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # The commented line will make space complexity to be O(n)
        # return ([i == nums[i]-1 for i in range(n)] + [0]).index(False) + 1
        # To achieve constant space complexity requirement of O(1)
        # use next with default parameter set to n + 1 as shown below:
        return next((i + 1 for i, num in enumerate(nums) if num != i + 1), n + 1)

    # Solution 3:
    #
    # Here are the train of thoughts to arrive to the final solution:
    # ----------------------------------------------------------------
    # The answer is always between 1 to length of nums + 1.
    # Why? Because the biggest positive integer we can put as answer for the input of length n,
    # is when the input is [1, 2, 3, ..., n], in that case the answer is n+1.
    # Otherwise, if the input is not exactly as mentioned (in any order),
    # then the answer must be a positive integer that is less than n+1.
    #
    # Given that the answer is limited to said range, then we can simply solve
    # this with linear time and linear space. We can create a flag booleans
    # that indicate whether an index is appearing in the nums or not. See simple code below!
    #
    # ------------- simple code starts here ------------
    # flags = [False] * len(nums)
    #
    # for num in nums:
    # 	if num > 0:
    # 		flags[num-1] = True // notice that we -1, so that the answer set 1..n becomes 0-indexed 0..n-1
    #
    # for index in range(len(flags)):
    # 	if flags[index] == False:
    # 		return index + 1
    #
    # return len(nums) + 1 // happens when all flags are true
    # ------------- simple code ends here -------------
    #
    # * Now, how do we improve this to be a better solution with constant additional space? In other words,
    #   how to get rid of the additional booleans? You can probably guess it already.
    #   Yes by using the original nums array as flags.
    #
    # * Let say we flag it by changing the value in index to None if it's appearing in nums.
    #   Problem? Yes, we still need to retain the original values in nums, because as we loop
    #   over the nums to flag the index, we will definitely get in trouble if the index
    #   we're flagging hasn't been evaluated yet. Take an example of [3,1,2]
    #   (which supposed to have the answer 4), here is how the nums array is being evaluated, in each loop-step:
    #
    #   ** Before loop: [3,1,2]
    #   ** Loop at index 0: [3, 1, None]. The index that 3 points to is index 2, therefore the value becomes None. This is the part where we change index 2, while index 2 itself hasn't been evaluated yet.
    #   ** Loop at index 1: [None, 1, None]. The index that 1 points to is index 0, therefore the value becomes None.
    #   ** Loop at index 2: [None, 1, None]. At this step, it's doing nothing because the original value of 2 has already been changed to None, and we have no way to flag index 1 as None.
    #
    # * So how do we flag elements in nums while also retaining original value that matters?
    #   Notice I mentioned 'that matters', because we only care about positive integers. We can simply
    #   discard anything that is not positive integers. And because of that, we can use positive
    #   and negative value as flag—multiply the value with -1 to flag it so it becomes negative.
    #   So positive means hasn't been flagged, negative means has been flagged. Whether it's
    #   positive or negative, we can get the original value with abs. So for above example,
    #   the correct steps would be:
    #
    #   ** Before loop: [3, 1, 2]
    #   ** Loop at index 0: [3, 1, -2]
    #   ** Loop at index 1: [-3, 1, -2]
    #   ** Loop at index 2: [-3, -1, -2]
    #   And finally when we're looking for the answer, we find that all the values are negative (flagged),
    #   therefore the answer is 4.
    #
    # * Final thoughts: what about those zeros and negative nums??? Simply change them to 0 before
    #   entering the main algorithm explained above. We just need to be careful not to multiply
    #   those zeros to -1 when flagging, instead change it to something like -inf
    #   (as long as it's a negative value, then it's flagged)
    #
    # TC: O(N)
    # SC: O(1)
    #
    def firstMissingPositive_solution_3(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = 0

        for i, num in enumerate(nums):
            index = abs(num) - 1
            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = -inf
                # we don't want to make negative to be positive again, when its duplicated num
                elif nums[index] > 0:
                    nums[index] *= -1

        for index, num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_firstMissingPositive(self):
        s = Solution()
        for nums, solution in (
            [[1, 2, 0], 3],
            [[3, 4, -1, 1], 2],
            [[7, 8, 9, 11, 12], 1],
            [[1, 2, 3, 4, 5], 6],
            [[0, -10, 1, 3, -20], 2],
        ):
            self.assertEqual(s.firstMissingPositive_solution_1(nums), solution)
            self.assertEqual(s.firstMissingPositive_solution_2(nums), solution)
            self.assertEqual(s.firstMissingPositive_solution_3(nums), solution)


if __name__ == "__main__":
    unittest.main()
