file_str = input("Enter me a file to open: ")

try:
    file_obj = open(file_str, 'r')
    print("Opened the file",file_str)    # executed if no error
except IOError:
    print("File opening failed")         # executed on file open error

print("moving on")                       # always executed
