class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        len_hay,len_ndl = len(haystack), len(needle)

        for i in range(len_hay - len_ndl + 1):
            if haystack [i:i + len_ndl] == needle:
                return i

        return -1