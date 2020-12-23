#
# Time :
# Space:
#
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
#
# Geeks For Geeks: Save Ironman
#
# Description:
#
# 026_geeksforgeeks_Check_If_Strings_Are_Rotations_of_Each_Other_or_Not
#
# **************************************************************************
# Source    : https://practice.geeksforgeeks.org/problems/save-ironman/0 (GeeksForGeeks - Save Ironman)

#
import re

import unittest


class Solution:

    # Solution 1:
    #
    def is_palindrome(self, string: str) -> bool:
        string = "".join(e for e in string if e.isalnum()).lower()
        isPalindrome = True
        for i in range(int(len(string) / 2)):
            if string[i] != string[(len(string) - 1) - i]:
                isPalindrome = False

        return isPalindrome
        # if (isPalindrome):
        #     print("YES")
        # else:
        #     print("NO")


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_is_palindrome(self) -> None:
        s = Solution()
        for string, solution in (
            ["geeksforgeeks", False],
            ["I am :IronnorI Ma, i", True],
            ["Ab?/Ba", True],
        ):
            self.assertEqual(solution, s.is_palindrome(string))


if __name__ == "__main__":
    unittest.main()
