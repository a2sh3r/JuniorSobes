from copy import deepcopy
from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        val = nums[i]

        while (i - 1 >= 0) and (nums[i-1] > val):
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1

    return nums


l1 = [3, 99, 4, 2, 1, -1, 11, 1, 1, 1, 1]
print(insertion_sort(l1))