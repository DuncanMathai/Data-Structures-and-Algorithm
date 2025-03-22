def rotate(nums, k):
    n = len(nums)
    k %= n  # To handle cases where k > n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
