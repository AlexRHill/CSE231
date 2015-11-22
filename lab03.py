user_str=('start')

max_int=1
count=0
while user_str !='quit':
    print(' ')
    user_str= input ('input a number or type "quit" to exit program: ')

    if user_str.isdigit()==False and user_str != 'quit':
        print('must be an integer or "quit" to exit the program')
        print(' ')
        continue
    elif user_str=='quit':
        continue
    else:
        user_int=int(user_str)

        print('Number is: ',user_int)
        print('Sequence is: ')
        while user_int>1:
            if user_int %2==0:
                user_int=user_int//2
                count+=1
                print(user_int, end=' ')
            else:
                user_int= (user_int*3)+1
                count+=1
                print(user_int, end=' ')
                
            if user_int>max_int:
                max_int=user_int
        print(' ')
        print ('Length was: ',count)
        print ('Largest was: ',max_int)
                
                

                
        




print('Thanks for playing')





        
    
