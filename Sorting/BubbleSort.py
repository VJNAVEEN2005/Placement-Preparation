def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1] , nums[j]
    return nums

arr = [2,32,23,24,3,2,42]

print(BubbleSort(arr))