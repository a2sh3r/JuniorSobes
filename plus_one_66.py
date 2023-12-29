from typing import List


def plusOne(digits: List[int]) -> List[int]:
    stock = 1
    for i in range(len(digits)-1, -1, -1):
        if stock == 0:
            if digits[i] + stock > 9:
                digits[i] = 0
                stock = 1
            else:
                digits[i] = digits[i] + stock
                stock = 0
        else:
            if digits[i] + stock > 9:
                digits[i] = 0
                stock = 1
            else:
                digits[i] = digits[i] + stock
                stock = 0
        if i == 0:
            if stock:
                digits.insert(0, 1)
    return digits


nums = [1, 2, 3]
nums2 = [9, 9, 9]
print(plusOne(nums))
print(plusOne(nums2))

