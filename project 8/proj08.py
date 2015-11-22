  ##################################################################
  #  Section 001H
  #  Computer Project #8
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################


import string

def fill_completions(c_dict, fd):
    for line in fd:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
#this cuts the words in the lines down to just the letters
            count = 0
            if word.isalpha() == False:
                break
            if len(word) == 1:
                break
#if there are non alphabetic characters, or the word is only 1 long, we
#don't care about it
            
            while count < len(word):
                if (count,word[count]) in c_dict:
                    c_dict[(count,word[count])].add(word)
                else:
                    c_dict[(count,word[count])] = set()
                    c_dict[(count,word[count])].add(word)
#we add the word to the matching set in the dictionary depending on
#where each letter is located

                count += 1


def find_completions(prefix, c_dict):
    count = 0
    set3 = c_dict[(count,prefix[count])]
    while count < len(prefix):
        set3 = set3&c_dict[(count,prefix[count])]
        count += 1
#this takes the set that goes with each letter of the prefix and checks
#the intersection of that set with every other letter in the prefix
    return set3       
        
    

def main():
    my_dict = {}
    file_str = "ap_docs.txt"
    f_obj = open(file_str)
    fill_completions(my_dict, f_obj)
    f_obj.close()
#this just fills the dictionary with the provided file

    while True:
        prefix = str(input("Give me a prefix to complete: (press '#' to quit) "))
        if prefix == "#":
            break
        set3 = find_completions(prefix, my_dict)
        if set3 != set():
            print(set3)
        else:
            print("Prefix has no completions.")
#this repeatedly prompts the user for a prefix and prints the possible
#words. if none are found, it says so.      
    

main()
