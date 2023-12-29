def longestNiceSubstring(s: str) -> str:
    i = j = 0
    pool = []
    while j < len(s):
        if s[j] not in pool:
            pool.append(j)
            j += 1
        elif s[j].lower() in pool and s[j].isupper():
            pool.remove(i)
            i += 1
            j += 1
    return pool
