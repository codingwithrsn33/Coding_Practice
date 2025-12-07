def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]
nums=[11,22,33,44,55]
print(second_largest(nums))
