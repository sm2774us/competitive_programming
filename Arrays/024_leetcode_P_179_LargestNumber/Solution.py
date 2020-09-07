#
# Time : O(N); Space: O(1)
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# 179. Largest Number
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# **************************************************************************
# Source: https://leetcode.com/problems/largest-number/ (Leetcode - Problem 179 - Largest Number)
#         https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0 (GeeksForGeeks - Largest Number formed from an Array)
#
# Solution Hint: (1) https://leetcode.com/problems/largest-number/discuss/213599/Thinking-Process-in-Python
#                (2) https://leetcode.com/problems/largest-number/discuss/53270/Python-simple-solution-in-4-lines
#                (3) https://leetcode.com/problems/largest-number/discuss/53236/1-liner-in-Python [ Python One-Liner ]
#
# Mathematical Proof: https://leetcode.com/problems/largest-number/discuss/291988/A-Proof-of-the-Concatenation-Comparator's-Transtivity
#                     https://leetcode.com/problems/largest-number/discuss/53195/Mathematical-proof-of-correctness-of-sorting-method
# **************************************************************************
#
from typing import List

from functools import cmp_to_key

import unittest


class Solution:

    # built-in function
    def largestNumberDetailedExplanation(self, nums: List[int]) -> str:
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]

        # Sort nums by cmp_func decreasingly.
        nums.sort(key=cmp_to_key(cmp_func), reverse=True)

        # Remove leading 0s, if empty return '0'.
        return "".join(nums).lstrip("0") or "0"

    # built-in function
    #
    # Explanation:
    # =====================================================================================================================
    # 1-we define a function that compares two string (a,b) . we consider a bigger than b if a+b>b+a
    # for example : (a="2",b="11") a is bigger than b because "211" >"112"
    #
    # 2-convert all elements of the list from int to string
    #
    # 3-sort the list descendingly using the comparing function we defined
    # for example sorting this list ["2","11","13"] using the function defined in step 1 would produce ["2","13","11"]
    #
    # 4-we concatatenate the list "21311"
    # =====================================================================================================================
    def largestNumber1(self, nums: List[int]) -> str:
        cmp_func = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(cmp_func), reverse=True)
        return str(int("".join(nums)))

    # Python3 in 2 lines, with key function sort and *Proof*
    #
    # I was bothered by that sort(ed) method/funciton has no cmp parameter in Python3, thus decide to find a key function instead.
    #
    # As pointed out in many posts, it needs to sort the numbers with cmp(x,y) being str(x)+str(y)<=str(y)+str(x).
    # This is the same as to say x*10^n+y<=y*10^m+x.
    # Here n = len(str(y)) and m = len(str(x)).
    # The above inequality is equivalent to x/(10^m-1)<=y/(10^n-1).
    # Thus the function x->x/(10^len(str(x))-1) can be used as the key for sorting.
    # This also serves a proof that the comparison essentially is a linear order on numbers (modulo equivalence).
    #
    # Now we can give a simple proof why this algorthm works. Suppose we have a chain of numbers like axb..., where x is (one of)
    # the biggest if the key function applied, and a=a_1a_2...a_n. Then ax<=a_1a_2...a_{n-1}xa_n by x">="a_n for cmp,
    # then by induction we may move x to the front, hence axb<=xab. That is there is always an arrangement with x
    # in the first place that achieves maximum among all arrangements.
    #
    # Here the transitivity is needed to show a maximal (if not greatest when it's only a partial order) x used in the above argument exists.
    #
    # Detailed Proof: https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/471630/Idea-through-mathematical-optimization
    def largestNumberConcise(self, nums: List[int]) -> str:
        nums.sort(reverse=True, key=lambda x: x / (10 ** (len(str(x))) - 1))
        return "".join(map(str, nums)).lstrip("0") or "0"

    # bubble sort
    def largestNumber2(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    # selection sort
    def largestNumber3(self, nums: List[int]) -> str:
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return str(int("".join(map(str, nums))))

    # insertion sort
    def largestNumber4(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos - 1], cur):
                nums[pos] = nums[pos - 1]  # move one-step forward
                pos -= 1
            nums[pos] = cur
        return str(int("".join(map(str, nums))))

    # merge sort
    def largestNumber5(self, nums: List[int]) -> str:
        nums = self.mergeSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def mergeSort(self, nums, l, r):
        if l > r:
            return
        if l == r:
            return [nums[l]]
        mid = l + (r - l) // 2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid + 1, r)
        return self.merge(left, right)

    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res

    # quick sort, in-place
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums, 0, len(nums) - 1)
        return str(int("".join(map(str, nums))))

    def quickSort(self, nums: List[int], l: int, r: int):
        if l >= r:
            return
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos - 1)
        self.quickSort(nums, pos + 1, r)

    def partition(self, nums: List[int], l: int, r: int):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_findKthSmallest(self) -> None:
        s = Solution()
        for nums, solution in ([[10, 2], "210"], [[3, 30, 34, 5, 9], "9534330"]):
            self.assertEqual(
                solution,
                s.largestNumber(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumberDetailedExplanation(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumberConcise(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumber1(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumber2(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumber3(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumber4(nums),
                "Should return the rarranged list such that they form the largest number",
            )
            self.assertEqual(
                solution,
                s.largestNumber5(nums),
                "Should return the rarranged list such that they form the largest number",
            )


if __name__ == "__main__":
    unittest.main()
