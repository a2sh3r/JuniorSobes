from typing import List
from collections import deque


def solve(nums: List[int], k: int) -> float:
    pool = deque()
    avg = 0
    left = 0
    for right in range(len(nums)):
        if right < k:
            avg = (avg * len(pool) + nums[right]) / (len(pool) + 1)
            pool.append(nums[right])
        else:
            avg = (avg * len(pool) - nums[left] + nums[right]) / (len(pool))
            left += 1
            pool.popleft()
            pool.append(nums[right])
            max_avg = max(max_avg, avg)
        if right == k-1:
            max_avg = avg

    return max_avg


nums = [4,0,4,3,3]

k = 5

print(solve(nums, k))
