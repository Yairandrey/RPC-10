def max_consecutive_letters(s, m):
    n = len(s)
    max_streak = 0
    char_count = {}
    left = 0

    for right in range(n):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        window_size = right - left + 1
        max_count = max(char_count.values())
        to_remove = window_size - max_count
        while to_remove > m:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            window_size = right - left + 1
            max_count = max(char_count.values())
            to_remove = window_size - max_count
        max_streak = max(max_streak, max_count)
    return max_streak

s = input().strip()
m = int(input())

result = max_consecutive_letters(s, m)
print(result)