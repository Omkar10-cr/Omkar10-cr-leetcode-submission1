class Solution:
    def findErrorNums(self, nums):
        dup = -1
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                dup = abs(x)
            else:
                nums[i] = -nums[i]
        missing = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]
        