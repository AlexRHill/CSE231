# try exception flow
# wfp, 11/26
# wfp, 2/4/13, updated

try:
    value_str = input('Enter a denominator: ')
    denom_int = int(value_str)
    print('The denominator is: ',denom_int)
    result_float = 10/denom_int
    print("10 divided by {:d} is {:4.2f}".format(denom_int, result_float))
    
except ValueError:
    print("couldn't convert input to an int")
    
except ZeroDivisionError:
    print("hey, you can't divide by zero")

print('Here we are at the end')
