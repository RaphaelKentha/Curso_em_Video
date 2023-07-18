#faca um programa que leia um numero inteiro e mostre sua tabuada
num_int = int(input('Digite um numero inteiro: '))
print('###########################################')
print('########## TABUADA DO {} ##################'.format(num_int))
print('###########################################')
for i in range(0, 10):
    print('\t{} x {} = {}'.format(num_int, i+1, (num_int * (i+1))))
print('###########################################')
#utlizando o for, para fazer a tabuada, de forma mais simples e rapida

#metodo sem laco de repeticao
'''tabu_val = int(input('Digite sua tabuada: '))
tab1 = (1 * tabu_val)
tab2 = (2 * tabu_val)
tab3 = (3 * tabu_val)
tab4 = (4 * tabu_val)
tab5 = (5 * tabu_val)
tab6 = (6 * tabu_val)
tab7 = (7 * tabu_val)
tab8 = (8 * tabu_val)
tab9 = (9 * tabu_val)
tab10 = (10 * tabu_val)
#exite laço de repetçao!!!!
print('1 X {} = {} \n2 X {} = {} \n3 X {} = {} \n4 X {} = {} \n5 X {} = {} \n6 X {} = {} \n7 X {} = {} \n8 X {} = {} \n9 X {} = {} \n10 X {} = {}'.format(tabu_val, tab1, tabu_val, tab2, tabu_val, tab3, tabu_val, tab4, tabu_val, tab5, tabu_val, tab6, tabu_val, tab7, tabu_val, tab8, tabu_val, tab9, tabu_val, tab10))
'''