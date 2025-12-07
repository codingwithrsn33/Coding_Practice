def non_repeated_character(list):
    result=[]
    
    for x in list:
        if list.count(x) == 1:
            result.append(x)
    
    return result

list=[1,2,2,3,4,4]
print(non_repeated_character(list))
