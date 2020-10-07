

def create_field(symbol):
    ''' return multidimensional list filled in with the entered character'''
    return [[symbol] * 15 for i in range(10)]


def create_vertical(field: list, num_column: int, quantity: int, symbol):

    '''the function changes
    --> playing field (list)
    --> globals variables - count_column, count_string (these are counters
        for the next call func)
    the function accepts 4 parametrs, the function draws vertically any symbols
    param: field - it's playing field type list,
    num_column - number of the column where the symbol will be drawn ,
    quantity - how many reps will be, symbol - symbols (str or int) that will be drawn'''

    x,y = quantity-quantity,quantity+1
    global count_string
    count_string = x
    global count_column
    count_column = num_column
    for line, colone in enumerate(field):
        if (x < line < y):
            for colone, i in enumerate(colone):
                if colone == num_column:
                    field[line][colone] = symbol
    return field, count_column, count_string

def create_horizontal(field: list, num_line: int, num_column, quantity: int, symbol):

    '''the function changes
    --> playing field (list)
    --> globals variables - count_column, count_string (these are counters
        for the next call func)
    the function accepts 4 parametrs, the function draws horizontally any symbols
    param: field - it's playing field type list,
    num_line - number of the line where the symbol will be drawn,
    num_column - number of the column where the symbol will be drawn ,
    quantity - how many reps will be, symbol - symbols (str or int) that will be drawn'''

    global count_column
    global count_string
    count_string = num_line
    y = (num_column + 1) + quantity
    for line,colone in enumerate(field):
        if line == num_line:
            for colone,i in enumerate(colone):
                if (num_column < colone < y):
                     field[line][colone] = symbol
    count_column = y
    return field, count_column, count_string




def display_screen(field):
    ''' output the  multidimensional list'''
    for i in field:
        print(*i)
    return field


word_list = ('Accept	Guess Achieve	Harass Add	Hate Admire	Hear Admit	Help Adopt	Hit Advise	Hope'
             'Agree	Identify Allow	Interrupt Announce	Introduce Appreciate	Irritate Approve	Jump Argue	Keep'
             'Arrive	Kick Ask	Kiss Assist	Laugh Attack	Learn Bake	Leave Bathe	Lend'.split())


    

