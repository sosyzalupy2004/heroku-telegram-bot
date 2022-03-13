import sqlite3

import pyqiwi

from settings import *
import ast
import requests
import json
from random import randint
import pyqiwi
                                    #-#-#-#-#-#-#-#-#-#BEGINNING#-#-#-#-#-#-#-#-#-#
def pay_seller(amount):
    wallet = pyqiwi.Wallet(token=api_qiwi,number=num_qiwi)
    wallet.qiwi_transfer(num_qiwi_seller,int(amount))

def create_order(id):
    id1 = id
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    try:
        q.execute(f'DELETE FROM check_payment WHERE id IS "{id1}"')
    except:
        pass
    q.execute('INSERT INTO check_payment VALUES (?,?,?)', (id1, total_cheque(id1)[0],randint(1,999999999)))
    conn.commit()


def check_payment(id):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    try:
        session = requests.Session()
        session.headers['authorization'] = 'Bearer ' + api_qiwi
        parameters = {'rows': '5'}
        h = session.get('https://edge.qiwi.com/payment-history/v1/persons/{}/payments'.format(num_qiwi),
                        params=parameters)
        req = json.loads(h.text)
        result = cursor.execute(f'SELECT * FROM check_payment WHERE id = {id}').fetchone()
        comment = result[2]
        sum = result[1]
        for i in range(len(req['data'])):
            if str(comment) in str(req['data'][i]['comment']) and str('643') in str(req['data'][i]["sum"]["currency"]) and str(sum) in str(req['data'][i]["sum"]["amount"]):
                return req["data"][i]["sum"]["amount"]
    except Exception as e:
        print(e)
    conn.close()


