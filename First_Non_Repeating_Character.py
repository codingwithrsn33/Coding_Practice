def first_unique_char(s):
    
    for i in range(len(s)):
        is_unique = True

        
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break

        if is_unique:
            return i

    return -1
