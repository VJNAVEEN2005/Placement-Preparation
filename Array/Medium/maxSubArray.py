class Solution(object):
    def maxSubArray(self, nums):
        maxSum = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum = curSum + i
            maxSum = max(maxSum , curSum)
        return maxSum