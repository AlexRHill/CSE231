def read_student(line):
    scores = line.strip()
    scores2 = scores.split()
    name = scores2[0]
    scores2 = scores2[1:]
    length = len(scores2)
    while len(scores2) < 8:
        scores2.append('0')
    while len(scores2) > 8:
        scores2 = scores2[1:]
    average = (int(scores2[0]) + int(scores2[1]) + int(scores2[2]) + int(scores2[3])
                   + int(scores2[4]) + int(scores2[5]) + int(scores2[6]) + int(scores2[7])
                   )/8
    average = round(average, 2)
    string = str(name) + " " + str(length) + " " + str(average) 
    return(string)
    


def process_file(fileobj, file_obj_out):
    fileobj1 = fileobj.readline()
    for line in fileobj:
        print_str = read_student(line)
        file_obj_out.write(print_str)


def main():
    main = False
    while (not main):
        try:
            open_file_name = input("what file do I open? ")
            fileobj = open(open_file_name,'r')
            main = True
        except IOError:
            print("you goofed")

    output_file_name = input("where do I save?")
    file_obj_out = open(output_file_name, "w")

    process_file(fileobj, file_obj_out)

main()


        

