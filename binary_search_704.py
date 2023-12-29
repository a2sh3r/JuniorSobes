from typing import List


def search(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) -1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return True
    return False


nums = [-1,0,3,5,9,12]
target = 13
print(search(nums, target))
