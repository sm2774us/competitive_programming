#
# Time  :
# Space :
#
# @tag : Dynamic Programming
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem 292: Nim Game
#
# You are playing the following Nim Game with your friend:
#
#   * Initially, there is a heap of stones on the table.
#   * You and your friend will alternate taking turns, and you go first.
#   * On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
#   * The one who removes the last stone is the winner.
#
# Given n, the number of stones in the heap, return true if you can win the game assuming
# both you and your friend play optimally, otherwise return false.
#
# Example 1:
#
# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
#
# Example 2:
#
# Input: n = 1
# Output: true
#
# Example 3:
#
# Input: n = 2
# Output: true
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
#
# **************************************************************************
# Source: https://leetcode.com/problems/nim-game/ (LeetCode - Problem 292 - Nim Game)
# **************************************************************************
#
# Solution Explanation:
# **************************************************************************
# initialize an array for the answer:
#
#   #              p1     p2    p3
#   results = [True, True, True]  # For 1, 2, and 3 stone, you will win
#
# Then for the four stones, we can think of it this way. Not it is your turn at position four of array, will you win (True) or lose (False)?
#
#   1. We can pick up one stone and lead us to the third position (p3) which means our opponent will win
#   2. We can pick up two stones and lead us to the second position (p2) which means our opponent will win
#   3. Or the last choice that we pick up three stones and lead us to the first position (p1) which our opponent will still win
#
# So the value for the fourth position will be False and build results = [True, True, True, False]. We can only win until we can reach a position with result as False that means our opponent loses. Then we can continue with above logic to build array results until it has our answer:
#
#   results = [True, True, True]
#   for i in range(3, n+1):
#       next_result = not results [-1] or not results [-2] or not results [-3]
#       results.append(next_result )
#
# And finally we just return the position of the n as our answer. (The array is zero-based, so we have to return results[n-1]):
#
#   results = [True, True, True]
#   for i in range(3, n+1):
#       next_result = not results [-1] or not results [-2] or not results [-3]
#       results.append(next_result )
#
#   return results[n-1]
#
# However, this will get us the Timeout in conclusion. So I did a bit observation on the result array:
#
#   results = [True, True, True, False, True, True, True, False, ...]
#
# So we knew that if the n is divisible by four, the answer will be False. Therefore we got return n % 4 finally.
#
#
from typing import List
import math
import unittest


class Solution(object):

    # Solution_1
    #
    def canWinNim(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

    # Solution_2 : Bit Manipulation
    #
    # This is why I sometimes can't help but hate python.
    #
    # Mathematically if n%4 == 0, you lose. But if you check for this directly, you get abysmal performance.
    #
    # Let's convert n to its binary representation (as a string). And then check the last two bits (as substrings).
    # If neither string equals '1' you win.
    # Sounds like a lot of extra useless work, right?
    def canWinNim_bit_manipulation_one(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        return "1" in bin(n)[-2:]

    def canWinNim_bit_manipulation_two(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        b = bin(n)
        return b[-1] == "1" or b[-2] == "1"


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_canWinNim(self) -> None:
        sol = Solution()
        for n, solution in ([4, False], [1, True], [2, True]):
            self.assertEqual(solution, sol.canWinNim(n))
            self.assertEqual(solution, sol.canWinNim_bit_manipulation_one(n))
            self.assertEqual(solution, sol.canWinNim_bit_manipulation_two(n))


# main
if __name__ == "__main__":
    unittest.main()
