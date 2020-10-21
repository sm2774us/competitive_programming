#
# Time  : O(N log N)
# Space :
#
# @tag : Greedy
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# GeeksForGeeks - Huffman Decoding
#
# Description:
#
# The task is to implement Huffman Encoding and Decoding.
#
# Input:
# First line consists of T test cases. Only line of every test case consists of String S.
#
# Output:
# Single line output, return the Decoded String.
#
# Constraints:
# 1<=T<=100
# 2<=S<=1000
#
# Example:
# Input:
# 2
# abc
# geeksforgeeks
# Output:
# abc
# geeksforgeeks
#
# **************************************************************************
# Source: https://practice.geeksforgeeks.org/problems/huffman-decoding-1/1 (GeeksForGeeks - Huffman Decoding)
#
# **************************************************************************
# Solution Explanation
# **************************************************************************
# Refer to Solution_Explanation.md
#
from collections import Counter
from functools import total_ordering
import heapq
import unittest


def compress_binary_string(string):
    """Convert string of 0s and 1s to bits, and reinterpret bits as string"""
    # string composed of bytes, each 8 bits
    # so must make sure string of 0s and 1s
    # has length which is a multiplier of 8
    pad = (8 - len(string)) % 8
    padded_data = "0" * pad + string

    chars = [
        # convert string to binary and reinterpret as ascii char
        chr(int(eight, 2))
        for eight in
        # split padded_data in segments of length 8
        [padded_data[i : i + 8] for i in range(0, len(padded_data), 8)]
    ]

    return "".join(chars), pad


def expand_compressed_string(string, pad=0):
    padded_data = "".join(
        [
            # interpret ascii char as base 2 int, convert to binary string,
            # remove 0b cruft, and ensure has length 8
            bin(ord(char))[2:].zfill(8)
            for char in string
        ]
    )

    return padded_data[pad:]


