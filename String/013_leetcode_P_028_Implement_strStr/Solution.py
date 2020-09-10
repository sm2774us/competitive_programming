# Time : O(MN), but the average is O(N); Space: O(N) - using Boyer Moore Horspool algorithm
# @tag : String, Rabin Karp Algorithm, Knuth Morris Pratt ALgorithm, Boyer Moore Algorithm, Boyer Moore Horspool Algorithm
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 14: Implement strStr
#
# Implement strStr() [ http://www.cplusplus.com/reference/cstring/strstr/ ].
#
# Returns a pointer to the first occurrence of str2 in str1, or a null pointer if str2 is not part of str1.
#
# The matching process does not include the terminating null-characters, but it stops there.
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# **************************************************************************
# Definition of strStr() in C++ API:
# **************************************************************************
#
# strstr
# const char * strstr ( const char * str1, const char * str2 );
#       char * strstr (       char * str1, const char * str2 );
# Locate substring
# **************************************************************************
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
#
#
# Constraints:
#
# haystack and needle consist only of lowercase English characters.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/implement-strstr/ (Leetcode - Problem 28 - Implement strStr)
#             https://practice.geeksforgeeks.org/problems/implement-strstr/1 (GeeksForGeeks - Implement strstr)
#
# **************************************************************************
# Solution Explanation:
# **************************************************************************
# 1) The most simplistic method is the find approach in Python (I believe it is a C implementation)
#    which actually uses the Boyer Moore Horspool algorithm( which I explain last).
#    This algorithm would not suffice in an interview.
#
# refer to => strStrUsingBuiltInFindFunction
#
# 2) Next, we have the index approach, which is an O(n^2) solution where we first check if the needle
#    is in the haystack (no pun intended). Well, if it is in the haystack then we just return the first
#    index of the substring needle within the haystack.
#    This algorithm would most likely not suffice in an interview.
#
# refer to => strStrIndexApproach
#
# 3) This is a funny split approach, but it works.
#    We use the split method to tokenize the haystack string based on the needle substring.
#    Since we tokenize it based on the needle, we know that there is only 1 large or small token (or list) before it.
#    To find the first index of the substring, we just grab the length of the large or small token
#    before the substring token, which is the first index.
#    I'm not sure if it would suffice in an interview, but maybe it can. Ask your interviewer.
#
#    *Example: **
#    Haystack: 'Hello'; Needle: 'll'
#    Tokenize based on needle: [He][ll][o]
#    len([He]) = 2, which is the first index of 'll' here.
#
# refer to => strStrSplitApproach
#
# 4) Next, we have a substring approach, where we specify a fixed sliding window (based on the needle length)
#    that checks each substring in the haystack if it matches needle.
#    This is an O(n^2) complexity as the substring method is O(n).
#
# refer to => strStrSubstringApproach
#
# 5) Then, we have a brute force approach, which actually works decently in terms of performance.
#    The worst case for this would be O(nm). I feel like most people would give this solution during an interview.
#    Basically, for each character in the haystack we check if its succeeding characters match each
#    character of the needle. Hence, we use (i + j) to iterate over the haystack in the inner loop.
#    If there is a mismatch then we just break out of the loop. However, if the inner loop successfully
#    finishes until the needle length then we should have j == len(needle) - 1, in which we can easily
#    return the index that we had in the outer loop.
#
# refer to => strStrBruteForceApproach
#
# 6) This is the infamous Rabin Karp algorithm, which is less scarier than it seems.
#    I suggest you read on modular arithmetic with prime numbers as a primer for this algorithm.
#    In short, we use a rolling hash method to verify if a substring is matching. In addition, we use modulus
#    with a prime number to ensure that we have a hash value within a small range of numbers and only a
#    small chance of hash collisions occurring.
#    In this algorithm, we first calculate the hash value of the needle substring and the first substring
#    from the haystack, which is the size of the needle.
#    For example: Haystack = 'Hello'; Needle = 'll', we calculate the hash of 'He' and 'll.
#    To calculate the hash value, we accumulate a total of each character's ascii value
#    multipled to a base (which in our case is the max number of ascii characters - 256), then we crunch
#    this large value into a small value using modulo. For the base, you can use other values,
#    but the max ascii seems reasonable here. Also, we would like to make our hash more complex to avoid collisions.
#
#    Now, down to the nitty gritty. We only need to loop until the ''length of the haystack - length of the needle''
#    because we are looking at a window, which means we already cover the size of the needle at the end
#    of the haystack. We only move forward to our inner loop if the hash value of the haystack and needle
#    are matching. Although the hash values match this does not necessarily mean that they are the same,
#    so we verify it character by character just like in the brute force approach, and only break out if the
#    characters do not match. However, if the haystack hash and needle hash do not match then we got to
#    update our window (hash value). The code here looks scary but I ensure you the concept is quite simple.
#    Since our hash value does not match we want to remove the first character from the hash and add the
#    next one in haystack. Remember, when we initially calculated our hash value with 'hello',
#    we used the formula: ('h' * 256) % 101. Well, now we have to remove the 'h' since it does not match 'l',
#    and then we have to add 'l' to 'e''s hash value. All we are doing in this equation is
#    we are removing ('h' * 256 % 101) from the current hash and adding ('l' * 256 % 101) to get a new hash
#    representing 'el' in 'hello'. We keep doing this until we have a match.
#
# refer to => strStrRobinKarpAlgorithm
#
# 7) This algorithm is the infamous Knuth Morris Pratt algorithm, which is pretty complex. In theory,
#    the worst case is O(n), but it tends to perform worse than the others here.
#    To keep things simple it uses a pre-processing list called lps (longest prefix matching suffix), which helps us
#    avoid comparing certain substrings again in needle. This allows us to continue to iterate over the haystack
#    while changing the starting pointer in lps (which represents indices to jump to for each character in needle),
#    depending on the character in haystack. The tricky part here is actually creating the lps list and
#    understanding the pattern that we are looking for. For example, the needle "AAABAAA",
#    "BAAA", 'll' would have the lps' [0,1,2,0,1,2,3], [0,0,0,0], and [0,1] respectively.
#    Can you catch the pattern here? It's pretty weird.
#    Basically the first character of a prefix will always be 0.
#    We have two pointers here that iterate over needle.
#
#    The first pointer is ahead by 1 (we will call it the 'current ', and the other one, the 'prior').
#
#    If the prior and current character in needle match, then we move both pointers up by 1, and update lps
#    with the value of the prior pointer, which allows us to get that [0,1,2] in the first lps example.
#
#    However, if the current and prior do not match then it depends on the value of the prior pointer in lps.
#    if the prior pointer in lps is 0 then we just make the current lps value = 0, and move the current pointer
#    up by 1, since it means there was no increasing prefix before.
#    On the other hand, if the prior pointer is not equal to 0 in lps, then we need to eventually
#    move the prior pointer back to the beginning of the longest prefix, which in this case is
#    at index 0 in [0,1,2,0,1,2,3] for 'AAABAAA'. In this example, when the prior pointer is at 2 and the
#    current pointer is at 0, we trigger prefix_ptr = lps[prefix_ptr - 1], since A and B do not match.
#    At this point in time our prefix_ptr goes to 1 in lps because of prefix_ptr - 1, and then the loop goes on.
#    We notice that A and B still do not match, so we do prefix_ptr - 1 again, and now it is at 0.
#    The loop continues sees that prefix_ptr is equal to 0 so we make the current pointer in lps equal to 0
#    and increment it by one.
#    Afterwards, we produce our lps list, which provides us indices to jump to if we match a certain suffix.
#
#    Moving on, we only need one loop because of our lps auxiliary list.
#    We increment both indexes of the haystack and needle if the characters match.
#    However, if we do not match then we need to set j to a certain index based on the prior position of j in lps
#    (the pointer of needle). We set the condition if j > 0 because '0 - 1' would be -1
#    which produces an index error. If j <= 0 then increment by 1 or we run into an infinite loop.
#    We keeping doing this until j is equal to the length of needle.
#
#    I will show a small example for this algorithm here:
#    Haystack: 'hello'
#    Needle: 'll'
#    lps = [0,1]
#
#    1: 'h' and 'l' do not match, j = 0, i = 0
#    j == 0 so we increment i by 1; i = 1
#    2: 'e' and 'l' do not match, j = 0, i = 1
#    j == 0 so we increment i by 1 again; i = 2
#    3: 'l' and 'l' do match, j = 0, i = 2
#    so we increment both; j = 1, i = 3
#    4: 'l' and 'l' do match, j = 1, i = 3
#    so we increment both; j = 2, i = 4
#    j == len(needle), so we return i - j, which is 2 (and this is correct since 'l' start at index 2 in 'hello')
#
# refer to => strStrKnuthMorrisPrattAlgorithm
#
# 8) This is the traditional Boyer Moore algorithm, which is O(nm) in the worst case and is similar to the idea of KMP,
#    but much easier. Basically, we create a pre-processing list with the size of the max number of
#    ascii characters (256). We map each character's ascii value in the needle substring with it's corresponding index.
#    The indices will essentially tell us how much we need to shift to the right of haystack to match the
#    needle substring in haystack. We use max here because it's possible to get 0,
#    and we need to increment the loop at least by 1 in those cases to avoid infinite loops.
#
# refer to => strStrBoyerMooreAlgorithm,
#
# 9) This is the optimized version of the Boyer Moore algorithm called the Boyer Moore Horspool algorithm.
#    The worst case it could run is O(mn), but the average is O(n).
#    I will only briefly explain this because it's pretty much identical to the Boyer Moore with some optimizations.
#    To create our pre-processing list we create a list the size of 256 with the values as the size of needle.
#    In the for loop, we exclude the last character from needle since the value is already there, but for the rest,
#    we map the length of the 'needle - index - 1' to each character in the list.
#    For example 'add' would be '2,0,0'. Afterwards, we find the starting index of needle based on the
#    right most character, which is based on the shift window that we calculate. We can see that i decrements
#    based on the right most character in the shift window until j < 0, then we return the i + 1.
#
# refer to => strStrBoyerMooreHorspoolAlgorithm,
#
from typing import List
import collections

