#
# Time  :
# Space :
#
# @tag : Bit Magic
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# EPI ( Elements Of Programming Interviews - Adnan Aziz ) : Rectangle Intersection
#
# Description:
#
# Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python/rectangle_intersection.py (EPI - Rectangle Intersection)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
import collections
import random
import unittest

Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))


class Solution(object):
    def is_intersect(self, r1: Rect, r2: Rect) -> bool:
        return (
            r1.x <= r2.x + r2.width
            and r1.x + r1.width >= r2.x
            and r1.y <= r2.y + r2.height
            and r1.y + r1.height >= r2.y
        )

    def intersect_rectangle(self, r1: Rect, r2: Rect) -> Rect:
        if not self.is_intersect(r1, r2):
            return Rect(0, 0, -1, -1)  # No intersection.
        return Rect(
            max(r1.x, r2.x),
            max(r1.y, r2.y),
            min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
            min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
        )


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_intersect_rectangle_small_test(self) -> None:
        sol = Solution()
        R1, R2 = Rect(0, 0, 2, 2), Rect(1, 1, 3, 3)
        self.assertEqual(Rect(1, 1, 1, 1), sol.intersect_rectangle(R1, R2))
        R1, R2 = Rect(0, 0, 1, 1), Rect(1, 1, 3, 3)
        self.assertEqual(Rect(1, 1, 0, 0), sol.intersect_rectangle(R1, R2))
        R1, R2 = Rect(0, 0, 1, 1), Rect(2, 2, 3, 3)
        self.assertEqual(Rect(0, 0, -1, -1), sol.intersect_rectangle(R1, R2))

    def test_intersect_rectangle(self) -> None:
        sol = Solution()
        for _ in range(10000):
            R1 = Rect(*(random.randint(1, 100) for i in range(4)))
            R2 = Rect(*(random.randint(1, 100) for i in range(4)))

            res = sol.is_intersect(R1, R2)
            ans = sol.intersect_rectangle(R1, R2)
            self.assertTrue(res == False or (ans.width >= 0 and ans.height >= 0))


# main
if __name__ == "__main__":
    unittest.main()
