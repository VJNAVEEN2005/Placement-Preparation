class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1 , len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0 :
                    l += 1
                else :
                    result.append([a,nums[l],nums[r]]) 
                    l += 1
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
            
        return result        
        
nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
k = sol.threeSum(nums)
print(k)  # Output: [[-1, -1, 2], [-1, 0, 1]]