# SELECTION SORT

def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print(nums)