def get_and_strip_number(s):
    """Requires:
       -- string s consists of (the string representing) a non-negative integer n followed
          by a single space, and then n words, each separated from the next by a single space
       Returns:
       -- the leading integer n (as an int), and
       -- the string of words following the leadine integer, starting with the first
            character of the first word"""
    integer = s.find(' ')
    #print(integer)
    if integer > 0:
        s1 = int(s[:integer])
        s2 = s[(integer + 1):]
    elif integer < 0:
        s1 = s
        s2 = ''
    #print(s1)
    #print(s2)
    return s1, s2

def get_and_strip_word(s):
    """Requires:
       -- string s has no leading spaces, and is either empty or
          consists of one or more words, each separated from the next by a single space
       Returns:
       -- first word of s, and
       -- the "rest" of s, i.e. what is left after stripping off the word and, if
          there is one, the space following the word"""
    integer = s.find(' ')
    #print(integer)
    if integer > 0:
        s1 = s[:integer]
        s2 = s[(integer + 1):]
    elif integer < 0:
        s1 = s
        s2 = ''
    #print(s1)
    #print(s2)
    return s1, s2
    
def pad_words(s, num_words, final_len):
    """Requires:
       -- final_len > len(s)
       -- string s consists of num_words words, each separated by a single space
       Returns:
       -- string r, containing the words in s evenly padded with spaces to make
          len(r) == final_len"""
    if num_words <= 1:      # best we can do is fill out the line with spaces
        return s + ((final_len - len(s))*' ')

    # there are at least 2 words, so at least one pigeon hole to fill (with spaces)
    num_pigeon_holes = num_words - 1                        # the buckets (pigeon holes) are between words
    num_pigeons = final_len - (len(s) - num_pigeon_holes)   # my pigeons are spaces
    pad_num = num_pigeons // num_pigeon_holes
    extra_num = num_pigeons % num_pigeon_holes              # number of holes that get an extra pigeon
    working_str = ''
    
    # take care of the first num_pigeon_holes - extra_num holes
    for i in range(num_pigeon_holes - extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + (pad_num * ' ')   # insert pad_num spaces

    # take care of the last extra_num holes
    for i in range(extra_num):
        word, s = get_and_strip_word(s)
        working_str += word + ((pad_num + 1) * ' ')

    working_str += s
    return working_str

def main():
    """Main program for testing some text formatting functions."""
    file_name = input("Enter the name of the input file: ")
    file_obj = open(file_name, "r")

    print("Line length should be as long as the longest line to print, or longer.") 
    line_len = int(input("Enter the desired line length: "))
    print()

    for line in file_obj:
        line = line.strip()                   # strip the trailing '\n'
        n, words = get_and_strip_number(line)
        print(pad_words(words, n, line_len))

    file_obj.close()

    
          
