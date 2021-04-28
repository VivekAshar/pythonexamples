def my_function_one(val1):
    def my_function_two(val2):
        return val1 * val2
    return my_function_two

my_result = my_function_one(10)
result = my_result(20)

print("result=",result)



