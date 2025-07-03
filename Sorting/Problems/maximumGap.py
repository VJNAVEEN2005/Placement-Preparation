# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2 :
            return 0
        
        max = 0
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] > max :
                max = nums[i] - nums[i-1]
        return max
        
        
# Example usage:# 
sol = Solution()
print(sol.maximumGap([3,6,9,1]))

# Output: 3
# Explanation: The maximum gap is between 6 and 9, which is 3.
