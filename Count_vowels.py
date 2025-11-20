String_input = input("Enter a String: ")
Count = 0
vowels = "aeiouAEIOU"

for ch in String_input:
    if ch in vowels:
        Count += 1
print("Number of Vowels in the String is :", Count)