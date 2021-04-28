def add(val1):
    return val1 + 10

def sub(val1):
    return val1 - 10

def job(func,val2):
    result = func(val2)
    print(result)

job(add,100)
job(sub,100)