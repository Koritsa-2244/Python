import timeit
def time_track (code_to_test):
    elapsed_time = timeit.timeit(code_to_test, number=100)*1000
    formated_time = "{:.3f} ms".format(elapsed_time)
    print(formated_time)


my_list1 = [6,5,4,3,2,1]
print('list ',my_list1)
my_dict1 = {6:6,5:5,4:4,3:3,2:2,1:1}
print('dict ',my_dict1.values())

# добавление элемента
my_list1.append(4)
print('\r\nдобавление элемента\r\nlist ', my_list1)
my_dict1[7] = 7
print(my_dict1.values())

# удаление элемента
my_list1.pop()
print('\r\nудаление элемента\r\nlist ',my_list1)
my_dict1.pop(7)
print(my_dict1.values())

# поиск элемента
print('\r\nпоиск элемента\r\nlist[4] = ', my_list1[4])
print('dict[5] = ', my_dict1[5])

# замена элемента
my_list1[0] = 5
my_list1.pop(1)
print('\r\nзамена элемента\r\nlist ', my_list1)
my_dict1[1]=5
print(my_dict1.values())
my_dict1[1]=1

# объединение
my_list2 = [4,5,6,7,8,9]
my_list3 = my_list1 + my_list2
print('\r\nОбъединение\r\nlist 2 ', my_list2, '\r\nlist ', my_list3)
my_dict2 = {4: 4, 5: 5, 6 : 6, 7: 7,8: 8, 9: 9}
my_dict3 = {**my_dict1,**my_dict2}
print('dict 2 ', my_dict2.values(), '\r\n', my_dict3.values())

# пересечение
my_list3 = set(my_list1).intersection(my_list2)
print('\r\nпересечение\r\nlist', my_list3)
my_dict3 = dict(set(my_dict1.items()).intersection(set(my_dict2.items())))
print(my_dict3.values())

# разница
my_list3 = list(set(my_list1)-set(my_list2))
print('\r\nразница\r\nlist', my_list3)
my_dict3 = dict(set(my_dict1.items())-(set(my_dict2.items())))
print(my_dict3.values())

# сортировка
my_list3 = sorted(my_list1)
print('\r\nsort\r\nlist ',my_list3)
my_dict3 = dict(sorted(my_dict1.items())) #sorted(my_dict1.items(), key=lambda item: item[1])
print(my_dict3.values())

# сравнение 
print('\r\nCравнение')
print('list',my_list3==my_list2) # тк сортировка прошла мимо списка1, то если с ним сравнивать выйдет 0
print('dict', my_dict3==my_dict2) # тк сортировка сохранилась и в 1 и в 3 словаре, сравнение выдаст 1

# очистка
my_list1.clear()
my_list2.clear()
my_list3.clear()
my_dict1.clear()
my_dict2.clear()
my_dict3.clear()

# Измерение времени еденицы измерения + округление секунда - до 6 знаков
code_to_test_list = """
my_list1 = [1,2,3,4,5,6]
"""
code_to_test_dict = """
my_dict1 = {1: 1, 2: 2, 3: 3, 4:4, 5:5, 6:6}
"""
print('добавление элемента list, dict')
time_track(code_to_test_list + "my_list1.append(4)")
time_track(code_to_test_dict + "my_dict1[7] = 4")

print('\r\nудаление элемента')
time_track(code_to_test_list + "my_list1.pop(5)")
time_track(code_to_test_dict + "my_dict1.pop(6)")

print('\r\nпоиск элемента')
time_track(code_to_test_list + "x = my_list1[4]")
time_track(code_to_test_dict + "x = my_dict1[5]")

print('\r\nзамена элементa')
time_track(code_to_test_list + 'my_list1[0] = 5')
time_track(code_to_test_dict + 'my_dict1[1]=5')

code_to_test_list1 = code_to_test_list + 'my_list2 = [4,5,6,7,8,9]\r\n'
code_to_test_dict1 = code_to_test_dict + 'my_dict2 = {4: 4, 5: 5, 6 : 6, 7: 7,8: 8, 9: 9}\r\n'
print('\r\nобъединение')
time_track(code_to_test_list1 + 'my_list3 = my_list1 + my_list2')
time_track(code_to_test_dict1 + 'my_dict3 = {**my_dict1,**my_dict2}')

print('\r\nпересечение')
time_track(code_to_test_list1 + 'my_list3 = set(my_list1).intersection(my_list2)')
time_track(code_to_test_dict1 + 'my_dict3 = dict(set(my_dict1.items()).intersection(set(my_dict2.items())))')

print('\r\nразница')
time_track(code_to_test_list1 + 'my_list3 = list(set(my_list1)-set(my_list2))')
time_track(code_to_test_dict1 + 'my_dict3 = dict(set(my_dict1.items())-(set(my_dict2.items())))')

print('\r\nсортировка')
code_to_test_list1 += 'my_list3 = sorted(my_list1)\r\n'
code_to_test_dict1 += 'my_dict3 = dict(sorted(my_dict1.items()))\r\n'
time_track(code_to_test_list1)
time_track(code_to_test_dict1)

print('\r\nсравнение')
time_track(code_to_test_list1 + 'my_list3==my_list2')
time_track(code_to_test_dict1 + 'my_dict3==my_dict2')

print('\r\nочистка')
time_track(code_to_test_list + 'my_list1.clear()')
time_track(code_to_test_dict + 'my_dict1.clear()')
