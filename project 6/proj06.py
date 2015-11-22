  ##################################################################
  #  Section 001H
  #  Computer Project #6
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################
          
def get_input_descriptor():
    main = False
    while (not main):
        try:
            open_file_name = input("What file do I open? ")
            fileobj = open(open_file_name,'r')
            main = True
        except IOError:
            print("Bad file name. Try again!")
            
        return fileobj

#this function checks for the file the user wants to open and if it
#can be opened, it then returns the file name to be used in main


    def get_data_list(file_object, column_number):
    data_list = []
    fileobj1 = file_object.readline()
#we check to see if the first line is usable by the rest of the program
    for line in file_object:
        test = line.strip()
        test2 = test.split(',')
#the lines are split into lists and split along the commas that separate
#the values
        date = test2[0]
        column_data = test2[column_number]
#we are only concerned with the column that is inputted by the user
        data_tuple = date,column_data        
        data_list.append(data_tuple)
    sorted_list = sorted(data_list)
    return sorted_list
#we append the tuple of date and number (from the specified column) to the list,
#sort it, and return it to be used by the


def average_data(list_of_tuples):
    count = 0
    number = 0
    datea = list_of_tuples[0][0]
    date2a = datea.split('-')
    date4 = str(date2a[1] + ':' + date2a[0])
    data_average = 0
    list2 = []
    average_count = 0
    while count < len(list_of_tuples):
#this was a bit tricky to make, basically, we check every single tuple and
#change the date in each one. When the dates are from the same month, the value
#associated is added to the average number.
        date = list_of_tuples[count][0]
        date2 = date.split('-')
        date3 = str(date2[1] + ':' + date2[0])
        if date3 == date4:
            data_average += float(list_of_tuples[count][1])
            average_count += 1
#then, the average count is updated so we know how many to divide the average
#number by in the end.
        else:
#when the dates change to a different month, we calculate the average, and
#append the average and the date to the list as a tuple. Then we start again.
            data_average2 = round(data_average/average_count,2)
            tuple_1 = data_average2,date4
            list2.append(tuple_1)
            average_count = 0
            data_average = 0
            data_average += float(list_of_tuples[count][1])
            average_count += 1
        count += 1
#this count is what eventually tells us when we finish the whole list
        date4 = date3

    data_average2 = round(data_average/average_count,2)
    tuple_1 = data_average2,date4
    list2.append(tuple_1)
    sorted_list2 = sorted(list2)
    return sorted_list2
#when we're all done, we finish the list, sort it, and return it to be used

  
def main():
    fileobj = get_input_descriptor()
    column_int = int(input("Which column? (must be between 0-6) "))
    sorted_list = get_data_list(fileobj, column_int)
    list_of_tuples = average_data(sorted_list)
#we run all of our other functions here and get the values we need
    print("")
    print("Lowest 6 values for column",column_int)
    print("Date:",list_of_tuples[0][1],"| Value:",list_of_tuples[0][0])
    print("Date:",list_of_tuples[1][1],"| Value:",list_of_tuples[1][0])
    print("Date:",list_of_tuples[2][1],"| Value:",list_of_tuples[2][0])
    print("Date:",list_of_tuples[3][1],"| Value:",list_of_tuples[3][0])
    print("Date:",list_of_tuples[4][1],"| Value:",list_of_tuples[4][0])
    print("Date:",list_of_tuples[5][1],"| Value:",list_of_tuples[5][0])
#since the list is sorted, we can easily find the lowest 6 values
    print("")
    print("Highest 6 values for column",column_int)
    print("Date:",list_of_tuples[-1][1],"| Value:",list_of_tuples[-1][0])
    print("Date:",list_of_tuples[-2][1],"| Value:",list_of_tuples[-2][0])
    print("Date:",list_of_tuples[-3][1],"| Value:",list_of_tuples[-3][0])
    print("Date:",list_of_tuples[-4][1],"| Value:",list_of_tuples[-4][0])
    print("Date:",list_of_tuples[-5][1],"| Value:",list_of_tuples[-5][0])
    print("Date:",list_of_tuples[-6][1],"| Value:",list_of_tuples[-6][0])
#and the highest 6 values
  
main()
#we run it and we're done
