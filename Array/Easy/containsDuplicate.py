class Solution(object):
    def containsDuplicate(self, nums):
        arr = set()
        for i in nums:
            if i not in arr:
                arr.add(i)
            else:
                return True
        return False

nums = [1, 2, 3, 1]
sol = Solution()
k = sol.containsDuplicate(nums)
print(k)  # Output: True