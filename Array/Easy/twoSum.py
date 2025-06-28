class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map :
                print(map)
                return [i, map[diff]]
            map[nums[i]] = i
                
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
k = sol.twoSum(nums, target)
print(k)  # Output: [1, 0]