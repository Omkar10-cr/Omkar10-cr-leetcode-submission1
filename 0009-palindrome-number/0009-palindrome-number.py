class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        # even digits: x == rev; odd digits: x == rev // 10 (drop middle digit)
        return x == rev or x == rev // 10