'''Пользователь вводит две буквы. Определить, на каких местах алфавита
 они стоят, и сколько между ними находится букв.
'''

letter_1,letter_2 = map(str,input('Введите две буквы -->').split())
first_letter = 97

letter_1 = ord(letter_1)
letter_2 = ord(letter_2)

place_1 = letter_1 - first_letter + 1
place_2 = letter_2 - first_letter + 1
letters = letter_2 - letter_1 - 1

print(f'место в алфавите  1ой буквы: {place_1}\n'
      f'место в алфавите 2ой буквы: {place_2}\n'
      f'между ними {letters} букв')