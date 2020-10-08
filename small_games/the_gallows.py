
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

def create_field(symbol):
    ''' return multidimensional list filled in with the entered character'''
    return [[symbol] * 15 for i in range(10)]

pl = create_field(' ')
create_vertical(pl,1,0,9,'X')
create_horizontal(pl,1,1,6,'=')
create_vertical(pl,5,1,4,'|')
create_vertical(pl,5,3,5,'O')
create_vertical(pl,5,4,6,'()')
create_vertical(pl,5,5,7,'/\\')

create_horizontal(pl, 9, 2, 8, '[ ]')
display_screen(pl)


