#user has to guess the number witch system is created

from random import randint as rand

user = input('please enter your name--> ')
comp_number = rand(1, 100)

again = input('Do you wanna start the game? \n yes or no --> ')
print(comp_number)


#game block
greeting_user = print('\t Hello, %s! You have to choise the number witch i made, \n \t from 1 to 100'
                      ' you\'ll have 5  attemps ' % user)

while again == 'yes':
    for attemps in range(5):
        answer_user = int(input('--number-->'))
        if answer_user == comp_number:
            again = input('congratulations you\'ve won \n play again(yes or no) --> ')
            continue
        elif answer_user < comp_number:
            print('less than it is')
        elif answer_user > comp_number:
            print('more than it is')
        else:
            again = input('game again? --> ')
            continue
    again = input ('play again? yes - no -->')


print('Thank\'s and bye')
