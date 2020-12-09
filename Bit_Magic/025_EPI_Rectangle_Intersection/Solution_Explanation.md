## EPI - Rectangle Intersection

## Problem Description:

This problem is concerned with rectangles whose sides are parallel to the X-axis and
Y-axis. See Figure 5.2 for examples.

![Image_1](Image_1.PNG)

Write a program which tests if two rectangles have a nonempty intersection. 
If the intersection is nonempty, return the rectangle formed by their intersection.

**___Hint: Think of the X and Y dimensions independently.___**

#### **Solution:**

Since the problem leaves it unspecified, we will treat the boundary as part
of the rectangle. This implies, for example, rectangles `A` and `B` 
in Figure 5.2 on the preceding section intersect.

There are many qualitatively different ways in which rectangles can intersect, 
e.g., 
* they have partial overlap (`D` and `F`), 
* one contains the other (`F` and `G`), 
* they share a common side (`D` and `F`), 
* they share a common corner (`A` and `B`), 
* they form a cross (`B` and `C`), 
* they form a tee (`F` and `H`), 
* etc. 

The case analysis is quite tricky.
A better approach is to focus on conditions under which it can be guaranteed 
that the rectangles do not intersect. 
For example, the rectangle with left-most lower point
`(1, 2)`, width `3`, and height `4` cannot possibly intersect 
with the rectangle with left-most lower point `(5,3)`, width `2`, and height `4`,
since the X-values of the first rectangle range from `1` to `1 + 3 = 4`, 
inclusive, and the X-values of the second rectangle range 
from `5` to `5 + 2 = 7`, inclusive.

Similarly, if the Y-values of the first rectangle do not intersect 
with the Y-values of the second rectangle, the two rectangles cannot intersect.

Equivalently, if the set of X-values for the rectangles intersect 
and the set of Y-values for the rectangles intersect, 
then all points with those X- and Y-values are
common to the two rectangles, 
so there is a nonempty intersection.

```python
import collections
import random
import unittest

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

class Solution(object):

    def is_intersect(self, r1: Rect, r2: Rect) -> bool:
        return (r1.x <= r2.x + r2.width and r1.x + r1.width >= r2.x
                and r1.y <= r2.y + r2.height and r1.y + r1.height >= r2.y)

    def intersect_rectangle(self, r1: Rect, r2: Rect) -> Rect:
        if not self.is_intersect(r1, r2):
            return Rect(0, 0, -1, -1)  # No intersection.
        return Rect(max(r1.x, r2.x), max(r1.y, r2.y),
                    min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
                    min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))

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
```

##### **Time Complexity:** `O(1)`

The time complexity is `O(1)`, since the number of operations is constant.

##### **Variant**

* Given four points in the plane, how would you check if they are the vertices of a rectangle?
*  How would you check if two rectangles, not necessarily aligned with the `X` and `Y` axes, intersect?
