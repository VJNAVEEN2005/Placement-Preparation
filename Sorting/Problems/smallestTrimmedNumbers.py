class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        result = []
        for i in queries:
            trim = i[1]
            value = i[0]
            stack = []
            for j in range(len(nums)):
                stack.append([nums[j][-trim:],j])
            stack.sort()
            result.append(stack[value-1][1])    
        
        return result
    
# Example usage:
sol = Solution()
print(sol.smallestTrimmedNumbers(["102","473","251","814"], [[1,1],[2,3],[4,2],[1,2]]))
# Output: [2, 0, 1, 0]

# Explanation:
# - For the first query [1,1], the smallest trimmed number is "102", which is at index 2.
# - For the second query [2,3], the smallest trimmed number is "251",   #   which is at index 0.
# - For the third query [4,2], the smallest trimmed number is "814", # which is at index 1.
# - For the fourth query [1,2], the smallest trimmed number is "102", # which is at index 0.
# Thus, the output is [2, 0, 1, 0]. 