import random

def scramble_word(word_str):
    if len(word_str) < 4:
        return word_str
    #don't scramble 3 or less characters
    
    count = 1
    word_list2 = []
    word_list = list(word_str)

    if word_list[0] < 'A':
        count += 1
        while (count) < len(word_list):
            word_list2.append(word_list[(count)])
            count += 1
        
    if word_list[-1] < 'A':
        while (count+2) < len(word_list):
            word_list2.append(word_list[count])
            count += 1
                        
    else:
        while (count+1) < len(word_list):
            word_list2.append(word_list[count])
            count += 1

    #this appends the middle characters to a new list, takes punctuation
    #at the end into account

    random.shuffle(word_list2)

    #the middle characters are shuffled

    count = 0

    count2 = len(word_list2)

    if (len(word_list) - len(word_list2)) == 3:
        count2 += 1
        
    
    while (count-2) < count2:
        if word_list[count] == "'":
            while word_list2[(count-1)] != word_list[count]:
                random.shuffle(word_list2)
        count += 1

    #if there's an apostrophe, it's position is preserved
    
    count = 0
    string_list = [word_list[0]]

    if word_list[0] < 'A':
        string_list.append(word_list[1])

    while count < len(word_list2):
        string_list.append(word_list2[count])
        count += 1

    count = 0
        
    if word_list[-1] < 'A':
        if word_list[-2] < 'A':
            string_list.append(word_list[-3])
        string_list.append(word_list[-2])

    #depending on the first and last characters, they are appended.
    #additional clauses were added if the first and last characters
    #are not letters
            
    string_list.append(word_list[-1])

    string = ''.join(string_list)
    
    if word_list[0] < 'A':
        if word_list[-1] >= 'A':
            string = string.replace(string[-1],'',1)
        if word_list[-1] < 'A':
            if word_list[-2] < 'A':
                string = string[0] + string[1:(len(string)+1)].replace(string[-3],'',1)
            string = string[0] + string[1:(len(string)+1)].replace(string[-1],'',1)
            if word_list[-2] != word_list[1]:
                string = string[0] + string[1:(len(string)+1)].replace(string[-2],'',1)
            else:
                string = string[0:2] + string[2:(len(string)+1)].replace(string[-2],'',1)

    #this makes sure duplicates aren't included in the string

    return string

def scramble_line(line_str):
    string = ''
    newline = line_str.split()
    for word in newline:
        newword = scramble_word(word)
        string += newword
        string += ' '

    #this simple function take the scramble word function and applies
    #it to every word in the line.
        
    return string
                
def open_read_file(file_name_str):
    keep_going = True
    while keep_going:
        try:
            file_obj = open(file_name_str, 'r')
            keep_going = False
        except IOError:
            print("{:s} is a bad file name, try again".format(in_name))
            file_name_str = input("Open what file to read:")
    return file_obj

    #this function takes the file name inputted by the user
    #and tries to open it, if it does, it returns it

def main():
    out_name = input("Open what file for writing:")
    out_obj = open(out_name, 'w')
    in_name = input("Open what file to read:")
    file_obj = open_read_file(in_name)

    #this function asks for files to open and to write to

    for line in file_obj:
        test = scramble_line(line)
        out_obj.write(test)

    #then it runs the scramble line on the opened file and writes
    #the scrambled line to the new file

main()
