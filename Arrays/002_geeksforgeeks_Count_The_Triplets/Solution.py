#
# Time : O(); Space: O()
# @tag : Arrays
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Description:
#
# Given an array of distinct integers. The task is to count all the triplets such that sum of two elements
# equals the third element. If no such triplets can be formed, then return -1.
#
# Constraints:
# 1 <= T <= 100
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/count-the-triplets/0 (GeeksForGeeks - Count the triplets)
#
# Solution Hint: https://gist.github.com/YPshir/d0931fb5c69f1cc0c988cb2c4620f676
#
from typing import List

import unittest

class Solution:
    # def triplets(self, arr: List[int]) -> int:
    #     ans = 0
    #     i = len(arr) - 1
    #     while i >= 2:
    #         j = 0
    #         k = i - 1
    #         while j < k:
    #             if arr[i] == arr[j] + arr[k]:
    #                 ans += 1
    #                 j += 1
    #                 k -= 1
    #             elif arr[i] > arr[j] + arr[k]:
    #                 j += 1
    #             else:
    #                 k -= 1
    #         i -= 1
    #     return ans

    def triplets(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        set_a = set(arr)
        max_a = arr[-1]
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                s = arr[i] + arr[j]
                if (s > max_a):
                    break
                elif (s in set_a):
                    ans += 1
        return(ans if ans > 0 else -1)

class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_triplets(self) -> None:
        s = Solution()
        for arr, solution in (
            [ [1, 5, 3, 2], 2 ],            # [1,2] => 3  [3,2] => 5 ;  so 2 Triplets
            [ [3, 2, 7], -1 ]               # No triplet(s) possible, so -1
        ):
            self.assertEqual(solution, s.triplets(arr),
            """Should return the total number of triplets 
            such that sum of two elements equals the third element""")

if __name__ == '__main__':
    unittest.main()