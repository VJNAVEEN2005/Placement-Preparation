def MergeSort(nums):
    if len(nums) > 1 :
        mid = len(nums)//2
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]
        
        MergeSort(leftHalf)
        MergeSort(rightHalf)
        
        i = j = k = 0
        
        while i < len(leftHalf) and j < len(rightHalf) :
            if leftHalf[i] < rightHalf[j] :
                nums[k] = leftHalf[i]
                i += 1
            else:
                nums[k] = rightHalf[j]
                j += 1
            k += 1
            
        while i < len(leftHalf):
            nums[k] = leftHalf[i]
            i += 1
            k += 1
        
        while j < len(rightHalf):
            nums[k] = rightHalf[j]
            j += 1
            k += 1

arr = [1,213,2,3,23,2,234,3]
MergeSort(arr)
print(arr)
    