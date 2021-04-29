def my_function_name(val):
    print("Inside function")
    val = [20, 40, 60, 80, 100]
    #print(val)

val = [10, 30, 50, 70, 90]
print("outside function")
my_function_name(val)
print(val)