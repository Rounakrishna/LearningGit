def first_missing_positive(nums):
    n = len(nums)
    
    # First, mark all negative values as 'n + 1'
    for i in range(n):
        if nums[i] <= 0:
            nums[i] = n + 1

    # Place each number in its correct position
    for num in nums:
        if 1 <= num <= n:
            nums[num-1] = num
            num=nums[num-1]
            
    # The first place where its number is not correct
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
            
    return n + 1

nums = [3, 4, -1, 1]
print(first_missing_positive(nums))  # Output: 2