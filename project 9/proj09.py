  ##################################################################
  #  Section 001H
  #  Computer Project #9
  #  Percentage contribution:
  #  hillale5        100%
  ##################################################################


import cardsBasic

def setup():
    """
    paramaters: None
    returns:
    - a foundation (list of 4 empty lists)
    - cell (list of 4 empty lists)
    - a tableau (a list of 10 lists, the dealt cards)
    """
    my_deck = cardsBasic.Deck()
    my_deck.shuffle()
#this gets the cards ready to be dealt
    
    tableau1_list=[]
    tableau2_list=[]
    for i in range(6):
        tableau1_list.append(my_deck.deal())
        tableau2_list.append(my_deck.deal())
#the first 2 tableaus have 6 cards each
        
    tableau3_list=[]
    tableau4_list=[]
    tableau5_list=[]
    tableau6_list=[]
    tableau7_list=[]
    tableau8_list=[]
    tableau9_list=[]
    tableau10_list=[]
    for i in range(5):
        tableau3_list.append(my_deck.deal())
        tableau4_list.append(my_deck.deal())
        tableau5_list.append(my_deck.deal())
        tableau6_list.append(my_deck.deal())
        tableau7_list.append(my_deck.deal())
        tableau8_list.append(my_deck.deal())
        tableau9_list.append(my_deck.deal())
        tableau10_list.append(my_deck.deal())
#the rest have 5  cards

    foundation = [[],[],[],[]]
    tableau = [tableau1_list,tableau2_list,tableau3_list,tableau4_list,tableau5_list,
               tableau6_list,tableau7_list,tableau8_list,tableau9_list,tableau10_list]
    cell = [[],[],[],[]]
#the lists for foundation, tableau, and cell are defined and returned
    
    return foundation,tableau,cell


def move_to_foundation(tableau,foundation,t_col,f_col):
    '''
    parameters: a tableau, a foundation, column of tableau, column of foundation
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a column of foundation
    This function can also be used to move a card from cell to foundation
    '''
    
    if foundation[(int(f_col)-1)] == []:
        if tableau[int(t_col)-1][-1].get_rank() == 1:
            return True
#if the foundation is empty and the card being moved is an Ace, move is valid
        
    elif tableau[int(t_col)-1][-1].get_suit() != foundation[(int(f_col)-1)][-1].get_suit():
        return False
#if the suits are different, move isn't valid
    
    elif tableau[int(t_col)-1][-1].get_rank() - foundation[(int(f_col)-1)][-1].get_rank() == 1:
        return True
#if they're the same suit and the card being moved is 1 more than the card on
#the tableau, move is valid

def move_to_cell(tableau,cell,t_col,c_col):
    '''
    parameters: a tableau, a cell, column of tableau, column of cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card at the end of a column of tableau to a cell
    '''
    if cell[(c_col-1)] == []:
        return True
#if the cell is empty, move is valid. only way this can work.
    
    else:
        return False

def move_to_tableau(tableau,cell,c_col,t_col):
    '''
    parameters: a tableau, a cell, column of tableau, a cell
    returns: Boolean (True if the move is valid, False otherwise)
    moves a card in the cell to a column of tableau
    remember to check validity of move
    '''
    if cell[(c_col-1)] == []:
        return False
#if the cell is empty, the move is not valid
    
    elif tableau[(int(t_col)-1)] == []:
        if cell[int(c_col)-1].get_rank() == 13:
            return True
#if the tableau is empty, only a king can be moved to it
        
    elif tableau[int(t_col)-1][-1].get_suit() != cell[(int(c_col)-1)][0].get_suit():
        return False
#if the cards are different suits, the move is not valid
        
    elif tableau[int(t_col)-1][-1].get_rank() - cell[(int(c_col)-1)][0].get_rank() == 1:
        return True
#if the ranks are 1 away in descending order, the move is valid
    
    else:
        return False        

def is_winner(foundation):
    '''
    parameters: a foundation
    return: Boolean
    '''
    if foundation[0] == []:
        return False
    elif foundation[1] == []:
        return False
    elif foundation[2] == []:
        return False
    elif foundation[3] == []:
        return False
