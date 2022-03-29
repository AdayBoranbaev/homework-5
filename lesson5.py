#-----1-----------------

with open('ex#1.txt', 'w', encoding='utf-8') as my_file:

line = " "
while line:
    line = input("Enter text: ")
    my_file.write(f"{line}\n")

#------ 2-------------------------

with open("ex#2.txt", 'r', encoding='utf-8') as f:
   file_r = [f'{line}. {count.strip()}'
             for line, count in enumerate(f, 1)]
   print(*file_r, f"Количество строк - {len(file_r)}")

#------ 3--------------------------

with open('ex#3.txt', 'r', encoding='utf-8') as f:
    dict_name = {line.split(): float(line.split()) for line in f}
    print(f' Средняя зарплата = {round(sum(dict.name.values()) / len(dict.name), 1)}')

#------- 4---------------------------

dir = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("ex#4.txt" , "w", encoding='utf-8') as f:
    with open("ex#4a.txt", encoding='utf-8') as f1:
        f.write([line.replace(line.split()[0], dir.get(line.split()[0])) for line in f1])

#--------5---------------------------

from random import randint

with open("ex#5.txt", "w", encoding='utf-8') as my_file:
    list = [randint(1, 100) for f in range(100)]
    my_file.write(" ".join(map(str, list)))

print(f"Сумма чисел равна- {sum(list)}")

#------6-----------------------------

with open('ex#6.txt', 'r', encoding='utf-8') as my_file:
    f = my_file.readlines()
    for a in f:
        new_obj = " ".join((i if i in '1234567890' else ' ') for i in a)
        new_obj2 = [int(i) for i in new_obj.split()]
    print(f'{a.split()[0]} {sum(new_obj2)}')

#--------7-----------------------------

---
