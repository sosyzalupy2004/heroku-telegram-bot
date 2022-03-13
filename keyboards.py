from telebot import types
from settings import vapes

main = types.ReplyKeyboardMarkup(row_width=2)
main.add(
    '🎋 Puff XXL (1600)',
    '🎋 Posh XL (1500)',
    '🎋 Alpha Onee Plus (2200)',
    '🎋 Maskking PRO (1000)',
    '🎋 HQD Cuvie Plus (1200)',
    '🎋 Bang XXL (2000)',
    '🎋 Bang Switch DUO (2000)',
    '🎋 HQD Maxim (400)'
)
btn5 = types.InlineKeyboardButton('Отчистить корзину', callback_data='delete')
btn2 = types.InlineKeyboardButton('Назад 🔙', callback_data='back')
btn3 = types.InlineKeyboardButton('Оформить Заказ 💳', callback_data='cheque')
btn4 = types.InlineKeyboardButton('Обновить адрес и контакты', callback_data='adr')

board2 = types.InlineKeyboardMarkup(row_width=2)
board2.add(btn5,btn2)

input_adress = types.InlineKeyboardMarkup(row_width=1)
adr = types.InlineKeyboardButton('Ввести адрес', callback_data='adr')
input_adress.add(adr)

input_money = types.InlineKeyboardMarkup(row_width=1)
btn = types.InlineKeyboardButton('Переходим к оплате 💳', callback_data='pay')
input_money.add(btn, btn2, btn4, btn5)

puff = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['puff_xxl_1600']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:puff_xxl_1600')
    puff.add(btn1)
puff.add(btn2,btn3)

posh = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['posh_xl_1500']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:posh_xl_1500')
    posh.add(btn1)
posh.add(btn2,btn3)

alpha = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['alpha_onee_plus_2200']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:alpha_onee_plus_2200')
    alpha.add(btn1)
alpha.add(btn2,btn3)

mask = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['maskking_1000']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:maskking_1000')
    mask.add(btn1)
mask.add(btn2,btn3)

hqd_cuvie_plus = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['hqd_cuvie_plus_1200']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:hqd_cuvie_plus_1200')
    hqd_cuvie_plus.add(btn1)
hqd_cuvie_plus.add(btn2, btn3)

    ##### = types.InlineKeyboardMarkup(row_width=1)
#   for btn in vapes[######]:
#      btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}_######')
#      #######.add()



bang_xxl = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['bang_xxl_2000'][0]:
    i = 1
    btn1 = types.InlineKeyboardButton(f"💨 {vapes['bang_xxl_2000'][0][btn]}", callback_data=f'{i}:bang_xxl_2000')
    i += 1
    bang_xxl.add(btn1)
bang_xxl.add(btn2,btn3)

bang_switch = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['bang_switch_duo_2000'][0]:
    i = 1
    btn1 = types.InlineKeyboardButton(f"💨 {vapes['bang_switch_duo_2000'][0][btn]}", callback_data=f'{i}:bang_switch_duo_2000')
    i += 1
    bang_switch.add(btn1)
bang_switch.add(btn2,btn3)

hqd_maxim = types.InlineKeyboardMarkup(row_width=2)
for btn in vapes['hqd_maxim_400']:
    btn1 = types.InlineKeyboardButton(f'💨 {btn}', callback_data=f'{btn}:hqd_maxim_400')
    hqd_maxim.add(btn1)
hqd_maxim.add(btn2,btn3)


