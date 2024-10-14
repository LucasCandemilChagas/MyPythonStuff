def myfunc(s):
    result = ''
    for index,value in enumerate(s): 
        if index%2!=0:
            result = result+value.upper()
        else:
            result = result+value
    return result 

print(myfunc('antropomorphism'))
    