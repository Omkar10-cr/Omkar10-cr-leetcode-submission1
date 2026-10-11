class Solution:
    def findMaxConsecutiveOnes(self, nums):
        best = cur = 0
        for x in nums:
            if x == 1:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return best
        