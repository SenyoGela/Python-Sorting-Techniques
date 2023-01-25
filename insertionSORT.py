# INSERTION SORT

def sort(nums):
    for i in range(1, len(nums)):
        j = i
        while nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)