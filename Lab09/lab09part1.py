import string


def print_index(f_obj):
    my_dict = {}
    count = 1
    for line in f_obj:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            if word:
                if word in my_dict:
                    b_set = my_dict[word]
                    b_set.add(count)
                else:
                    a_set = set()
                    a_set.add(count)
                    my_dict[word]=a_set

        count += 1

    pairs_list = []
    for key,value in my_dict.items():
        pairs_list.append((key, value))
    print('Words in alphabetical order as word:count pairs')
    pairs_list.sort()
    print_cols = 0

    for word,cnt in pairs_list:
        print((word,cnt), end=' ')
        if print_cols == 0:
            print()
            print_cols = 0
        else:
            print_cols += 1


def compare_files(f_obj, g_obj):
    #count = 0
    #count2 = 0
    set1 = set()
    set2 = set()
    for line in f_obj:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            if word != '':
                set1.add(word)
        for line in g_obj:
            line = line.strip()
            word_list = line.split()
            for word in word_list:
                word = word.lower()
                word = word.strip(string.punctuation)
                if word != '':
                    set2.add(word)

    combined_set = set1 & set2
    union_set = set1 | set2
    
    print("Common words:",len(combined_set))
    print("Total words:",len(union_set))

def main():
    file_str = input('What file:')
    f_obj = open(file_str)
    file2_str = input('What file:')
    g_obj = open(file2_str)
    #print_index(f_obj)
    compare_files(f_obj, g_obj)
    
    f_obj.close()
    #print('There were %d words in the file %s'%(len(my_dict),file_str))
    #print_alphabetic(my_dict)
    #print_frequency(my_dict)
    #return my_dict

main()
