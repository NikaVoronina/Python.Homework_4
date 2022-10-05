# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('task_5.txt', 'w') as file:
    file.write('2 * x ^ 2 + 5 * x ^ 5')
with open('task_5_1.txt', 'w') as file:
    file.write('23 * x ^ 4 + 9 * x ^ 6')

with open('task_5.txt','r') as file:
    task_1 = file.readline()
    list_of_task_1 = task_1.split()


with open('task_5_1.txt','r') as file:
    task_2 = file.readline()
    list_of_task_2 = task_2.split()

print(f'{list_of_task_1} + {list_of_task_2}')
sum_task = list_of_task_1 + list_of_task_2

with open('sum_task_5.txt', 'w') as file:
    file.write(f'{list_of_task_1} + {list_of_task_2}')