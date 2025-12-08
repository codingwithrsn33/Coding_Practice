text = input("Enter Words :")
words = text.split()
reversed_string= words[:: -1]

output =" ".join(reversed_string)

print(output)
