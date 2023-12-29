""" Скользящее окно """


def longest_substring(s: str) -> int:
    char_set = set()
    max_len = 0
    left = right = 0
    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1
    return max_len


s = "abcabcbb"
print(longest_substring(s))
