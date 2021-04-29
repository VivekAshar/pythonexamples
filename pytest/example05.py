'''
def input_val(val1):
    print ('Entered positive value is', val1)

input_val(10)
'''

'''
def input_val(val1):
    print ('Entered positive value is', val1)

input_val(-10)
'''


def input_val(val1):
    assert val1 > 0, "Value has to be greater than 0"
    print ('Entered positive value is', val1)

input_val(6)
