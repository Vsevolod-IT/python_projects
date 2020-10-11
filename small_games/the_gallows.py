from random import choice

def create_field(symbol):
    '''
    return multidimensional list any count rows and columns filled in with the entered character or integer
    '''
    return [[symbol] * 15 for i in range(10)]

def create_vertical(field: list, num_column: int, start: int, stop: int, symbol):
    '''
    func inserts the characters vertically into multidimensional list.
    Param: field - multidimensional list, num_column - by x, start/stop - index (slice of list), symbol-str or int
    '''
    for line, colone in enumerate(field):
        if (start < line < stop):
            for colone, i in enumerate(colone):
                if colone == num_column:
                    field[line][colone] = symbol

    return field



def create_horizontal(field, num_line, start, stop, symbol):
    '''
    func inserts the characters horizpntal into multidimensional list.
    param : field - multidimensional list, num_line - by y, start/stop - index (slice of list), symbol-str or int
     '''
    for line, colone in enumerate(field):
        if line == num_line:
            for colone, i in enumerate(colone):
                if (start < colone < stop):
                    field[line][colone] = symbol
    return field


def display_screen(field):
    ''' output the  multidimensional list'''
    for i in field:
        print(*i)
    return field



def draw_gallow(count=[]):
    '''
    the function draws a gallows at pre-defined coordinates
    param: count as counter for calling
    '''
    global flag
    if not count:
        count.append(1)
    check = count[-1]
    if check == 1:
        create_vertical(pl, 1, 0, 9, 'X')
    elif check == 2:
        create_horizontal(pl,1,1,6,'=')
    elif check ==3:
        create_vertical(pl,5,1,4,'|')
    elif check ==4:
        create_vertical(pl,5,3,5,'O')
    elif check == 5:
        create_vertical(pl,5,4,6,'()')
    elif check == 6:
        create_vertical(pl, 5, 5, 7, '/\\')
    else:
        flag = False
        return flag
    count[-1] += 1


def check_letter(word):
    '''
    the function takes the selected system call requests a letter from the user and checks
    if there's a letter in word, if not it launches dsraw_gallon and adds the letter to the list letters you entered,
    if Yes then it prints the letter in the playing field
    param: word - word from list words
    '''
    letter = input('enter letter ->').lower()
    if letter in word:
        ind = word.index(letter)
        pl[9][ind] = letter
    elif letter in entered_letter:
        print('already entered letter')
        draw_gallow()
    elif letter not in word:
        print('no this letter')
        entered_letter.append(letter)
        draw_gallow()
    else:
        print('enter only latin letter')
    return letter

def check_win():
    '''
    checks the user's word if it is correct stops the game loop
    '''
    global flag
    word_user = pl[9][0:6]
    word_user = ''.join(word_user)
    if word == word_user:
        print('you won')
        flag = False
        return flag


# words for making
words = 'absher absorb abston absurd acacia acarid accede accent accept access accord accost accrue ' \
        'ashman ashore ashton Askins batoon Batres Batson batten Batten batter battle Batton Baucom ' \
        'Bauder cuckoo cuddle cudgel Cuevas Cullen Culler Culley Cullum Culver Cumbie cunted cupful'.split(' ')

# play_again and flag it's  bool for  2 circle while
play_again = 'yes'
flag = True

# game block
while play_again == 'yes':

    entered_letter = []
    word = (choice(words))
    word = word.lower()
    print(word)
    pl = create_field(' ')
    create_horizontal(pl, 9, -1, 6, '[ ]')
    display_screen(pl)
    while flag:
        check_letter(word)
        check_win()
        display_screen(pl)
    play_again = input('play again -->')



