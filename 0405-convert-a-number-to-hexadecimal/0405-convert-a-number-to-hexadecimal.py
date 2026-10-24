
class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        num = num & 0xFFFFFFFF
        result = ""
        hex_chars = "0123456789abcdef"

        while num > 0:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num //= 16

        return result
