#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Microsoft | Interview | Rod Cutting
#
# Description:
#
# Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
# Determine the locations where the cuts are to be made for maximum profit.
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/613310/microsoft-rod-cutting (Microsoft | Interview | Rod Cutting)
# **************************************************************************
#
# Reference
# **************************************************************************
# https://github.com/OpenGenus/cosmos/blob/bb07b7beb3fb2e367e83b1c81bfc08a76d50a16b/code/dynamic_programming/src/box_stacking/box_stacking.py
#
from typing import List

import unittest


class Solution(object):
    def solve_rod_cut(self, P: List[int], L: int) -> List[int]:
        ln = [i for i in range(1, L + 1)]
        return self.rod_cut(ln, P, L)

    def rod_cut(self, ln: List[int], P: List[int], L: int) -> List[int]:
        st = [[0] * (L + 1) for i in range(L + 1)]
        for i in range(1, L + 1):

            for j in range(1, L + 1):

                if ln[i - 1] <= j:
                    st[i][j] = max(P[i - 1] + st[i][j - ln[i - 1]], st[i - 1][j])
                else:
                    st[i][j] = st[i - 1][j]

        ## position of the cuts
        pos = []
        i, j = L, L
        while i > 0 and j > 0:
            if st[i][j] == st[i - 1][j]:
                i -= 1
            else:
                pos.append(j)
                j -= i
        return pos

        # ## if asked size of the cuts
        # pos = []
        # i, j = L, L
        # while i > 0 and j > 0:
        #     if st[i][j] == st[i - 1][j]:
        #         i -= 1
        #     else:
        #         pos.append(i)  # this is changed , so insted of the column we take the rows
        #         j -= i
        # return pos


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_solve_rod_cut(self) -> None:
        sol = Solution()
        L = 4
        P = [1, 2, 3, 4]
        self.assertEqual([4, 3, 2, 1], sol.solve_rod_cut(P, L))
        L = 8
        P = [1, 5, 8, 9, 10, 17, 17, 20]
        self.assertEqual([8, 2], sol.solve_rod_cut(P, L))


# main
if __name__ == "__main__":
    unittest.main()