def first_join(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute("INSERT INTO users VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id, [], [], [], [], [], [], [], [], 0))
    conn.commit()
    conn.close()

def info_user(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute("SELECT puff_xxl_1600 FROM users WHERE id IS "+str(id))
    q = [*q]
    if q == []:
        return 'new'
    else:
        return 'ok'


                                    #-#-#-#-#-#-#-#-#-#LETSGOOOOOOO#-#-#-#-#-#-#-#-#-#


def separator(data,id):
    first_part = data.split(':')[0]
    second_part = data.split(':')[1]
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute(f"SELECT {second_part} FROM users WHERE id IS "+str(id))
    q_new = [*q][0][0]
    x = ast.literal_eval(q_new)
    x.append(first_part)
    if second_part == 'bang_switch_duo_2000':
        q.execute(f'UPDATE users SET bang_switch_duo_2000="{x}" WHERE id IS "{id}"')
    elif second_part == 'puff_xxl_1600':
        q.execute(f'UPDATE users SET puff_xxl_1600="{x}" WHERE id IS "{id}"')
    elif second_part == 'posh_xl_1500':
        q.execute(f'UPDATE users SET posh_xl_1500="{x}" WHERE id IS "{id}"')
    elif second_part == 'alpha_onee_plus_2200':
        q.execute(f'UPDATE users SET alpha_onee_plus_2200="{x}" WHERE id IS "{id}"')
    elif second_part == 'maskking_1000':
        q.execute(f'UPDATE users SET maskking_1000="{x}" WHERE id IS "{id}"')
    elif second_part == 'hqd_cuvie_plus_1200':
        q.execute(f'UPDATE users SET hqd_cuvie_plus_1200="{x}" WHERE id IS "{id}"')
    elif second_part == 'bang_xxl_2000':
        q.execute(f'UPDATE users SET bang_xxl_2000="{x}" WHERE id IS "{id}"')
    elif second_part == 'bang_switch_duo_2000':
        q.execute(f'UPDATE users SET bang_switch_duo_2000="{x}" WHERE id IS "{id}"')
    elif second_part == 'hqd_maxim_400':
        q.execute(f'UPDATE users SET hqd_maxim_400="{x}" WHERE id IS "{id}"')
    conn.commit()
    conn.close()

def reset_cart(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute(f'UPDATE users SET bang_switch_duo_2000="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET puff_xxl_1600="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET posh_xl_1500="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET alpha_onee_plus_2200="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET maskking_1000="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET hqd_cuvie_plus_1200="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET bang_xxl_2000="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET hqd_maxim_400="[]" WHERE id IS "{id}"')
    q.execute(f'UPDATE users SET total ="0" WHERE id IS "{id}"')
    conn.commit()
    conn.close()

def total_cheque(id):
    s = 0
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    sum_puff_xxl_1600 = 0
    try:
        q.execute("SELECT puff_xxl_1600 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        s = s + a
        sum_puff_xxl_1600 = a * puff_xxl_1600_cost
    except:
        pass
    sum_posh_xl_1500 = 0
    try:
        q.execute("SELECT posh_xl_1500 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        sum_posh_xl_1500 = a * posh_xl_1500_cost
        s = s + a
    except:
        pass
    sum_alpha_onee_plus_2200 = 0
    try:
        q.execute("SELECT alpha_onee_plus_2200 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        sum_alpha_onee_plus_2200 = a * alpha_onee_plus_2200_cost
        s = s + a
    except:
        pass
    sum_bang_switch_duo_2000 = 0
    try:
        q.execute("SELECT bang_switch_duo_2000 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        sum_bang_switch_duo_2000 = a * bang_switch_duo_2000_cost
        s = s + a
    except:
        pass
    sum_hqd_cuvie_plus_1200 = 0
    try:
        q.execute("SELECT hqd_cuvie_plus_1200 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        sum_hqd_cuvie_plus_1200 = a * hqd_cuvie_plus_1200_cost
        s = s + a
    except:
        pass
    sum_bang_xxl_2000 = 0
    try:
        q.execute("SELECT bang_xxl_2000 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        sum_bang_xxl_2000 = a * bang_xxl_2000_cost
        s = s + a
    except:
        pass
    sum_hqd_maxim_400 = 0
    try:
        q.execute("SELECT hqd_maxim_400 FROM users WHERE id IS " + str(id))
        q_new = [*q][0][0]
        x = ast.literal_eval(q_new)
        a = len(x)
        conn.close()
        sum_hqd_maxim_400 = a * hqd_maxim_400_cost
        s = s + a
    except:
        pass
    total = sum_puff_xxl_1600 + sum_posh_xl_1500 + sum_alpha_onee_plus_2200 + sum_bang_switch_duo_2000 + sum_hqd_cuvie_plus_1200 + sum_bang_xxl_2000 + sum_hqd_maxim_400
    return [total,s]

def all_in_list(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute('SELECT * FROM users WHERE id IS '+str(id))
    q = [*q]
    q = q[0][1:9]
    list = []
    for elem in q:
        list.append(elem)
    return list

def delete_code(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    q.execute('DELETE FROM check_payment WHERE id IS '+str(id))
    conn.commit()
    conn.close()

def include(id):
    list_with_all = all_in_list(id)
    all_puff_xxl_1600 = list_with_all[0]
    all_puff_xxl_1600 = ast.literal_eval(all_puff_xxl_1600)
    print(all_puff_xxl_1600)
    all_posh_xl_1500 = list_with_all[1]
    all_posh_xl_1500 = ast.literal_eval(all_posh_xl_1500)
    print(all_posh_xl_1500)
    all_alpha_onee_plus_2200 = list_with_all[2]
    all_alpha_onee_plus_2200 = ast.literal_eval(all_alpha_onee_plus_2200)
    print(all_alpha_onee_plus_2200)
    all_maskking_1000 = list_with_all[3]
    all_maskking_1000 = ast.literal_eval(all_maskking_1000)
    print(all_maskking_1000)
    all_hqd_cuvie_plus_1200 = list_with_all[4]
    all_hqd_cuvie_plus_1200 = ast.literal_eval(all_hqd_cuvie_plus_1200)
    print(all_hqd_cuvie_plus_1200)
    all_bang_xxl_2000 = list_with_all[5]
    all_bang_xxl_2000 = ast.literal_eval(all_bang_xxl_2000)
    print(all_bang_xxl_2000)
    all_bang_switch_duo_2000 = list_with_all[6]
    all_bang_switch_duo_2000 = ast.literal_eval(all_bang_switch_duo_2000)
    print(all_bang_switch_duo_2000)
    all_hqd_maxim_400 = list_with_all[7]
    all_hqd_maxim_400 = ast.literal_eval(all_hqd_maxim_400)
    print(all_hqd_maxim_400)
    text = 'В вашем заказе:\n'
    if len(all_puff_xxl_1600) != 0:
        lenght = len(all_puff_xxl_1600)
        text = text + ' --<code>Puff XXL(1600):</code>\n'
        num = 1
        for item in list(dict.fromkeys(all_puff_xxl_1600)):
            num = all_puff_xxl_1600.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_posh_xl_1500) != 0:
        lenght = len(all_puff_xxl_1600)
        text = text + ' --<code>Posh XL(1500):</code>\n'
        for item in list(dict.fromkeys(all_posh_xl_1500)):
            num = all_posh_xl_1500.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_alpha_onee_plus_2200) != 0:
        lenght = len(all_alpha_onee_plus_2200)
        text = text + ' --<code>Alpha Onee Plus(2200):</code>\n'
        for item in list(dict.fromkeys(all_alpha_onee_plus_2200)):
            num = all_alpha_onee_plus_2200.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_maskking_1000) != 0:
        lenght = len(all_maskking_1000)
        text = text + ' --<code>Maskking Pro (1000):</code>\n'
        for item in list(dict.fromkeys(all_maskking_1000)):
            num = all_maskking_1000.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_hqd_cuvie_plus_1200) != 0:
        lenght = len(all_hqd_cuvie_plus_1200)
        text = text + ' --<code>HQD Cuvie Plus(1200):</code>\n'
        for item in list(dict.fromkeys(all_hqd_cuvie_plus_1200)):
            num = all_hqd_cuvie_plus_1200.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_bang_xxl_2000) != 0:
        lenght = len(all_bang_xxl_2000)
        text = text + ' --<code>Bang XXL(2000):</code>\n'
        for item in list(dict.fromkeys(all_bang_xxl_2000)):
            num = all_bang_xxl_2000.count(item)
            item = int(item)
            text = text + f'{vapes["bang_xxl_2000"][0][item]} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_bang_switch_duo_2000) != 0:
        lenght = len(all_bang_switch_duo_2000)
        text = text + ' --<code>BANG Switch Duo (2000):</code>\n'
        for item in list(dict.fromkeys(all_bang_switch_duo_2000)):
            num = all_bang_switch_duo_2000.count(item)
            item = int(item)
            text = text + f'{vapes["bang_switch_duo_2000"][0][item]} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    if len(all_hqd_maxim_400) != 0:
        lenght = len(all_hqd_maxim_400)
        text = text + ' --<code>HQD Maxim (400):</code>\n'
        for item in list(dict.fromkeys(all_hqd_maxim_400)):
            num = all_hqd_maxim_400.count(item)
            text = text + f'{item} x{num}\n'
            lenght = lenght - num
            if lenght == 0:
                break
    return text

def get_adr(id):
    try:
        conn = sqlite3.connect('db.db')
        q = conn.cursor()
        result = q.execute('SELECT * FROM adresses WHERE id IS '+str(id)).fetchone()
        result = result[1]
        conn.close()
        return result
    except:
        return None

def insert_adr(message):
    id = message.from_user.id
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    try:
        q.execute('DELETE FROM adresses WHERE id IS '+str(id))
        conn.commit()
    except:
        pass
    q.execute('INSERT INTO adresses VALUES (?,?)',(id,message.text))
    conn.commit()
    conn.close()

def return_qiwi_link(id):
    conn = sqlite3.connect('db.db')
    q = conn.cursor()
    result = q.execute('SELECT * FROM check_payment WHERE id IS '+str(id)).fetchone()
    tuple = result
    amount = tuple[1]
    code = tuple[2]
    link = f'https://qiwi.com/payment/form/99?extra%5B%27account%27%5D={num_qiwi}&amountInteger={amount}&amountFraction=0&extra%5B%27comment%27%5D={code}&currency=643&blocked[0]=account'
    return link