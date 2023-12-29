"""Алгоритм Кнута-Морриса-Пратта КМП"""


def strStr(haystack: str, needle: str) -> int:
    h_len, n_len = len(haystack), len(needle)

    p = [0] * n_len
    j = 0
    i = 1

    while i < n_len:
        if needle[j] == needle[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]

    j = 0

    for i in range(h_len):
        while j > 0 and needle[j] != haystack[i]:
            j = p[j - 1]
        if needle[j] == haystack[i]:
            j += 1
        if j == len(needle):
            return i - j + 1

    return -1


haystack = "asssadbutsad"
needle = "sad"
print(strStr(haystack, needle))
