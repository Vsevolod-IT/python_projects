


# create screen
def create_screen(symbol):
    return [[symbol] * 15 for i in range(10)]


# create vertical
def create_post(a):
    for line,colone in enumerate(a): # в каком столбе и  сколько
        if (0 < line < 9):
            for colone,i in enumerate(colone):
                if colone == 3:
                     a[line][colone] = 'N'
    return a


# create gorizontal
def create_beam(a):
    for line,colone in enumerate(a): # в какой строке и сколько
        if line == 1:
            for colone,i in enumerate(colone):
                if (3 < colone < 8):
                     a[line][colone] = '='
    return a


# create rope
def create_rope(a):
    for line,colone in enumerate(a):
        if (1 < line < 4):
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' |'
    return a


# block create man
def create_head(a):
    for line,colone in enumerate(a):
        if line == 4:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' @'
    return a


def create_body(a):
    for line,colone in enumerate(a):
        if line == 5:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = '/()\\'
    return a


def create_legs(a):
    for line,colone in enumerate(a):
        if line == 6:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' /\\'
    return a

# display game's screen
def display_screen(a):
    for i in a:
        print(*i)
    return a


word_list = ('Accept	Guess Achieve	Harass Add	Hate Admire	Hear Admit	Help Adopt	Hit Advise	Hope'
             'Agree	Identify Allow	Interrupt Announce	Introduce Appreciate	Irritate Approve	Jump Argue	Keep'
             'Arrive	Kick Ask	Kiss Assist	Laugh Attack	Learn Bake	Leave Bathe	Lend'.split())


a = create_screen('.')
create_post(a) # 8
create_beam(a) # 4
create_rope(a) # 2
create_head(a) # 1
create_body(a) # 1
create_legs(a) # 1

display_screen(a)


# change func

#create vertical

def create_vertical(field: list, num_column: int, quantity: int, symbol):
    global column
    column = num_column
    x,y = quantity-quantity,quantity+1
    for line, colone in enumerate(field):
        if (x < line < y):
            for colone, i in enumerate(colone):
                if colone == num_column:
                    field[line][colone] = symbol
    return field, column

# create gorizontal
def create_gorizontal(field: list, num_line: int, num_column, quantity: int, symbol):
    global column
    y = (num_column + 1) + quantity
    for line,colone in enumerate(field):
        if line == num_line:
            for colone,i in enumerate(colone):
                if (num_column < colone < y):
                     field[line][colone] = symbol
    column = y
    return field,column

