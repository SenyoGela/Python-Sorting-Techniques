# MERGE SORT

def sort(nums):
    if len(nums) > 1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

        sort(left_nums)
        sort(right_nums)

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)