@total_ordering
class HuffmanTree(object):
    """Huffman Code implementation
    See See https://en.wikipedia.org/wiki/Huffman_coding.
    """

    def __init__(self, weight, data, left=None, right=None):
        self.weight = weight
        self.data = data
        self.left = left
        self.right = right
        self.codebook = {}
        self.build_codebook()

    def __eq__(self, other):
        return (self.data, self.weight) == (other.data, other.weight)

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.data < other.data
        else:
            return self.weight < other.weight

    def __repr__(self):
        ldata = self.left and self.left.data
        rdata = self.right and self.right.data
        return f"<HuffmanTree (data: {self.data}, " f"left: {ldata}, right: {rdata})>"

    def is_leaf(self):
        return not self.right and not self.left

    def build_codebook(self):
        """Create map of chars to binary string encodings"""
        self.codebook = {}

        nodes = {"0": self.left, "1": self.right}

        for prefix, node in nodes.items():
            if not node:
                continue

            if node.is_leaf():
                self.codebook[node.data] = prefix

            for data, code in node.codebook.items():
                self.codebook[data] = prefix + code

        return self.codebook

    @classmethod
    def from_string(cls, string):
        # count frequencies of characters in string
        frequency = Counter(string)

        # build priority queue from frequency counter -
        # higher frequency characters have lower priority
        heap = [HuffmanTree(weight, data) for data, weight in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            weight = left.weight + right.weight
            data = left.data + right.data

            parent = HuffmanTree(weight, data, left, right)
            heapq.heappush(heap, parent)

        return heapq.heappop(heap)

    def __encode_tree(self, leaves):
        """Encode tree structure as string of 0s and 1s
        String is '0xy' where x and y are encodings of
        the left and right subtrees, respectively.
        If string has no children, string is '1'.
        Works b/c Huffman Tree is a full binary tree i.e.
        every node has either two children or no children
        Will append to leaves in preorder
        """
        if self.is_leaf():
            leaves.append(self.data)
            return "1"

        header = "0"

        header += self.left.__encode_tree(leaves)
        header += self.right.__encode_tree(leaves)

        return header

    def encode_tree(self):
        leaves = []

        encoded_tree = self.__encode_tree(leaves)
        leaves = "".join(leaves)

        return encoded_tree, leaves

    @classmethod
    def decode_tree(cls, encoded_tree, leaves, idx=0):
        """Decode tree; inverse of encode_tree
        NB: Resulting tree will have all weightless nodes
        """
        leaves = list(leaves)

        def decode_tree_helper():
            nonlocal idx
            nonlocal leaves
            nonlocal encoded_tree

            if idx >= len(encoded_tree):
                return None

            char = encoded_tree[idx]

            # leaf
            if char == "1":
                idx += 1
                data = leaves.pop(0)
                return HuffmanTree(0, data)

            idx += 1
            left = decode_tree_helper()
            right = decode_tree_helper()

            data = ""

            if left:
                data += left.data
            if right:
                data += right.data

            return HuffmanTree(0, data, left, right)

        return decode_tree_helper()

    @classmethod
    def encode(cls, string):
        """Encode the given string and its Huffman Tree"""
        huff_tree = HuffmanTree.from_string(string)
        encoded_data = huff_tree.huffman_encode(string)
        compressed_data, data_pad = compress_binary_string(encoded_data)

        encoded_tree, leaves = huff_tree.encode_tree()
        compressed_tree, tree_pad = compress_binary_string(encoded_tree)

        segments = [len(compressed_tree), tree_pad, len(leaves), data_pad]
        segments = [str(e) for e in segments]

        segments.append(compressed_tree + leaves + compressed_data)
        return "|".join(segments)

    @classmethod
    def decode(cls, string):
        """Inverse of encode"""
        meta = string.split("|", 4)

        if len(meta) != 5:
            raise ValueError("Improperly encoded string")

        meta[:4] = [int(e) for e in meta[:4]]
        ctree_len, tree_pad, leave_len, data_pad, rest = meta

        compressed_tree = rest[:ctree_len]
        leaves = rest[ctree_len : ctree_len + leave_len]
        compressed_data = rest[ctree_len + leave_len :]

        encoded_data = expand_compressed_string(compressed_data, data_pad)
        encoded_tree = expand_compressed_string(compressed_tree, tree_pad)

        huff_tree = HuffmanTree.decode_tree(encoded_tree, leaves)
        return huff_tree.huffman_decode(encoded_data)

    def huffman_encode(self, string):
        """Encode a string to another string consisting of only 0s and 1s
        NB: You should use encode, and not this method, if you need
            to decode the string and this tree will not be available
        """
        return "".join([self.codebook[char] for char in string])

    def huffman_decode(self, string):
        """Inverse of huffman_encode"""
        decoded_string = ""
        node = self

        for char in string:
            if char == "0":
                node = node.left
            elif char == "1":
                node = node.right
            else:
                raise ValueError("Improperly encoded string")

            if node.is_leaf():
                decoded_string += node.data
                node = self

        return decoded_string


class TestHuffmanTree(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(HuffmanTree(5, "a") == HuffmanTree(5, "a"), True)
        self.assertEqual(HuffmanTree(5, "a") == HuffmanTree(5, "b"), False)
        self.assertEqual(HuffmanTree(5, "a") == HuffmanTree(6, "a"), False)

    def test_lt(self):
        self.assertEqual(HuffmanTree(5, "a") < HuffmanTree(5, "b"), True)
        self.assertEqual(HuffmanTree(5, "b") == HuffmanTree(5, "a"), False)
        self.assertEqual(HuffmanTree(5, "b") == HuffmanTree(6, "a"), False)

    def test_from_string(self):
        string = "abb"
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.data, "ab")
        self.assertEqual(tree.weight, 3)
        self.assertEqual(tree.codebook, {"a": "0", "b": "1"})

        self.assertEqual(tree.left.data, "a")
        self.assertEqual(tree.left.weight, 1)
        self.assertEqual(tree.left.codebook, {})

        self.assertEqual(tree.right.data, "b")
        self.assertEqual(tree.right.weight, 2)
        self.assertEqual(tree.right.codebook, {})

    def test_huffman_encode(self):
        string = "abb"
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.huffman_encode(string), "011")

        string = "hello world!"
        expected = "1110110101010010101000011110111001011"
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.huffman_encode(string), expected)

    def test_huffman_decode(self):
        string = "abb"
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.huffman_decode("011"), string)

        string = "hello world!"
        expected = "1110110101010010101000011110111001011"
        tree = HuffmanTree.from_string(string)
        self.assertEqual(tree.huffman_decode(expected), string)

    def test_encode_tree(self):
        string = "abb"
        tree = HuffmanTree.from_string(string)

        self.assertEqual(tree.encode_tree(), ("011", "ab"))

        string = "abbc"
        tree = HuffmanTree.from_string(string)

        self.assertEqual(tree.encode_tree(), ("00111", "acb"))

    def test_decode_tree(self):
        encoded_tree, leaves = ("011", "ab")
        tree = HuffmanTree.decode_tree(encoded_tree, leaves)

        self.assertEqual(tree.data, "ab")
        self.assertEqual(tree.weight, 0)
        self.assertEqual(tree.codebook, {"a": "0", "b": "1"})

        self.assertEqual(tree.left.data, "a")
        self.assertEqual(tree.left.weight, 0)
        self.assertEqual(tree.left.codebook, {})

        self.assertEqual(tree.right.data, "b")
        self.assertEqual(tree.right.weight, 0)
        self.assertEqual(tree.right.codebook, {})

        self.assertEqual(tree.encode_tree(), (encoded_tree, leaves))


def encode(string: str) -> str:
    return HuffmanTree.encode(string)


def decode(string: str) -> str:
    return HuffmanTree.decode(string)


class TestEncoding(unittest.TestCase):
    def test_given(self):
        strings = {
            "0DE9MDK9J8I1BMUQ18HARUPOKXFE4HLADWV12OYYTUFI59Y1",
            "6QXXCOLMUNBLYY0WOB5BR2HIR5L5XG02TGRAGV",
            "5PNL",
            "GKF8ANZ2DH6P3B5WWFMELX8XEMRSJGKHMDN932EZTM2O",
            "4ZILNB9DW3Y65GIG4Z5WWICIJN6H7HTU88",
            "Aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa",
            "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
            "lots|of\nunexpected\tchars\\x",
        }

        for string in strings:
            encoded = encode(string)
            decoded = decode(encoded)
            self.assertEqual(string, decoded)


if __name__ == "__main__":
    unittest.main()
