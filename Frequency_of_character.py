String_input = input("Enter a String :")
Freq = {}

for ch in String_input:
    if ch in Freq:
        Freq[ch] += 1
    else:
        Freq[ch] = 0
for key,value in Freq.items():
    print(key, " :", value)