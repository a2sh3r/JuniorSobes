from typing import List


def heap_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    def heapify(nums_: List[int], n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums_[i] < nums_[left]:
            largest = left

        if right < n and nums_[largest] < nums_[right]:
            largest = right

        if largest != i:
            nums_[i], nums_[largest] = nums_[largest], nums_[i]
            heapify(nums_, n, largest)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

    return nums


nums = [1, 4, 2, 9, 8, 5, 1]
print(heap_sort(nums))
