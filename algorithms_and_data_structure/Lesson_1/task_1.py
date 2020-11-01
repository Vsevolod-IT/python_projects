'''Выполнить логические побитовые операции «И»,
   «ИЛИ» и др. над числами 5 и 6. Выполнить над числом
   5 побитовый сдвиг вправо и влево на два знака.'''

a = 5
b =6

conjunction = a & b
disjunction = a | b
xor = a ^ b
denial_a = ~a
denial_b = ~b
bitwise_shift_right = a << 2
bitwise_shift_left = a >> 2

print(f' conjunction: -->{conjunction}\n disjunction: --> {disjunction}\n'
      f' xor: --> {xor}\n denial_a: --> {denial_a}\n denial_b: --> {denial_b}\n'
      f' bitwise_shift_right: --> {bitwise_shift_right}\n bitwise_shift_left: --> {bitwise_shift_left}')