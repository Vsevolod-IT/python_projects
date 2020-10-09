from random import choice

def create_field(symbol):
    ''' return multidimensional list filled in with the entered character'''
    return [[symbol] * 15 for i in range(10)]

def create_vertical(field,num_column, start, stop, symbol):
    for line, colone in enumerate(field):
        if (start < line < stop):
            for colone, i in enumerate(colone):
                if colone == num_column:
                    field[line][colone] = symbol
    return field



def create_horizontal(field, num_line, start, stop, symbol):
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
    else:
        create_vertical(pl,5,4,6,'()')
    count[-1] += 1

def check_letter(word):
    letter = input('enter letter ->').lower()
    if letter in word:
        ind = word.index(letter)
        pl[9][ind] = letter
    elif letter not in word:
        print('no this letter')
        entered_letter.append(letter)
        draw_gallow()
    elif letter in entered_letter:
        print('already entered letter')
    else:
        print('enter only latin letter')
    return letter


words = 'absher absorb abston absurd acacia acarid accede accent accept access accord accost accrue ' \
        'ashman ashore ashton Askins batoon Batres Batson batten Batten batter battle Batton Baucom ' \
        'Bauder cuckoo cuddle cudgel Cuevas Cullen Culler Culley Cullum Culver Cumbie cunted cupful'.split(' ')

play_again = 'yes'

while play_again == 'yes':

    entered_letter = []
    word = (choice(words))
    word = word.lower()
    print(word)
    pl = create_field(' ')
    create_horizontal(pl, 9, -1, 6, '[ ]')
    display_screen(pl)
    for _ in enumerate(word):
        check_letter(word)
    play_again = input('play again -->')



