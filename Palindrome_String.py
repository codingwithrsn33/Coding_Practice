String_input = input("Enter a String: ")

cleaned = String_input.replace(" ", "").lower()
reversed_string = cleaned[::-1]

if cleaned == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")
