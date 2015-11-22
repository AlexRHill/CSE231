
def make_new_row(old_row):
    if old_row == []:
        return [1]
    elif old_row == [1]:
        return [1,1]
    #this is basically error checking
    
    new_row = [1]
    count = 1
    while (count) < len(old_row):
        new_int = old_row[(count-1)] + old_row[count]
        new_row.append(new_int)
        count+=1
        #add the numbers, append to the end
    new_row.append(1)
    
    return new_row

test = make_new_row([])

print(test)
"""Requires:
       -- list old_row that begins and ends with a 1 and has zero or more
          integers in between (has to have at least [1,1])
       Returns:
       -- list beginning and ending with a 1 and each interior (non 1)
          integer is the sum of the corresponding old_row elements
          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """

    
