# Twitter | OA 2019 | Social Network
#
# @tag : Graph ; Transitive Reduction
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# Twitter | OA 2019 | Social Network
#
# Problem Description:
# **************************************************************************
# Refer to Problem_Description.md.
# **************************************************************************
#
# **************************************************************************
# Source: https://leetcode.com/discuss/interview-question/374447/twitter-oa-2019-social-network (Twitter | OA 2019 | Social Network)
#
# **************************************************************************
# References:
# **************************************************************************
#
import unittest


class UnionFind:
    def __init__(self, N):
        self.items = [[i] for i in range(N)]

    def _find_index(self, item):
        for i in range(len(self.items)):
            if item in self.items[i]:
                return i
        return None

    def union(self, a, b):
        aIndex = self._find_index(a)
        bIndex = self._find_index(b)

        if aIndex is not None and bIndex is not None and aIndex != bIndex:
            self.items[bIndex] += self.items[aIndex]
            del self.items[aIndex]

    def countGroups(self):
        return len(self.items)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_socialNetworkCountGroups(self) -> None:
        n = 4
        matrix = ["1100", "1110", "0110", "0001"]
        UF = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if matrix[i][j] == "1" and i != j:
                    UF.union(i, j)

        # print(UF.countGroups())
        self.assertEqual(2, UF.countGroups())


# main
if __name__ == "__main__":
    unittest.main()
