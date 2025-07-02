def SelectionSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i,len(nums)):
            if nums[min_index] > nums[j] :
                min_index = j
        nums[i],nums[min_index] = nums[min_index], nums[i]
    return nums

arr = [2,32,32,21,2,13,42]

print(SelectionSort(arr))