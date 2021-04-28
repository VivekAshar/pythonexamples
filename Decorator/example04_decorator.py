def my_function_handle_divide(func):
    def my_logic(a,b):
        print("2 numbers entered for division are",a,b)
        if (b == 0):
            print("division is not possible")
            return
        elif (a == 0):
            print("division operation is not needed")
            return 0

        return func(a,b)
    return my_logic

@my_function_handle_divide
def my_function_divide(a, b):
    return (a / b)

#result = my_function_divide(2, 5)
#result = my_function_divide(2, 0)
result = my_function_divide(0, 2)
print("result=", result)