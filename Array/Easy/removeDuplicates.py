class Solution(object):
    def removeDuplicates(self, nums):
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
        print(arr)
        nums[:] = arr
        return len(arr)

nums = [1, 1, 2]
sol = Solution()
k = sol.removeDuplicates(nums)
print(nums[:k])  # Output: [1, 2]
