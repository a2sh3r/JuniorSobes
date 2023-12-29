from typing import List


def solve(nums: List[int], val: int) -> int:
    j = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

nums = [3,1,2,3,2]
print(solve(nums, 3))
