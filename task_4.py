# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from calendar import c
import os
os.system('cls')
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

random_list = list([randint(0, 101) for i in range(k + 1)])
if random_list[0] == 0:
    random_list[0] = randint(1, 101)

def get_task(k, random_list):
    str1 = [' * x ** ']*(k - 1) + [' * x']
    task = [[a, b, c] for a, b, c  in itertools.zip_longest(random_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in task:
        x.append(' + ')
    task = list(itertools.chain(* task))
    task[-1] = ' = 0'
    return "".join(map(str, task)).replace(' 1 * x',' x')

list = get_task(k, random_list)
print(f'{k} => {list}')

with open('Task_4.txt', 'w') as data:
    data.write(list)