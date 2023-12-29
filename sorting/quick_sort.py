from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    support_sum = nums[0]
    left = [i for i in nums if i < support_sum]
    mid = [i for i in nums if i == support_sum]
    right = [i for i in nums if i > support_sum]

    return quick_sort(left) + mid + quick_sort(right)


nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print(quick_sort(nums))
