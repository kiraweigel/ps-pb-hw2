account1 = {'login':'Ivan' , 'password': 'q1'}
account2 = {'login':'Petr' , 'password': 'q2'}
account3 = {'login':'Olga' , 'password': 'q3'}
account4 = {'login':'Anna' , 'password': 'q4'}

user1 = {'name':'Иван', 'age': 20, 'account':account1}
user2 = {'name':'Петр', 'age': 25, 'account':account2}
user3 = {'name':'Ольга', 'age': 18, 'account':account3}
user4 = {'name':'Анна', 'age': 27, 'account':account4}

user_list = [user1, user2, user3, user4]

#ПЕРВАЯ ЧАСТЬ ЗАДАЧИ
key = input('Введите ключ (name или account): ') 
lower_key = key.lower()

try:
    print(f'значение ключа {key} для юзера 1 = ' + user1[lower_key])
    print(f'значение ключа {key} для юзера 2 = ' + user2[lower_key])
    print(f'значение ключа {key} для юзера 3 = ' + user3[lower_key])
    print(f'значение ключа {key} для юзера 4 = ' + user4[lower_key])
except:
    print('Введенный ключ не найден')

#ВТОРАЯ ЧАСТЬ ЗАДАЧИ

user_number = input('Введите порядковый номер: ')
user_temp = user_list[int(user_number)-1]
user_cred = user_temp['account']

try:
    print(f'Данные по юзеру № {user_number}:')
    print('имя: ' , user_temp['name'])
    print('возраст: ' , user_temp['age'])
    print('логин: ' , user_cred['login'])
    print('пароль: ' , user_cred['password'])
except:
    print('Пользователь с указанным номером не найден')

#ТРЕТЬЯ ЧАСТЬ ЗАДАЧИ

user_remove = input('Введите номер пользователя, которого нужно переместить в конец: ')
user_remove_name = user_list[int(user_remove)-1]

print('Список до изменения: ' , user_list)

print('Пользователь с именем ', user_remove_name['name'] , 'перемещен в конец')

element = user_list.pop(int(user_remove)-1)
user_list.append(element)

print('Список после изменения: ' , user_list)

print(user_list)

#ЧЕТВЕРТАЯ ЧАСТЬ ЗАДАЧИ
average_age = (user1['age'] + user2['age'] + user3['age'] + user4['age']) / len(user_list)
print(f'Средний возраст всех пользователей = {average_age}')
