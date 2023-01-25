# QUICK SORT

def sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        sort(nums, left, partition_pos - 1)
        sort(nums, partition_pos + 1, right)



nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)