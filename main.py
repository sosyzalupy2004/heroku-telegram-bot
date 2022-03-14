import sqlite3
import os
import telebot
from telebot import types
import settings
import keyboards as kb
import func

bot = telebot.TeleBot(settings.api_tg)

try:
    @bot.message_handler(commands=['stats'])
    def stats_func(message):
        if message.from_user.id == settings.my_id:
            conn = sqlite3.connect('db.db')
            q = conn.cursor()
            q = q.execute('SELECT COUNT(*) FROM adresses').fetchone()
            bot.send_message(settings.my_id,f'Всего в боте {q[0]} пользователей')
            #bot.send_message(settings.my_id,f'Всего {users} юзеров.')


    @bot.message_handler(commands=['stop'])
    def stats_func(message):
        if message.from_user.id == settings.my_id:
            bot.send_message(settings.my_id, 'Бот выключен.')
            os._exit(0)
            # bot.send_message(settings.my_id,f'Всего {users} юзеров.')


    @bot.message_handler(commands=['start'])
    def start_func(message):
        id = message.from_user.id
        if func.get_adr(id) == None:
            print(f'new /start user:{id}')
            bot.send_message(settings.my_id,f'new /start user:{id}')
            bot.send_message(id,'Привет! Так как ты у нас новенький, для работы нужно установить адрес ⬇️ (кнопочка внизу)! Потом нажми /start, чтобы начать закупаться)', reply_markup=kb.input_adress)
        else:
            id = message.from_user.id
            nick = message.from_user.first_name
            bot.send_message(id,f'Привет, {nick}!\nВремя раскумариться, выбирай внизу девайсы под продажу в своем городе и заказывай)\n➖➖➖➖➖➖➖➖➖➖➖\n ☑️ <strong>Актуальный каталог</strong> ☑️\n➖➖➖➖➖➖➖➖➖➖➖\nPuff XXL -{settings.puff_xxl_1600_cost}р\nPosh XL -{settings.posh_xl_1500_cost}р\nAlpha Onee Plus -{settings.alpha_onee_plus_2200_cost}р\nBang Switch Duo -{settings.bang_switch_duo_2000_cost}р\nHQD Cuvie Plus -{settings.hqd_cuvie_plus_1200_cost}р\nBANG XXL -{settings.bang_xxl_2000_cost}р\nHQD Maxim -{settings.hqd_maxim_400_cost}р\nMaskking Pro -{settings.maskking_1000_cost}р',reply_markup=kb.main, parse_mode='HTML')
            if func.info_user(id) == 'new':
                func.first_join(id)

    @bot.message_handler(content_types=['text'])
    def start_text(message):
        id = message.from_user.id
        if func.get_adr(id) == None:
            bot.send_message(id, 'Для работы нужно установить адрес!', reply_markup=kb.adr)
        else:
            id = message.from_user.id
            if message.text == '🎋 Puff XXL (1600)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.puff)
            elif message.text == '🎋 Posh XL (1500)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.posh)
            elif message.text == '🎋 Alpha Onee Plus (2200)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.alpha)
            elif message.text == '🎋 Maskking PRO (1000)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.mask)
            elif message.text == '🎋 HQD Cuvie Plus (1200)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.hqd_cuvie_plus)
            elif message.text == '🎋 Bang XXL (2000)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.bang_xxl)
            elif message.text == '🎋 Bang Switch DUO (2000)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.bang_switch)
            elif message.text == '🎋 HQD Maxim (400)':
                bot.send_message(id, 'Выбери вкус:', reply_markup=kb.hqd_maxim)
            else:
                bot.send_message(id, 'Я не понимаю, юзай кнопки!')

    @bot.callback_query_handler(func=lambda call:True)
    def start_call(call):
        id = call.from_user.id
        data = call.data
        if call.data == 'cheque':
            if func.total_cheque(id)[1] >= 8:
                if int(func.total_cheque(id)[0]) < 5000:
                    bot.send_message(id,f'Сумма заказа: {func.total_cheque(id)[0]}\n'+func.include(id)+'\nПРОВЕРЬ АДРЕС И КОНТАКТ:\n'+func.get_adr(id), reply_markup=kb.input_money, parse_mode='HTML')
                else:
                    bot.send_message(id,f'Сумма заказа: {func.total_cheque(id)[0]}\n'+func.include(id)+'\nПРОВЕРЬ АДРЕС И КОНТАКТ:\n'+func.get_adr(id), reply_markup=kb.input_money, parse_mode='HTML')
            else:
                bot.send_message(id,f'Сумма заказа: {func.total_cheque(id)[0]}\n'+func.include(id)+'\nПРОВЕРЬ АДРЕС И КОНТАКТ:\n'+func.get_adr(id), reply_markup=kb.input_money, parse_mode='HTML')


        elif call.data == 'pay':
            func.create_order(call.from_user.id)
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton('Ссылка на оплату', url=func.return_qiwi_link(call.from_user.id))
            button2 = types.InlineKeyboardButton('Проверить оплату', callback_data='check_payment')
            keyboard.add(button,button2)
            bot.send_message(id,'<strong>КОММЕНТАРИЙ НЕ ИЗМЕНЯТЬ!!!</strong>\nВ форме все указано, что нужно, можете не переживать)',reply_markup=keyboard, parse_mode='HTML')


        elif call.data == 'check_payment':
            id = call.from_user.id
            if func.check_payment(id) != None:
               sum = int(func.total_cheque(id)[1])
               if int(func.total_cheque(id)[1])<5000:
                    bot.send_message(id,'Оплата принята! По вопросам логистики: @viphqd')
                   func.pay_seller(sum)
                   bot.send_message(settings.my_id, f'Новый заказ oт {call.from_user.id}:\n' + func.include(call.from_user.id) + f'/n Адрес: {func.get_adr(call.from_user.id)}')
                   bot.send_message(settings.seller_id, f'Новый заказ oт {call.from_user.id}:\n' + func.include(call.from_user.id) + f'/n Адрес: {func.get_adr(call.from_user.id)}')
                   func.reset_cart(id)
                   func.delete_code(id)

               else:
                   bot.send_message(id,'Оплата принята! По вопросам логистики: @darknethero')
                   func.pay_seller(sum)
                   bot.send_message(settings.my_id, f'Новый заказ oт {call.from_user.id}:\n' + func.include(call.from_user.id) + f'/n Адрес: {func.get_adr(call.from_user.id)}')
                   bot.send_message(settings.seller_id, f'Новый заказ oт {call.from_user.id}:\n' + func.include(call.from_user.id) + f'/n Адрес: {func.get_adr(call.from_user.id)}')
                   func.reset_cart(id)
                   func.delete_code(id)
            else:
                bot.send_message(id,'Oплата не найдена!')


        elif call.data == 'adr':
            msg = bot.send_message(id,'Введи свой адрес, Телефон и Имя + Фамилию (необхожимо для заказа)')
            bot.register_next_step_handler(msg, func.insert_adr)

        elif call.data == 'back':
            bot.send_message(call.from_user.id,'Главное Меню',reply_markup=kb.main)

        elif call.data == 'delete':
            func.reset_cart(id)
            bot.send_message(id,'Корзина отчищена!')

        else:
            data = call.data
            id = call.from_user.id
            func.separator(data,id)
            bot.answer_callback_query(callback_query_id=call.id,text='Товар добавлен в корзину!', show_alert=True,)
    bot.polling(none_stop=True)
except Exception as e:
    print(e)
    print('reconnect to Telegram....')
    bot.polling(none_stop=True)