def InsertionSort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j - 1] , nums[j] = nums[j] , nums[j - 1]
            j -= 1
    return nums

arr = [12,32,3,23,242,2]
print(InsertionSort(arr))