#if any foundation is empty, no winner. this accounts for index errors
    
    elif foundation[0][-1].get_value() == 13:
        if foundation[1][-1].get_value() == 13:
            if foundation[2][-1].get_value() == 13:
                if foundation[3][-1].get_value() == 13:
                    print("You won! You are really awesome!")
                    return True
#if the top card on every foundation is a king, the player wins.
                
    else:
        return False


def move_in_tableau(tableau,t_col_source,t_col_dest):
    '''
    parameters: a tableau, the source tableau column and the destination tableau column
    returns: Boolean
    move card from one tableau column to another
    remember to check validity of move
    '''
    if tableau[(t_col_source-1)] == []:
        return False
#if there is no card being moved, the move is not valid
    
    elif tableau[(int(t_col_dest)-1)] == []:
        if tableau[int(t_col_source)-1][-1].get_rank() == 13:
            return True
#if the tableau is empty, only a king can be moved
        
    elif tableau[int(t_col_dest)-1][-1].get_suit() != tableau[(int(t_col_source)-1)][-1].get_suit():
        return False
#if the suits are different, the move is not valid
        
    elif tableau[int(t_col_dest)-1][-1].get_rank() - tableau[(int(t_col_source)-1)][-1].get_rank() == 1:
        return True
#if the cards are in the right descending order, the move is valid
    
    else:
        return False        
        
def print_game(foundation, tableau,cell):
#function was included
    """
    parameters: a tableau, a foundation and a cell
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  
        b) print foundation ( can print the top card only)
        c) print cells

    """
    cell_found = '''
      F1      F2      C1      C2      C3      C4      F3      F4
'''
    print(cell_found)

    row = ''
    for stack in foundation[0:2]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''
            
    for c in cell:
        
        try:
            row += '%8s' % c[0]
        except IndexError:
            row += '%8s' % ''
            
    row = row+ ' '
    for stack in foundation[2:]:
        try:
            row += '%8s' % stack[-1]
        except IndexError:
            row += '%8s' % ''

    print (row)
    print ('----------')


    
    print ("Tableau")
    row = ''
    for i in range(len(tableau)):
        row += '%8s' % (i + 1)
    print (row)

    """find the length of the longest stack"""
    stack_length = []
    for stack in tableau:
        stack_length.append(len(stack))
    max_length = max(stack_length)

    for i in range(max_length):
        row = ''                    # remember to clear the row
        for stack in tableau:
            try:
                row += '%8s' % stack[i]
            except IndexError:
                row += '%8s' % ''
        print (row)
    print ('----------')

def print_rules():
#function was included
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    to_print ='''Rules of Seahaven Towers

    a. Only one card at a time can be moved.
    b. Foundation
        Each foundation holds only one suit and is built up from Ace to King.
        You can move a card to the foundation from a cell or the tableau.
        Once a card is on the foundation it cannot be moved off.
    c. Tableau 
        i. The card at the bottom of a column may be moved to an open cell,
           a foundation or another column of the tableau.
        ii. Moving a card to a tableau column follows these rules
            1. A card can only be moved to the bottom of a column
            2. When you move a card to a column in the tableau you can only
               build down by rank and by the same color. For example, you
               can move a Two of Hearts onto a Three of Hearts (the pile goes
               down by rank, and same color)
        iii. Empty columns may be filled only by a King with any color.
    d. Cell
        i. One cell spot can only contain 1 card
        ii. The card may be moved to the tableau or the foundation.
'''
    print(to_print)

def show_help():
#function was included
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    response ='''
    Responses are:
    --------------
         t2f T F   - move from Tableau T to Foundation F (T and F are ints)
	 t2c T C   - move from Tableau T to Cell C (T and C are ints)
	 t2t T1 T2 - move from Tableau T1 to Tableau T2 (T1 and T2 are ints)
	 c2t C T   - move from Cell C to Tableau T (C and T are ints)
	 c2f C F   - move from Cell C to Foundation F (C and F are ints)
	 'h' for help
	 'q' to quit
         '''
    print (response)
         

        
def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    print_rules()
    foundation, tableau, cell = setup()
    show_help()
#this calls the functions that set the game up
       
    while True:
        print_game(foundation, tableau, cell)
        response = input("Command (type 'h' for help): ")
        response = response.strip()
        response_list = response.split()
