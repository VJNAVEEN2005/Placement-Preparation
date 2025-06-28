class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i
        return result
    
nums = [4, 1, 2, 1, 2]
sol = Solution()
k = sol.singleNumber(nums)
print(k)  # Output: 4