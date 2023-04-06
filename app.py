from flask import Flask, render_template, request, url_for, redirect
import re
import requests
import os

app = Flask(__name__)

def acc_api_call(item_id):
    url = 'https://trade.jp.playblackdesert.com/Trademarket/GetWorldMarketSubList'
    headers = {        
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainKey": item_id
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    res_letter = response.text
    res_list = re.split(r'[\-|:]', res_letter)
    del res_list[0:2]
    del res_list[-1]

    price_list = [int(res_list[10 * n + 3]) for n in range(6)]
    return price_list



def item_api_call(item_id):
    url = 'https://trade.jp.playblackdesert.com/Trademarket/GetWorldMarketSubList'
    headers = {        
        "Content-Type": "application/json",
        "User-Agent": "BlackDesert"
    }
    payload = {
        "keyType": 0,
        "mainKey": item_id
    }

    response = requests.request('POST', url, json=payload, headers=headers)
    res_letter = response.text
    res_list = re.split(r'[\-|:]', res_letter)
    del res_list[0:2]
    del res_list[-1]
    return int(res_list[3])

tax = 0.8547

# DB // SQLを導入したいですまる
bs_armour = item_api_call(16002)
bs_wepon = item_api_call(16001)
crescent = acc_api_call(12031)
tun_ring = acc_api_call(12061)
ruin_ring = acc_api_call(12060)
disto = acc_api_call(11853)
narc = acc_api_call(11834)
tun_belt = acc_api_call(12237)
tun_ear = acc_api_call(11828)
tun_neck = acc_api_call(11629)
turo_belt = acc_api_call(12257)
basi_belt = acc_api_call(12230)
centa_belt = acc_api_call(12229)
ominous_ring = acc_api_call(12068)
ogre_ring = acc_api_call(11607)
laytenn = acc_api_call(11630)
sicil = acc_api_call(11625)
dawn = acc_api_call(11855)
vaha = acc_api_call(11875)
cadry = acc_api_call(12032)
valt_belt = acc_api_call(12236)
ethereal = acc_api_call(11856)
lunar = acc_api_call(11663)
river = acc_api_call(11662)
orkin_belt = acc_api_call(12251)


def ja_name(item):
    accessories = {
        'crescent': '三日月リング',
        'tun_ring': 'ツンリング',
        'tun_belt': 'ツンベルト',
        'disto': '侵食',
        'narc': 'ナク',
        'ruin_ring': '廃墟リング',
        'tun_ear': 'ツン耳',
        'tun_neck': 'ツンネク',
        'turo_belt': 'トゥーロ',
        'basi_belt': 'バジベルト',
        'centa_belt': 'ケンタベルト',
        'ominous_ring': '背後リング',
        'ogre_ring': 'オーガリング',
        'laytenn': 'ライテン',
        'sicil': 'シチル',
        'dawn': '黎明',
        'vaha': 'バア',
        'cadry': 'カドリー',
        'valt_belt': 'バルタラ',
        'lunar': '月ネックレス',
        'river': '川ネックレス',
        'ethereal': '夢幻イヤリング',
        'orkin_belt': 'オルキンベルト' 
    }

    if item in accessories.keys():
        return accessories[item]
    
def ja_level_name(level):
    lv = {
        'pri': '真1',
        'duo': '真2',
        'tri': '真3',
        'tet': '真4',
        'pen': '真5'
    }

    if level in lv.keys():
        return lv[level]


def acc_pri(acc, tax):
    stack_cost = bs_armour * 31
    chance = 0.70
    # 18fsでsoftcap
    pri_expected_value = round((acc[1]*tax - stack_cost)*chance)
    str_pri_expected_value = '{:,}'.format(pri_expected_value)
    base_sell = round((acc[0]*2) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return str_pri_expected_value, str_base_sell

    '''
    真1を叩いた時の期待売上/str_pri_expected_value
    ベース2つを売った時の売上/str_base_sell
    以下同様
    '''

def acc_duo(acc, tax):
    try2_stack_cost = (150 + 31) * bs_armour
    try1_stack_cost = 31 * bs_armour
    s2_chance = 0.7*0.5
    s1f1_chance = 0.7*0.5
    f1_chance = 0.3
    # duoは40fsでsoftcap
    duo_expected_value = round( ((acc[2]*tax - try2_stack_cost)* s2_chance) + ((0 - try1_stack_cost)*s1f1_chance) + acc[0]*tax*f1_chance ) 
    str_duo_expected_value = '{:,}'.format(duo_expected_value)
    base_sell = round((acc[0]*3) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return str_duo_expected_value, str_base_sell

def acc_tri(acc, tax):
    try3_stack_cost = (200 + 150 + 31) * bs_armour
    try2_stack_cost = (150 + 31) * bs_armour
    try1_stack_cost = 31 * bs_armour
    s3_chance = 0.7*0.5*0.41
    s2f1_chance = 0.7*0.5*0.59
    s1f1_chance = 0.7*0.5
    f1s1_chance = 0.3*0.7
    f2_chance = 0.3*0.3
    tri_expected_value = round( ((acc[3]*tax - try3_stack_cost)* s3_chance) + ((0 - try2_stack_cost)* s2f1_chance) + ((0 - try1_stack_cost + acc[0]*tax)* s1f1_chance) + ((acc[1]*tax - try1_stack_cost)*f1s1_chance) + ((0 - try1_stack_cost)*f2_chance))
    str_tri_expected_value = '{:,}'.format(tri_expected_value)
    base_sell = round((acc[0]*4) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return str_tri_expected_value, str_base_sell

def acc_tet(acc, tax):
    try4_stack_cost = (2000 + 200 + 150 + 31)* bs_armour
    try3_stack_cost = (200 + 150 + 31) * bs_armour
    try2_stack_cost = (150 + 31) * bs_armour
    try1_stack_cost = 31 * bs_armour

    # straight
    s4_chance = 0.7*0.5*0.41*0.3
    # tri then fail
    s3f1_chance = 0.7*0.5*0.41*0.7
    # duo then fail, sell 1
    s2f1_chance = 0.7*0.5*0.59
    # pri then fail, then pri
    s1f1s1_chance = 0.7*0.5*0.7
    # pri then fail, then fail
    s1f1f1_chance = 0.7*0.5*0.3
    # #fail then duo
    f1s2_chance = 0.3*0.7*0.5
    # fail then pri, then fail
    f1s1f1_chance = 0.3*0.7*0.5
    # fail, fail, sell 1
    f2s1_chance = 0.3*0.3

    tet_expected_value = round(((acc[4]*tax - try4_stack_cost)* s4_chance) +
                                ((0 - try4_stack_cost)* s3f1_chance) + 
                                ((acc[0]*tax - try2_stack_cost)* s2f1_chance) +
                                ((acc[1]*tax - try1_stack_cost*2)* s1f1s1_chance) + 
                                ((0 - try1_stack_cost*2)* s1f1f1_chance) + 
                                ((acc[2]*tax - try2_stack_cost)* f1s2_chance) +
                                ((0 - try1_stack_cost)* f1s1f1_chance) +
                                ((acc[0]*tax)* f2s1_chance)
                                )
    str_tet_expected_value = '{:,}'.format(tet_expected_value)

    base_sell = round((acc[0]*5) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return str_tet_expected_value, str_base_sell

def acc_pen(acc, tax):
    try5_stack_cost = (20000)
    try4_stack_cost = (2000 + 200 + 150 + 31)* bs_armour
    try3_stack_cost = (200 + 150 + 31) * bs_armour
    try2_stack_cost = (150 + 31) * bs_armour
    try1_stack_cost = 31 * bs_armour

    # straight
    s5_chance = 0.7*0.5*0.41*0.3*0.115
    # tet then fail
    s4f1_chance = 0.7*0.5*0.41*0.3*0.885
    # tri then fail tet chal, then sell 1
    s3f1_chance = 0.7*0.5*0.41*0.7
    # duo then fail, then duo
    s2f1s2_chance = 0.7*0.5*0.59*0.7*0.5
    # duo then fail, then fail, sell 1
    s2f2_chance = 0.7*0.5*0.59*0.3
    # duo then fail, then pri, then fail duo chal
    s2f1s1f1_chance = 0.7*0.5*0.59*0.7*0.5
    # pri then fail, duo
    s1f1s2_chance = 0.7*0.5*0.7*0.5
    # pri then fail, pri then fail
    s1f1s1f1_chance = 0.7*0.5*0.7*0.5
    # pri then fail, fail, sell 1
    s1f2_chance = 0.7*0.5*0.3
    # fail, then tri
    f1s3_chance = 0.3*0.7*0.5*0.41
    # fail, then duo, then fail
    f1s2f1_chance = 0.3*0.7*0.5*0.59
    # fail, then pri, then fail sell 1
    f1s1f1_chance = 0.3*0.7*0.5
    # fail, fail, pri
    f2s1_chance = 0.3*0.3*0.7
    # fail, fail, fail
    f3_chance = 0.3*0.3*0.3

    pen_expected_value = round( ((acc[5]*tax - try5_stack_cost)*s5_chance) +
                               ((0 - try5_stack_cost)*s4f1_chance) +
                               ((acc[2]*tax - try2_stack_cost)*s3f1_chance) +
                               ((acc[0]*tax - try3_stack_cost)*s2f1s2_chance) +
                               ((acc[0]*tax - try2_stack_cost)*s2f2_chance) +
                               ((0 - try2_stack_cost - try1_stack_cost)*s2f1s1f1_chance) +
                               ((acc[2]*tax - try2_stack_cost)*s1f1s2_chance) +
                               ((0 - try1_stack_cost*2)*s1f1s1f1_chance) +
                               ((acc[0]*tax - try1_stack_cost)*s1f2_chance) +
                               ((acc[3]*tax - try3_stack_cost)*f1s3_chance) +
                               ((0 - try2_stack_cost)*f1s2f1_chance) +
                               ((acc[0]*tax - try1_stack_cost)*f1s1f1_chance) +
                               ((acc[1]*tax - try1_stack_cost)*f2s1_chance) +
                               ((0)*f3_chance)
                            )
    str_pen_expected_value = '{:,}'.format(pen_expected_value)

    base_sell = round((acc[0]*6) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return str_pen_expected_value, str_base_sell

@app.route('/', methods=['GET', 'POST'])
def index_root():
    return redirect(url_for('index'))

@app.route('/acc-enhancing', methods=['GET', 'POST'])
def index():
    tap = None
    sell = None
    name = None
    level = None
    item = None
    family_fame = False
    pp = False
    marchant_ring = False
    selected_item = None
    selected_level = None
    if request.method == 'POST':
        item = request.form['item']
        level = request.form['level']
        selected_item = item
        selected_level = level
        family_fame = "family_fame" in request.form
        pp = "pp" in request.form
        marchant_ring = "marchant_ring" in request.form
        tax = 0.6533
        if family_fame:
            tax = tax + 0.065
        if pp:
            tax = tax + 0.1949
        if marchant_ring:
            tax = tax + 0.0325


    # アクセサリーと強化関数のマッピング
    accessories = {
        'crescent': crescent,
        'tun_ring': tun_ring,
        'tun_belt': tun_belt,
        'disto': disto,
        'narc': narc,
        'ruin_ring': ruin_ring,
        'tun_ear': tun_ear,
        'tun_neck': tun_neck,
        'turo_belt': turo_belt,
        'basi_belt': basi_belt,
        'centa_belt': centa_belt,
        'ominous_ring': ominous_ring,
        'ogre_ring': ogre_ring,
        'laytenn': laytenn,
        'sicil': sicil,
        'dawn': dawn,
        'vaha': vaha,
        'cadry': cadry,
        'valt_belt': valt_belt,
        'lunar': lunar,
        'river': river,
        'ethereal': ethereal,
        'orkin_belt': orkin_belt
    }

    # 強化レベルと関数のマッピング
    enhancement_funcs = {
        'pri': acc_pri,
        'duo': acc_duo,
        'tri': acc_tri,
        'tet': acc_tet,
        'pen': acc_pen
    }

    # 選択されたアクセサリーと強化関数を取得
    selected_accessory = accessories.get(item)
    selected_func = enhancement_funcs.get(level)

    # 強化期待値と売り上げを計算
    if selected_accessory and selected_func:
        tap, sell = selected_func(selected_accessory, tax)

    name = ja_name(item)
    level = ja_level_name(level)

    return render_template('index.html', tap=tap, sell=sell, name=name, level=level,
                            family_fame=family_fame, pp=pp, marchant_ring=marchant_ring, 
                            selected_item=selected_item, selected_level=selected_level, 
                            updates=updates)

@app.route('/updates', methods=['GET', 'POST'])
def updates():

    updates = [
    {
        'date': '2023-03-27',
        'info': '真5の期待値計算を追加しました。'
    },
    {
        'date': '2023-03-26',
        'info': '真4の期待値計算とアクセサリーを追加しました。'
    },
    {
        'date': '2023-03-24',
        'info': 'アップデート情報と計算方法のセクションを追加しました。'
    },
    {
        'date': '2023-03-23',
        'info': 'ページを公開しました。'
    },
]
    
    return render_template('updates.html', updates=updates)

@app.route('/how-to-calc', methods=['GET', 'POST'])
def how_to_calc():
    return render_template('how-to-calc.html')

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
    app.run(debug=True)
    app.config['DEBUG'] = True