from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    max_val = max(nums)

    count_list = [0] * (max_val + 1)

    for num in nums:
        count_list[num] += 1

    sorted_list = []

    for index, count in enumerate(count_list):
        if count:
            sorted_list += [index] * count

    return sorted_list


nums = [1, 9, 8, 3, 3]
print(counting_sort(nums))