class Solution:
    def smallerNumbersThanCurrent(self, nums):
        cnt = [0] * 102
        for x in nums:
            cnt[x + 1] += 1
        for v in range(1, 102):
            cnt[v] += cnt[v - 1]
        return [cnt[x] for x in nums]