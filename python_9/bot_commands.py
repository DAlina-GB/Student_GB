from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import datetime
from spy_log import *
import random
import strings as st


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')  # ~print


def w_d_command(update: Update, context: CallbackContext):
    log(update, context)
    input_text = update.message.text[4:] if len(update.message.text) > 4 else ""
    input_text = words_delete(input_text)
    if input_text:
        update.message.reply_text(input_text)


def ran_command(update: Update, context: CallbackContext):
    log(update, context)
    input_text = update.message.text[4:] if len(update.message.text) > 4 else ""
    randomlist = input_text.split() if input_text else []
    if not input_text:
        randomlist = random.sample(range(10), 5)
    update.message.reply_text(randomlist)
    random.shuffle(randomlist)
    update.message.reply_text(randomlist)


# # 38. Напишите программу, удаляющую из 
# # текста все слова содержащие "абв".

def words_delete(input_text):
    if not input_text:
        return ""
    input_text = list(filter(lambda x: 'абв' not in x, input_text.split()))
    return " ".join(input_text)


# TicTacToe

def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False

def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == st.SYMBOL_UNDEF:
            counter += 1
    return counter

def game(callBackData):
    # -------------------------------------------------- global message  # использование глобальной переменной message
    message = st.ANSW_YOUR_TURN  # сообщение, которое вернется
    alert = None

    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9:  
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == st.SYMBOL_UNDEF:  # проверка: если в нажатой кнопке не выбран крестик/нолик, то можно туда сходить крестику
            charList[buttonNumber] = st.SYMBOL_X  
            if isWin(charList, st.SYMBOL_X):
                 message = st.ANSW_YOU_WIN 
            else:  
                if countUndefinedCells(charList) != 0:  
                    
                    isCycleContinue = True
                    
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand] == st.SYMBOL_UNDEF:  
                            charList[rand] = st.SYMBOL_O
                            isCycleContinue = False  
                            if isWin(charList, st.SYMBOL_O):  
                                message = st.ANSW_BOT_WIN

        
            alert = st.ALERT_CANNOT_MOVE_TO_THIS_CELL

       
        if countUndefinedCells(charList) == 0 and message == st.ANSW_YOUR_TURN:
            message = st.ANSW_DRAW

        
        callBackData = ''
        for c in charList:
            callBackData += c

    
    if message == st.ANSW_YOU_WIN or message == st.ANSW_BOT_WIN or message == st.ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  

    return message, callBackData, alert



def getKeyboard(callBackData):
    keyboard = [[], [], []] 

    if callBackData != None:  
      
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    return keyboard


def newGame(update, _):
    
    data = ''
    for i in range(0, 9):
        data += st.SYMBOL_UNDEF


    update.message.reply_text(st.ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))


def button(update, _):
    query = update.callback_query
    callbackData = query.data  
    message, callbackData, alert = game(callbackData)  
    if alert is None:  
        query.answer()   
        query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else:  
        query.answer(text=alert, show_alert=True)


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Калькулятор производит следующие действия над числами, в том числе с комплексными:'
                              f'\nсложение "+", вычитание "-", умножение "*", деление"/", возведение в степень"**", остаток от деления "%"'
                              f'\nпосле команды /calc между числами и действием необходимо ставить пробел, пример /calc 5 ** 2 или /calc 2-3j + 23+7j')

def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = items[1]
    action = items[2]
    y = items[3]
    exept = x + action + y
    result=eval(exept)
    print(f'{exept} = {result}')
    update.message.reply_text(f'{x} {action} {y} = {result}')

