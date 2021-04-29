def my_function_name(val):
    return lambda val1 : val1 * val

myresult = my_function_name(10)
print(myresult)
print(myresult(20))
