# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Игра против бота с интеллектом:
from random import randint

def Users_steps():
    global count
    step = int(input('Сколько конфет Вы забираете? '))
    count -= step
    if count <= 0:
        print("Вы выиграли!")
    else:
        print('Осталось {} конфет'.format(count))
        

def Bots_steps():
    global count, max_step
    if count % (max_step + 1) !=0:
        step = count % (max_step + 1)
    else:
        step = randint(1, 28)
    print('Бот забрал {} конфет'.format(step))
    count -= step
    if count <= 0:
        print('Вы проиграли!')
    else:
        print('Осталось {} конфет'.format(count))

count = 2021
max_step = 28

input('Чтобы бросить жребий, нажмите Enter: ')
lot = randint(0,1)

if lot:
    print('Первым ходите Вы.')
else:
    print('Первым ходит бот.')

while count > 0:
    if lot:
        Users_steps()
        if count > 0:
            Bots_steps()
    else:
        Bots_steps()
        if count > 0:
            Users_steps()

# Игра человек против человека

# def Users_steps(user):
#     global count
#     print('Ходит {}: '.format(user))
#     step = int(input('Сколько конфет Вы забираете? '))
#     count -= step
#     if count <= 0:
#         print("Выиграл {}!".format(user))
#     else:
#         print('Осталось {} конфет'.format(count))

# count = 100
# max_step = 28
# user1 = 'первый игрок'
# user2 = 'второй игрок'

# while count > 0:
#     Users_steps(user1)
#     if count > 0:
#         Users_steps(user2)