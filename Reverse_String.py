String_input = input("Enter a String: ")
reversed_string = " "

for i in range(len(String_input)-1,-1,-1):
    reversed_string += String_input[i]
print(" Reversed String be :", reversed_string)