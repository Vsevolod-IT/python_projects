
def calculate():
    while True:
        a, action, b = map(str, input('введите пример --> ').split(' '))
        a, b = map(int, (a, b))
        if action == '0':
            print('*' * 10)
            break
        elif action == '-':
            print(f'{a - b}')
        elif action == '*':
            print(f'{a*b}')
        elif action == '/':
            print(f'{a // b}')
        elif action == '+':
            print(f'{a + b}')
        else:
            print('неверный знак (используйте: 0, +, *, -, /)')

calculate()