small_list = [1, 3, 5, 7, 9]
large_list = [0, 2, 4, 6, 8, 10]

small_index = large_index = 0

result = []

while large_index < len(large_list) and small_index < len(small_list):
    element_from_large = large_list[large_index]
    element_from_small = small_list[small_index]

    if element_from_large <= element_from_small:
        result.append(element_from_large)
        large_index += 1
    else:
        result.append(element_from_small)
        small_index += 1

result += large_list[large_index:] + small_list[small_index:]

print(result)