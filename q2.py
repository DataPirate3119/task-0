def process_list(numbers):
    res=numbers.copy()
    for i in numbers:
        if i<0:
            res.remove(i)
    res.append(0)
    res.sort()
    return res

original=[5,-2,8,-1,3]
result=process_list(original)
print("Original: ", original)
print("Result: ", result)
