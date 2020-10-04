'''a =[' |@-----@\n'
     '|      |\n
     '|      0\n
     '|     /|\\n
      |     / \\n
     /|\' ]'''
import itertools

a = [[i for i in itertools.repeat('.', 30)]for i in range(15)]
for i in a:
     print(*i)

hangman_design = {'base':'/|\ ',
                  'post': '|',
                  'beam': '=++=+=+=+=+=+@'}
print(hangman_design)



