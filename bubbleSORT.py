# BUBBLE SORT

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

        print(nums)

nums = [75, 30, 49, 81, 54, 57, 79, 50, 85, 71]
sort(nums)

print("")
print("Sorted Array:", nums)