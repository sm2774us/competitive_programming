#
# Time  :
# Space :
#
# @tag : Backtracking
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 79: Word Search
#
# Description:
#
# Refer to Problem_Description.md
#
# **************************************************************************
# Source: https://leetcode.com/problems/word-search/ (LeetCode - Problem 79 - Word Search)
# **************************************************************************
#
from typing import List
from itertools import product

import unittest


class Solution(object):

    # Solution 1: DFS with backtracking
    #
    # In general I think this problem do not have polynomial solution,
    # so we need to check a lot of possible options.
    # What should we use in this case: it is bruteforce, with backtracking.
    # Let dfs(ind, i, j) be our backtracking function, where i and j are
    # coordinates of cell we are currently in and ind is index of letter
    # in word we currently in. Then our dfs algorithm will look like:
    #
    #   1. First, we have self.Found variable, which helps us to finish earlier if we already found solution.
    #   2. Now, we check if ind is equal to k - number of symbols in word. If we reach this point,
    #      it means we found word, so we put self.Found to True and return back.
    #   3. If we go outside our board, we return back.
    #   4. If symbol we are currently on in words is not equal to symbol in table, we also return back.
    #   5. Then we visit all neibours, putting board[i][j] = "#" before - we say in this way,
    #      that this cell was visited and changing it back after.
    #
    # What concerns main function, we need to start dfs from every cell of our board
    # and also I use early stopping if we already found word.
    #
    # Complexity: Time complexity is potentially O(m*n*3^k), where k is length of word and m and n are
    # sizes of our board: we start from all possible cells of board, and each time (except first) we can go
    # in 3 directions (we can not go back). In practice however this number will be usually much smaller,
    # because we have a lot of dead-ends. Space complexity is O(k) - potential size of our recursion stack.
    #
    # If you think this analysis can be improved, please let me know!
    #
    def exist_solution_1(self, board: List[str], word: str) -> bool:
        def dfs(ind, i, j):
            if self.Found:
                return  # early stop if word is found

            if ind == k:
                self.Found = True  # for early stopping
                return

            if i < 0 or i >= m or j < 0 or j >= n:
                return

            tmp = board[i][j]
            if tmp != word[ind]:
                return

            board[i][j] = "#"
            moveDirection = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            for x, y in moveDirection:
                dfs(ind + 1, i + x, j + y)
            board[i][j] = tmp

        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)

        for i, j in product(range(m), range(n)):
            if self.Found:
                return True  # early stop if word is found
            dfs(0, i, j)
        return self.Found

    # Solution 2 : DFS
    #
    # Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa.
    #        ord() => used to convert a character to an int
    #        chr() => used to convert an int to a character
    def exist_solution_2(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False

        # check whether can find word, start at (r,c) position
        def dfs(r, c, idx):
            if (
                0 <= r < len(board)
                and 0 <= c < len(board[0])
                and word[idx] == board[r][c]
            ):
                if idx == len(word) - 1:
                    return True

                board[r][c] = ord(board[r][c])
                # check whether can find "word" along multiple directions
                for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if dfs(i, j, idx + 1):
                        return True

                board[r][c] = chr(board[r][c])
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_exist(self) -> None:
        sol = Solution()
        for board, word, solution in (
            [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCCED",
                True,
            ],
            [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "SEE",
                True,
            ],
            [
                [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
                "ABCB",
                False,
            ],
        ):
            self.assertEqual(solution, sol.exist_solution_1(board, word))
            self.assertEqual(solution, sol.exist_solution_2(board, word))


# main
if __name__ == "__main__":
    unittest.main()
