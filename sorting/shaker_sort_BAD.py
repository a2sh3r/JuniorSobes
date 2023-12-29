from copy import deepcopy
from typing import List


def shaker_sort(nums: List[int]) -> list:
    left = 0
    right = len(nums) - 1
    while left < right:
        for i in range(right, left, -1):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

        for i in range(left + 1, right):
            if nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

        right -= 1
        left += 1

    return nums


l1 = [12, 12, 1, 8, 4]
print(shaker_sort(l1))
