from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if i < len(left):
        sorted_list += left[i:]

    if j < len(right):
        sorted_list += right[j:]

    return sorted_list


nums = [9, 1, 8, 2, 7, 3, 6, 4, 5]

print(merge_sort(nums))
