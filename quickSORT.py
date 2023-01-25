# QUICK SORT

def sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        sort(nums, left, partition_pos - 1)
        sort(nums, partition_pos + 1, right)

def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] >= pivot
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)