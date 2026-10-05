class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()

        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch

        return new_s == new_s[::-1]