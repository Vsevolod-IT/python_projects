
part = {''}

# create screen
a = [[' '] * 15 for i in range(10)]

# create vertical
for line,colone in enumerate(a):
    if (0 < line < 9):
        for colone,i in enumerate(colone):
            if colone == 3:
                 a[line][colone] = 'N'

# create gorizontal
for line,colone in enumerate(a):
    if line == 1:
        for colone,i in enumerate(colone):
            if (3 < colone < 8):
                 a[line][colone] = '='

# create bond
for line,colone in enumerate(a):
    if (1 < line < 4):
        for colone,i in enumerate(colone):
            if colone == 7:
                 a[line][colone] = ' |'

# block create man
for line,colone in enumerate(a):
    if line == 4:
        for colone,i in enumerate(colone):
            if colone == 7:
                 a[line][colone] = ' @'


for line,colone in enumerate(a):
    if line == 5:
        for colone,i in enumerate(colone):
            if colone == 7:
                 a[line][colone] = '/|\\'

for line,colone in enumerate(a):
    if line == 6:
        for colone,i in enumerate(colone):
            if colone == 7:
                 a[line][colone] = ' /\\'
# view screen
for i in a:
    print(*i)





