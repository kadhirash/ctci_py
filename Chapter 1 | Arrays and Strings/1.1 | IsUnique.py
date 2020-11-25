"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

import unittest


def isUnique(s: str) -> bool:
    ans = {}  # hash map | dictionary
    for index in range(len(s)):
        if index in ans:
            return False
        else:
            ans[index] = index
    return True


class Test(unittest.TestCase):
    dataT = [("abcd"), ("s4fad"), ("")]
    dataF = [("23dds")]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        #false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
