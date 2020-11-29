#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 490: The Maze
#
# Description:
#
# Refer to LeetCode_Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/the-maze/ (LeetCode - Problem 490 - The Maze)
# **************************************************************************
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from typing import List

import unittest


class Solution(object):
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        """
        Detailed explanation is available at
        https://medium.com/@edward.zhou/leet-code-53-maximum-subarray-detailed-explained-python3-solution-d91c7affc02a
        """
        visited = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dest = (destination[0], destination[1])

        def rollFrom(pos):
            # check all possible stop positions that current pos can roll to
            # and exclude those that are already in visited
            # and then keep rolling from the rest
            # print("rolling from {}".format(pos))
            newStops = []
            for d in dirs:
                newX = pos[0]
                newY = pos[1]
                while True:  # rolling
                    possibleNewX = newX + d[0]
                    possibleNewY = newY + d[1]
                    if (
                        (possibleNewX >= 0 and possibleNewX < len(maze))
                        and (possibleNewY >= 0 and possibleNewY < len(maze[0]))
                        and (maze[possibleNewX][possibleNewY] != 1)
                    ):
                        newX = possibleNewX
                        newY = possibleNewY
                        continue
                    else:
                        break
                newStop = (newX, newY)
                if newStop == dest:
                    return True
                newStops.append(newStop)

            visited.append(pos)

            for newStop in newStops:
                if newStop not in visited:
                    if rollFrom(newStop):
                        return True
            return False

        startPos = (start[0], start[1])
        return rollFrom(startPos)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hasPath(self) -> None:
        sol = Solution()
        grid = [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ]
        start = [0, 4]
        destination = [4, 4]
        self.assertEqual(True, sol.hasPath(grid, start, destination))


# main
if __name__ == "__main__":
    # sol = Solution()
    # grid = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    # start = [0,4]
    # destination = [4,4]
    # print(sol.hasPath(grid, start, destination))
    unittest.main()
