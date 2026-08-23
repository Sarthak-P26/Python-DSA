def maxSubArray(nums):
    sums = 0
    total_sum = sum(nums)
    if len(nums) == 1:
        return nums[0]
    if len(nums) ==2:
        return max(nums[0], nums[1], total_sum)
    for i in range(len(nums)):
        for j in range(0, len(nums)):
            new_sum = sum(nums[i:j])
            if sums < new_sum :
                sums = new_sum
    if total_sum < sums:            
        return sums
    else:
        return sum(nums)
        
    return sum(array)


# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
result = maxSubArray([-2,-3,-1])
print(result)