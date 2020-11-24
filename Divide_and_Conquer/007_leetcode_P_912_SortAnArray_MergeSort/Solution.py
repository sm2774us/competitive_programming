#
# Time  :
# Space :
#
# @tag : Divide And Conquer ; Binary Search
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 912: Sort an Array
#
# Description:
#
# Given an array of integers nums, sort the array in ascending order.
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#
# Constraints:
#   * 1 <= nums.length <= 50000
#   * -50000 <= nums[i] <= 50000
#
# **************************************************************************
# Source: https://leetcode.com/problems/sort-an-array/ (LeetCode - Problem 912 - Sort an Array)
#         https://practice.geeksforgeeks.org/problems/quick-sort/1 (GeeksForGeeks - Quick Sort)
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List
import bisect
import collections

import unittest


class Solution(object):

    # Solution_1 : Selection Sort
    #
    def sortArray_solution_1_selection_sort(self, nums: List[int]) -> List[int]:
        # This value of i corresponds to how many values were sorted
        for i in range(len(nums)):
            # We assume that the first item of the unsorted segment is the smallest
            lowest_value_index = i
            # This loop iterates over the unsorted items
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            # Swap values of the lowest unsorted element with the first unsorted
            # element
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums

    # Solution_2 : Bubble Sort
    #
    def sortArray_solution_2_bubble_sort(self, nums: List[int]) -> List[int]:
        # We set swapped to True so the loop looks runs at least once
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Set the flag to True so we'll loop again
                    swapped = True
        return nums

    # Solution_3 : Insertion Sort
    #
    def sortArray_solution_3_insertion_sort(self, nums: List[int]) -> List[int]:
        # Start on the second element as we assume the first element is sorted
        for i in range(1, len(nums)):
            item_to_insert = nums[i]
            # And keep a reference of the index of the previous element
            j = i - 1
            # Move all items of the sorted segment forward if they are larger than
            # the item to insert
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            # Insert the item
            nums[j + 1] = item_to_insert
        return nums

    # Solution_4 : Binary Insertion Sort
    #
    # def sortArray_solution_4_binary_insertion_sort(self, nums: List[int]) -> List[int]:
    #     L = len(nums)
    #     for i in range(1, L): bisect.insort_left(nums, nums.pop(i), 0, i)
    #     return nums

    def binarySearch(self, nums, start, end, value):
        if start == end:
            if nums[start] > value:
                return start
            else:
                return start + 1

        if start + 1 == end:
            return start + 1

        mid = (start + end) // 2
        if nums[mid] < value:
            return self.binary_search(nums, value, mid, end)
        elif nums[mid] > value:
            return self.binary_search(nums, value, start, mid)
        else:
            return mid

    def sortArray_solution_4_binary_insertion_sort(self, nums):
        for i in range(1, len(nums)):
            if nums[i] <= nums[0]:
                index = 0
            elif nums[i] >= nums[i - 1]:
                continue
            else:
                index = self.binary_search(nums[0:i], 0, i - 1, nums[i])
            nums = nums[:index] + [nums[i]] + nums[index:i] + nums[i + 1 :]
        return nums

    # Solution_5 : Counting Sort
    #
    def sortArray_solution_5_counting_sort(self, nums: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(nums), min(nums), max(nums), []
        for n in range(m, M + 1):
            S.extend([n] * C[n])
        return S

    # Solution_6 : Heap Sort
    #
    def heapify(self, nums, heap_size, root_index):
        # Assume the index of the largest element is the root index
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # If the left child of the root is a valid index, and the element is greater
        # than the current largest element, then update the largest element
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # Do the same for the right child of the root
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # If the largest element is no longer the root element, swap them
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # Heapify the new root element to ensure it's the largest
            self.heapify(nums, heap_size, largest)

    def sortArray_solution_6_heap_sort(self, nums):
        n = len(nums)

        # Create a Max Heap from the list
        # The 2nd argument of range means we stop at the element before -1 i.e.
        # the first element of the list.
        # The 3rd argument of range means we iterate backwards, reducing the count
        # of i by 1
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        # Move the root of the max heap to the end of
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

        return nums

    # There are different ways to do a Quick Sort partition, this implements the
    # Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
    def partition(self, nums, low, high):
        # We select the middle element to be the pivot. Some implementations select
        # the first element or the last element. Sometimes the median value becomes
        # the pivot, or a random one. There are many more strategies that can be
        # chosen or created.
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # If an element at i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot), then swap them
            nums[i], nums[j] = nums[j], nums[i]

    # Solution_7 : Quick Sort
    #
    def sortArray_solution_7_quick_sort(self, nums: List[int]) -> List[int]:
        # Create a helper function that will be called recursively
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = self.partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)
        return nums

    def merge(self, left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # We use the list lengths often, so its handy to make variables
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if (
                left_list_index < left_list_length
                and right_list_index < right_list_length
            ):
                # We check which value from the start of each list is smaller
                # If the item at the beginning of the left list is smaller, add it
                # to the sorted list
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                # If the item at the beginning of the right list is smaller, add it
                # to the sorted list
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # If we've reached the end of the of the left list, add the elements
            # from the right list
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            # If we've reached the end of the of the right list, add the elements
            # from the left list
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    # Solution_8 : Merge Sort
    #
    def sortArray_solution_8_merge_sort(self, nums: List[int]) -> List[int]:
        # If the list is a single element, return it
        if len(nums) <= 1:
            return nums

        # Use floor division to get midpoint, indices must be integers
        mid = len(nums) // 2

        # Sort and merge each half
        left_list = self.sortArray_solution_8_merge_sort(nums[:mid])
        right_list = self.sortArray_solution_8_merge_sort(nums[mid:])

        # Merge the sorted lists into a new one
        return self.merge(left_list, right_list)

    # Solution_9 : Bucket Sort
    #
    def sortArray_solution_9_bucket_sort(self, nums: List[int]) -> List[int]:
        # Find maximum value in the list and use length of the list to determine which value in the list goes into which bucket
        max_value = max(nums)
        size = max_value / len(nums)

        # Create n empty buckets where n is equal to the length of the input list
        buckets_list = []
        for x in range(len(nums)):
            buckets_list.append([])

            # Put list elements into different buckets based on the size
        for i in range(len(nums)):
            j = int(nums[i] / size)
            if j != len(nums):
                buckets_list[j].append(nums[i])
            else:
                buckets_list[len(nums) - 1].append(nums[i])

        # Sort elements within the buckets using Insertion Sort
        for z in range(len(nums)):
            self.sortArray_solution_3_insertion_sort(buckets_list[z])

        # Concatenate buckets with sorted elements into a single list
        final_output = []
        for x in range(len(nums)):
            final_output = final_output + buckets_list[x]
        return final_output


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sortArray(self) -> None:
        sol = Solution()
        for nums, solution in (
            [[5, 2, 3, 1], [1, 2, 3, 5]],
            [[5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]],
            [[4, 1, 3, 9, 7], [1, 3, 4, 7, 9]],
            [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
        ):
            self.assertEqual(solution, sol.sortArray_solution_1_selection_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_2_bubble_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_3_insertion_sort(nums))
            self.assertEqual(
                solution, sol.sortArray_solution_4_binary_insertion_sort(nums)
            )
            self.assertEqual(solution, sol.sortArray_solution_5_counting_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_6_heap_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_7_quick_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_8_merge_sort(nums))
            self.assertEqual(solution, sol.sortArray_solution_9_bucket_sort(nums))


# main
if __name__ == "__main__":
    unittest.main()
