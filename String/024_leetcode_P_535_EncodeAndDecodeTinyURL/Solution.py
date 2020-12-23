# Time  :
# Space :
# @tag : String
# @by  : Shaikat Majumdar
# @date: Aug 27, 2020
# **************************************************************************
# LeetCode - Problem - 535: Encode and Decode TinyURL
#
# > Note: This is a companion problem to the System Design problem: Design TinyURL.
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
# and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
# to the original URL.
#
# **************************************************************************
# Source    : https://leetcode.com/problems/encode-and-decode-tinyurl/ (LeetCode - Problem 535 - Encode and Decode TinyURL)
#
# **************************************************************************
# Reference : https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/183171/Python-%2B-md5-%2B-convert-to-base-62-greater-28-ms
#
#
import hashlib
import string

import unittest

#
# 1. We can use a-z, A-Z, 0-9 alphabet which makes 62 possible characters for encoding.
# 2. We don't want to use plain randomization, since the same long URLs will result
#    in different tiny URLs and we don't want to waste space by storing two maps to keep track of both mappings.
# 3. Instead, we will use md5 hash for a long URL and get a hexadecimal hash as a string.
# 4. To reduce the length of resulting suffix of tiny URL we get 3 slices of 10 bytes
#    each of original md5 hash -> convert each of them to integer -> xor them -> convert to base 62
#    (size of our alphabet) to get the corresponding characters.
#
# Note: Even though we could just use a single 1/3 slice of original md5 hash,
#       we could potentially introduce a collision when 2 different long URLs share the same md5 hash prefix.
#
#
class Codec:
    _PREFIX = "http://tinyurl.com"
    _ALPHABET = string.ascii_letters + string.digits
    _BASE = len(_ALPHABET)

    def __init__(self):
        self.tiny_to_long = {}

    def _convert_to_base(self, x):
        result = []
        while x:
            x, r = divmod(x, Codec._BASE)
            result.append(Codec._ALPHABET[r])
        return "".join(result)

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        md5_hash = hashlib.md5(longUrl.encode("utf-8")).hexdigest()
        # md5_hash has 32 bytes
        # get 3 slices of 10 bytes each and xor them so we end up with a shorter URL suffix of len 8
        size = len(md5_hash)

        x = md5_hash[: size // 3]
        y = md5_hash[size // 3 : -size // 3]
        z = md5_hash[-size // 3 :]
        x_as_int = int(x, 16)
        y_as_int = int(y, 16)
        z_as_int = int(z, 16)
        xored = x_as_int ^ y_as_int ^ z_as_int

        suffix = self._convert_to_base(xored)
        tiny_url = Codec._PREFIX + "/" + suffix
        if tiny_url not in self.tiny_to_long:
            self.tiny_to_long[tiny_url] = longUrl

        return tiny_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.tiny_to_long.get(shortUrl)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_encode(self) -> None:
        codec = Codec()
        self.assertEqual(
            "http://tinyurl.com/KalnJbwe",
            codec.encode("https://leetcode.com/problems/design-tinyurl"),
        )

    def test_decode(self) -> None:
        codec = Codec()
        tinyUrl = codec.encode("https://leetcode.com/problems/design-tinyurl")
        # self.assertEqual("https://leetcode.com/problems/design-tinyurl", codec.decode("http://tinyurl.com/KalnJbwe"))
        self.assertEqual(
            "https://leetcode.com/problems/design-tinyurl", codec.decode(tinyUrl)
        )


if __name__ == "__main__":
    unittest.main()
