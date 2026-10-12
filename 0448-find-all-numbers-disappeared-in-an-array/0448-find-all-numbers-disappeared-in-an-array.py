class Solution(object):
    def findDisappearedNumbers(self, nums):
        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]
        return [i + 1 for i, v in enumerate(nums) if v > 0]
        