def longeststring(s: str) -> int:
    left = 0
    used = {}
    longest = 0
    
    for i in range(len(s)):
        ch = s[i]
    
        if ch in used and used[ch] >= left:
            left = used[ch] + 1
        
        used[ch] = i
        longest = max(longest, i - left + 1)

    return longest

print(longeststring("abcbgshdjeg"))