import unittest


class Solution:
    def strStrUsingBuiltInFindFunction(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStrIndexApproach(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def strStrSplitApproach(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1

        result = haystack.split(needle)
        return len(result[0])

    def strStrSubstringApproach(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        needle_size = len(needle)

        for i in range(len(haystack)):
            if haystack[i:needle_size] == needle:
                return i
            needle_size += 1
        return -1

    def strStrBruteForceApproach(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            for j in range(len(needle)):

                if haystack[i + j] != needle[j]:
                    break

                if j == len(needle) - 1:
                    return i

            if i == (len(haystack) - len(needle)):
                return -1

    def strStrRobinKarpAlgorithm(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

            # Our base value
        max_ascii = 256
        haystack_size = len(haystack)
        needle_size = len(needle)
        haystack_hash = 0
        needle_hash = 0

        # Reduces chance of collision and reduces values within a smaller range
        prime_num = 101

        for i in range(needle_size):
            haystack_hash += (ord(haystack[i]) * max_ascii) % prime_num
            needle_hash += (ord(needle[i]) * max_ascii) % prime_num

        for i in range(haystack_size - needle_size + 1):
            if haystack_hash == needle_hash:
                for j in range(needle_size):
                    if haystack[i + j] != needle[j]:
                        break

                    if j == (needle_size - 1):
                        return i

            if i < (haystack_size - needle_size):
                haystack_hash = (
                    haystack_hash - ((ord(haystack[i]) * max_ascii) % prime_num)
                ) + ((ord(haystack[i + needle_size]) * max_ascii) % prime_num)

        return -1

    def strStrKnuthMorrisPrattAlgorithm(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        needle_size = len(needle)
        lps = [0] * needle_size
        i = 1
        prefix_ptr = 0
        while i < needle_size:

            if needle[i] == needle[prefix_ptr]:
                prefix_ptr += 1
                lps[i] = prefix_ptr
                i += 1
            else:
                if prefix_ptr == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prefix_ptr = lps[prefix_ptr - 1]

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

            if j == len(needle):
                return i - j

        return -1

    def strStrBoyerMooreAlgorithm(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

            # Boyer Moore
        pre = [-1] * 256
        needle_size = len(needle)
        for i in range(needle_size):
            pre[ord(needle[i])] = i

        hay_size = len(haystack)
        shift_ind = 0

        while shift_ind <= (hay_size - needle_size):
            j = needle_size - 1
            while (j >= 0) and haystack[shift_ind + j] == needle[j]:
                j -= 1

            if j < 0:
                return shift_ind
            else:
                shift_ind += max(1, pre[ord(needle[j])] - j)
        return -1

    def strStrBoyerMooreHorspoolAlgorithm(self, haystack: str, needle: str) -> int:
        hay_size = len(haystack)
        needle_size = len(needle)
        if needle_size > hay_size:
            return -1

        pre = [needle_size] * 256

        for i in range(needle_size - 1):
            pre[ord(needle[i])] = needle_size - i - 1

        shift_ind = needle_size - 1
        while shift_ind < hay_size:
            j = needle_size - 1
            i = shift_ind

            while j >= 0 and haystack[i] == needle[j]:
                j -= 1
                i -= 1

            if j < 0:
                return i + 1

            shift_ind += pre[ord(haystack[shift_ind])]

        return -1


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_myAtoiLeetcode(self) -> None:
        sol = Solution()
        for haystack, needle, solution in (
            ["hello", "ll", 2],
            ["aaaaa", "bba", -1],
            ["GeeksForGeeks", "Fr", -1],
            ["GeeksForGeeks", "For", 5],
        ):
            self.assertEqual(
                solution,
                sol.strStrUsingBuiltInFindFunction(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrIndexApproach(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrSplitApproach(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrSubstringApproach(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrBruteForceApproach(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrRobinKarpAlgorithm(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrKnuthMorrisPrattAlgorithm(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrBoyerMooreAlgorithm(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )
            self.assertEqual(
                solution,
                sol.strStrBoyerMooreHorspoolAlgorithm(haystack, needle),
                "Should return the index of the first occurrence of needle in haystack",
            )


if __name__ == "__main__":
    unittest.main()
