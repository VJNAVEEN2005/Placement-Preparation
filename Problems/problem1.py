def isCanBeSolved(nums):
    arr = []
    while nums:
        arr.append(nums % 10)
        nums = nums // 10
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return 0
    
    if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] == arr[2]:
        if arr[0] == arr[1] :
            num1 = arr[0]
            num2 = arr[2]
        elif arr[1] == arr[2]:
            num1 = arr[1]
            num2 = arr[0]
        else:
            num1 = arr[0]
            num2 = arr[1]
            
        count = 0    
        while num1 != num2:
            if num1 > num2:
                return -1
            else:
                num1 += 1
                num2 -= 1
                count += 1
        return count
    else:
        return -1
        
nums = 117
print(isCanBeSolved(nums))  
