# SELECTION SORT

def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
