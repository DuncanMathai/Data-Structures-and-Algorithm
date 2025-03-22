def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1  # New length of array

# Example usage:
nums = [1, 1, 2]
new_length = removeDuplicates(nums)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [1, 2]
