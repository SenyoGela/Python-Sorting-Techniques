# MERGE SORT

def sort(nums):
    if len(nums) > 1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

        # recursion
        sort(left_nums)
        sort(right_nums)

        # merge
        i = 0   # left nums index
        j = 0   # right nums index
        k = 0   # merged array index
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
                k += 1
            else:
                nums[k] = right_nums[j]
                j += 1
                k += 1

        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1

        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1

    print(nums)

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)