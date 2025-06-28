class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
result = sol.rotate(nums, k)
print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]