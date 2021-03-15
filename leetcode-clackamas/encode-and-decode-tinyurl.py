import string
import random

letters = string.ascii_letters + string.digits

class Codec:
    def __init__(self):
        self.e = {"": ""}
        self.d = {"": ""}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        if longUrl in self.e:
            return self.e[longUrl]

        h = ""
        shortUrl = ""
        while shortUrl in self.d:
            h = "".join(random.sample(letters, 7))
            shortUrl = f"http://tinyurl.com/{h}"

        self.e[longUrl] = shortUrl
        self.d[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.d:
            return self.d[shortUrl]
        raise Exception("shortUrl does not have a mapping")

codec = Codec()
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
assert codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")) == "https://leetcode.com/problems/design-tinyurl"