#user has to guess the number witch system is created

from random import randint as rand

user_name,attemps,min_figer,max_figer = map(str, input('\tThis is game \' guess number\''
                                              'please enter your name,\n\thow many attemps do you want,'
                                              'min figer, max figer \n\t(each one from /) --> ').split())

attemps,min_figer,max_figer = int(attemps), int(min_figer), int(max_figer)

comp_number = rand(min_figer, max_figer)
again = 'yes'
print(comp_number)

#game block
greeting_user = print('\t So, %s You have to choise the number witch i made, \n \t from %d to %d'
                      ' you\'ll have %d  attemps ' % (user_name,min_figer, max_figer, attemps ))

while again == 'yes':
    for i in range(attemps):
        try:
            answer_user = int(input('--number-->'))
            if answer_user == comp_number:
                print('\t  congratulations you\'ve won ')
                break
            elif answer_user < comp_number:
                print('less than it is')
            elif answer_user > comp_number:
                print('more than it is')
        except:
            break
    again = input ('play again? yes - no -->')


print('\nThank\'s and bye')
