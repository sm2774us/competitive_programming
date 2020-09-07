#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 75. Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
# **************************************************************************
# 1. A rather straight forward solution is a two-pass algorithm using counting sort.
# 2. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 3. Could you come up with a one-pass algorithm using only constant space?
#
# **************************************************************************
# Source: https://leetcode.com/problems/sort-colors/ (Leetcode - Problem 75 - Sort Colors)
#         https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0 (GeeksForGeeks - Sort an array of 0s, 1s and 2s)
#
# Similar To: Dutch Partinioning Problem ( https://en.wikipedia.org/wiki/Dutch_national_flag_problem )
#         EPI - https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python_solutions/dutch_national_flag.py
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified,
# and blue. Initially we group all elements into unclassified. We iterate from the beginning as long
# as the white pointer is less than the blue pointer.
#
# Intuition:
# ----------
# The idea is to introduce three pointer that would do the job of sorting for us. pointer_red moves
# from the left side (remember it's taking care of zeros and all zeros should go to the left side of the sorted array)
# and moves one index forward once we found a 0 in the array. pointer_white is our "moving pointer" that goes
# through the array and helps with sorting. It also starts from 0 but goes one step forward if it
# finds either 0 or 1(it want to finally stop at the border of 1s and 2s). And, finally,
# pointer_blue moves from right leftward. It moves to left one step every time we find a 2.
#
# Consider this array: [1,2,1,1,0]: pointer_red = 0, pointer_white =0, and pointer_blue = 4 intially.
# Remember pointer_white is our moving pointer from left, and it stops when it gets to pointer_blue.
# Do you know why?
# Because we move the pointer_blue only if we find a number 2 and then reduce it by 1, meaning
# all the values to the right of pointer_blue are 2 already, and there is no need for pointer_
# white to go and check there! Does this make sense?
#
# Let's continue with the example with started! We pass the while loop criterion, nums[pointer_white] ==1!
# If our array doesn't have a 0, we shouldn't move this 1, right? and we haven't seen the rest of the array,
# so, we just increase pointer_white to see what's the next number (line #1).
# The next number is 2!
# It should be the right side of the output array, correct? Using line #4, we change this value
# with the pointer_blue value, which is 0. Now, the array looks like [1,0,1,1,2]!!
# Attention that we haven't changed pointer_white! It's still looking at index 1
# whose value is zero now. What happens? Line #3 swaps nums[0] and nums[1].
# Now array looks like [0, 1, 1,1,2]. Both pointer_red and pointer_white increase!
# Note that we increase pointer_red by one since 0 is placed correctly
# and we don't need to check that location anymore (all the values to the left of pointer_red are zero).
# Now, pointer_red = 1, pointer_while = 2, and pointer_blue =3, and array [0, 1, 1,1,2].
# Still while loop is valid. So, we keep going. Now nums[pointer_white] is looking at 1.
# It's located correctly (line #1), it become pointer_white = 3. Again, correct!
# Now, it's pointer_white = 4, doesn't pass the while loop criterion, and it stops!
# Sorted!
#
# That's it!!
#
from typing import List

import unittest


class Solution:
    # Time: O(n) ; Space: O(1)
    def sortColors(self, nums: List[int]) -> None:
        # zero and r record the position of "0" and "2" respectively
        pointer_red = 0
        pointer_white = 0
        pointer_blue = len(nums) - 1

        while pointer_white <= pointer_blue:
            if nums[pointer_white] == 1:  # 1
                pointer_white += 1
            elif nums[pointer_white] == 0:  # 2
                nums[pointer_white], nums[pointer_red] = (
                    nums[pointer_red],
                    nums[pointer_white],
                )  # 3
                pointer_white += 1
                pointer_red += 1
            else:
                nums[pointer_white], nums[pointer_blue] = (
                    nums[pointer_blue],
                    nums[pointer_white],
                )  # 4
                pointer_blue -= 1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sortColors(self) -> None:
        s = Solution()
        nums = [2, 0, 2, 1, 1, 0]
        s.sortColors(nums)
        self.assertEqual(
            [0, 0, 1, 1, 2, 2],
            nums,
            """Array should now be sorted such objects of the same color are now adjacent, 
                         with colors in the order red, white, and blue. With 0, 1, and 2 representing the colors
                         red, white, and blue respectively.                         
                         """,
        )


if __name__ == "__main__":
    unittest.main()
