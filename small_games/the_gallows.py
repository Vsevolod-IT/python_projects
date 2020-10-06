


# create screen
def create_screen(symbol):
    return [[symbol] * 15 for i in range(10)]
a = create_screen(' ')

# create vertical
def create_post(a):
    for line,colone in enumerate(a):
        if (0 < line < 9):
            for colone,i in enumerate(colone):
                if colone == 3:
                     a[line][colone] = 'N'
    return a
create_post(a)

# create gorizontal
def create_beam(a):
    for line,colone in enumerate(a):
        if line == 1:
            for colone,i in enumerate(colone):
                if (3 < colone < 8):
                     a[line][colone] = '='
    return a

create_beam(a)
# create rope
def create_rope(a):
    for line,colone in enumerate(a):
        if (1 < line < 4):
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' |'
    return a
create_rope(a)

# block create man
def create_head(a):
    for line,colone in enumerate(a):
        if line == 4:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' @'
    return a
create_head(a)

def create_body(a):
    for line,colone in enumerate(a):
        if line == 5:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = '/()\\'
    return a
create_body(a)

def create_legs(a):
    for line,colone in enumerate(a):
        if line == 6:
            for colone,i in enumerate(colone):
                if colone == 7:
                     a[line][colone] = ' /\\'
    return a
create_legs(a)
# display game's screen
def display_screen(a):
    for i in a:
        print(*i)
    return a
display_screen(a)





