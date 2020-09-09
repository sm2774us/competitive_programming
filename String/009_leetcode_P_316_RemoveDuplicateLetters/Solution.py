# Time : O(N); Space: O(N)
# @tag : String, Stack
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 316: Remove Duplicate Letters
#
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter
# appears once and only once. You must make sure your result is the smallest in lexicographical order
# among all possible results.
#
# Example 1:
#
# Input: "bcabc"
# Output: "abc"
# Example 2:
#
# Input: "cbacdcbc"
# Output: "acdb"
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
#
# **************************************************************************
# Source    : https://leetcode.com/problems/remove-duplicate-letters/ (Leetcode - Problem 316 - Remove Duplicate Letters)
#             https://practice.geeksforgeeks.org/problems/remove-duplicates/0 (GeeksForGeeks - Remove Duplicates)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# If we take the example 'bcabc'; and we try to manually solve this one.
#
# 1. encountered b, [good] --store it [we have nothing, let's start with this character]
# 2. encountered c, -- store it too [this is bigger than last one --> good! (lexicographically)]
# 3. encountered a, [this is smaller than the ones we have come across in the past, right? If we skip all the
#                    past ones because they were bigger than current and also presume that they appear in the future
#                    than this is a good candidate to start with.]
#    -->>Its very clear now, that a stack would be a good DS to use here or perhaps one of the better choices
#    if not the best.
# 4. encountered b, [good] -- store it [lexicographically preffered candidate when compared to last item
#                                       in the stack -- 'a']
#    ...... and keep going on till the string ends; we now have the required string in the stack.
#
#
from typing import List
import collections

import unittest

NO_OF_CHARS = 256


class Solution:
    """
    :type s: str
    :rtype: str
    """

    def removeDuplicateLetters(self, s: str) -> str:
        """Let's start with having three DS - counter for all the character frequecies in the string
                                            - a boolean list for the characters which we encounter so that we can skip them once they are encountered
                                            - a stack to store the lexicographically appropriate order of the string without the duplicates
        """
        countList = [0] * 26
        boolList = [False] * 26
        stack = []
        """Initializer the counter array"""
        for character in s:
            countList[ord(character) - ord("a")] += 1

        """Traverse the given string"""
        for character in s:
            """Decrease the count in the counter array as we came across this letter in a respective iteration"""
            countList[ord(character) - ord("a")] -= 1
            """skip the character altogether if we have encountered it already"""
            if boolList[ord(character) - ord("a")]:
                continue

            """if the stack is not empty and the iterator points to a character which is smaller than the last element in the stack --> we need to skip all the characters in the stack which are bigger than the current item. And we can only skip the items if there is a chance of encountering them in the future so we also should check for this in this while loop threshold statment"""
            while (
                stack
                and character < stack[-1]
                and countList[ord(stack[-1]) - ord("a")] > 0
            ):
                """the control comes here only if the logic found candidates to be removed from the stack. Hence lets just reverse the boolean values for these items as we should consider them fresh new items when we encounter them in the future so that we don't skip them"""
                boolList[ord(stack[-1]) - ord("a")] = False
                """pop the item"""
                stack.pop()

            """just add the item to the stack"""
            stack.append(character)

            """Don't forget to switch the boolean key ON for this item, so we can skip it, if possible"""
            boolList[ord(character) - ord("a")] = True

        return "".join(stack)

    # Since strings in Python are immutable and cannot be changed
    # This utility function will convert the string to list
    def toMutable(self, string: str) -> List[str]:
        list = []
        for i in string:
            list.append(i)
        return list

    # Utility function that changes list to string
    def toString(self, list: List[str]) -> str:
        return "".join(list)

    def removeDuplicateLettersAndMaintainOrderGeeksForGeeks(self, s: str) -> str:
        bin_hash = [0] * NO_OF_CHARS
        ip_ind = 0
        res_ind = 0
        temp = ""
        mutableString = self.toMutable(s)

        # In place removal of duplicate characters
        while ip_ind != len(mutableString):
            temp = mutableString[ip_ind]
            if bin_hash[ord(temp)] == 0:
                bin_hash[ord(temp)] = 1
                mutableString[res_ind] = mutableString[ip_ind]
                res_ind += 1
            ip_ind += 1

        # After above step string is stringiittg.
        # Removing extra iittg after string
        return self.toString(mutableString[0:res_ind])


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_removeDuplicateLettersLeetCode(self) -> None:
        sol = Solution()
        for s, solution in (["bcabc", "abc"], ["cbacdcbc", "acdb"]):
            self.assertEqual(
                solution,
                sol.removeDuplicateLetters(s),
                "Should remove duplicate letters from string s",
            )

    def test_removeDuplicateLettersGeeksForGeeks(self) -> None:
        sol = Solution()
        for s, solution in (
            ["geeksforgeeks", "geksfor"],
            ["geeks for geeks", "geks for"],
        ):
            self.assertEqual(
                solution,
                sol.removeDuplicateLettersAndMaintainOrderGeeksForGeeks(s),
                "Should remove duplicate letters and maintain the order of the string s",
            )


if __name__ == "__main__":
    unittest.main()
