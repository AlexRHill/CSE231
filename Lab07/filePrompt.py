# wfp, 6/8/07
# continuous file prompt
# wfp, 2/4/13, added function, cleaned up for py3

#function to repeatedly ask for a file to open 
#continues to prompt until a file opens successfully
def open_file(file_name_str, mode_str):
    opened_file_bool = False
    while (not opened_file_bool):
        try:
            file_obj = open(file_name_str, mode_str)
            opened_file_bool = True   # only executed after file opens
        except IOError:
            print("Bad file name, try again ")
            file_name_str = input("What file???") #reprompt, bad file
    else:
        return(file_obj)
        
# open a file for reading
file_str = input("Read what file:")
file_read_obj = open_file(file_str, 'r')

# open a file for writing
file_str = input("Write to what file:")
file_write_obj = open_file(file_str, 'w')

# write the reversed lines
for line_str in file_read_obj:
    line_str = line_str.strip()
    reverse_str = line_str[::-1]
    file_write_obj.write(reverse_str+'\n')
    
file_read_obj.close()
file_write_obj.close()
    