#this checks for user response and splits it into the components

        if len(response_list) == 0:
            print("Invalid response.")
            continue

        if len(response_list) == 1:
            if response_list[0] == 'q':
                break
#if q, quit
            elif response_list[0] == 'h':
                show_help()
                continue
#if h, show the help and restart the loop

            else:
                print("Invalid response, hit h if you need help.")
                continue

        if len(response_list) == 2:
            print("Invalid response, hit h if you need help.")
            continue

        if len(response_list) > 3:
            print("Invalid response, hit h if you need help.")
            continue

#if the response is not exactly 3 characters long, reprompt.
        
        if len(response_list) > 1:
            r = response_list[0]
            
            if response_list[1].isdigit() == False:
                print("Invalid response, hit h if you need help.")
                continue

            r1 = int(response_list[1])
            if r1 == 0:
                print("Illegal selection, choose another.")
                continue
            use1 = (r1 - 1)

            if response_list[2].isdigit() == False:
                print("Invalid response, hit h if you need help.")
                continue

            r2 = int(response_list[2])
            if r2 == 0:
                print("Illegal selection, choose another.")
                continue
            use2 = (r2 - 1)

#each component of the response is assigned to a variable for use
#if they aren't digits or they are 0, user is reprompted
            
            if r == 't2f':
                if r1 > 10:
                    print("Invalid selection, choose another.")
                    continue
                elif r1 < 1:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 > 4:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 < 1:
                    print("Invalid selection, choose another.")
                    continue
#this error checking is included in all of the coming statements.
#if the response is not in the range that is expected, user is reprompted


                boolean = move_to_foundation(tableau, foundation, r1, r2)
                if boolean == True:
                    foundation[use2].append(tableau[use1][-1])
                    tableau[use1] = tableau[use1][0:-1]
#if the move is valid, it is done. tableau to foundation
                    
                else:
                    print("Illegal move, choose another.")
                    
            elif r == 't2t':
                if r1 > 10:
                    print("Invalid selection, choose another.")
                    continue
                elif r1 < 1:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 > 10:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 < 1:
                    print("Invalid selection, choose another.")
                    continue

                boolean = move_in_tableau(tableau,r1,r2)
                if boolean == True:
                    tableau[use2].append(tableau[use1][-1])
                    tableau[use1] = tableau[use1][0:-1]
#same as above but from tableau to other tableau
                else:
                    print("Illegal move, choose another.")

            
            elif r == 't2c':
                if r1 > 10:
                    print("Invalid selection, choose another.")
                    continue
                elif r1 < 1:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 > 4:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 < 1:
                    print("Invalid selection, choose another.")
                    continue

                boolean = move_to_cell(tableau,cell,r1,r2)
                if boolean == True:
                    cell[use2].append(tableau[use1][-1])
                    tableau[use1] = tableau[use1][0:-1]
#same as above but tableau to cell
                else:
                    print("Illegal move, choose another.")
                    
            elif r == 'c2t':
                if r1 > 4:
                    print("Invalid selection, choose another.")
                    continue
                elif r1 < 1:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 > 10:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 < 1:
                    print("Invalid selection, choose another.")
                    continue
                        
                boolean = move_to_tableau(tableau,cell,r1,r2)
                if boolean == True:
                    tableau[use2].append(cell[use1][0])
                    cell[use1] = []
#same as above but cell to tableau. cell is emptied as only 1 card in a cell
                else:
                    print("Illegal move, choose another.")

            elif r == 'c2f':
                if r1 > 4:
                    print("Invalid selection, choose another.")
                    continue
                elif r1 < 1:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 > 4:
                    print("Invalid selection, choose another.")
                    continue
                elif r2 < 1:
                    print("Invalid selection, choose another.")
                    continue

                boolean = move_to_foundation(cell, foundation, r1, r2)
                if boolean == True:
                    foundation[use2].append(cell[use1][-1])
                    cell[use1] = []
#same as above but cell to foundation
                else:
                    print("Illegal move, choose another.")
                    
            else:
                print('Unknown command:',r)
                #if the command is not recognized, it is printed and reprompt
                
        else:
            print("Unknown Command:",response)
            
        boolean = is_winner(foundation)
        if boolean == True:
                break
        #the function always checks for a winner. if it gets one, loop breaks

    print('Thanks for playing')

play()
