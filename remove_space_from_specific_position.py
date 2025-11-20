String_input = input("Enter String :")
start = 6
end = 11

before = String_input[: start]
middle = String_input[start:end]
end = String_input[end:]

no_space_string = middle.replace(" ", "")

result= before + no_space_string + end
print(result)