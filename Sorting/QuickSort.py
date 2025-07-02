def QuickSort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1
    if low < high :
        pivot = partition(nums,low,high)
        QuickSort(nums,low,pivot-1)
        QuickSort(nums,pivot+1,high)    
        
def partition(nums,low,high):
    pivot = nums[high]
    i = low - 1
    for j in range(low,high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1] , nums[high] = nums[high] , nums[i+1]
    return i+1

arr = [12,32,3,2,4,245,4]
QuickSort(arr)
print(arr)