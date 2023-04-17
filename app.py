from flask import Flask, render_template, request, url_for, jsonify
from api_call_module import api_call
app = Flask(__name__)


# DB // SQLを導入したいですまる
bs_armour = api_call.item_api_call(16002)
bs_wepon = api_call.item_api_call(16001)
concentrated_magical_black_gem = api_call.item_api_call(4987)
crescent = api_call.acc_api_call(12031)
tun_ring = api_call.acc_api_call(12061)
ruin_ring = api_call.acc_api_call(12060)
disto = api_call.acc_api_call(11853)
narc = api_call.acc_api_call(11834)
tun_belt = api_call.acc_api_call(12237)
tun_ear = api_call.acc_api_call(11828)
tun_neck = api_call.acc_api_call(11629)
turo_belt = api_call.acc_api_call(12257)
basi_belt = api_call.acc_api_call(12230)
centa_belt = api_call.acc_api_call(12229)
ominous_ring = api_call.acc_api_call(12068)
ogre_ring = api_call.acc_api_call(11607)
laytenn = api_call.acc_api_call(11630)
sicil = api_call.acc_api_call(11625)
dawn = api_call.acc_api_call(11855)
vaha = api_call.acc_api_call(11875)
cadry = api_call.acc_api_call(12032)
valt_belt = api_call.acc_api_call(12236)
ethereal = api_call.acc_api_call(11856)
lunar = api_call.acc_api_call(11663)
river = api_call.acc_api_call(11662)
orkin_belt = api_call.acc_api_call(12251)
manos_ring = api_call.acc_api_call(705511)
manos_earring = api_call.acc_api_call(705510)
manos_necklace = api_call.acc_api_call(705509)
manos_belt = api_call.acc_api_call(705512)

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
    'orkin_belt': orkin_belt,
    'manos_ring': manos_ring,
    'manos_earring': manos_earring,
    'manos_necklace': manos_necklace,
    'manos_belt': manos_belt
}


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
        'orkin_belt': 'オルキンベルト',
        'manos_ring': 'マノスリング',
        'manos_earring': 'マノスイヤリング',
        'manos_necklace': 'マノスネックレス',
        'manos_belt': 'マノスベルト'
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

    return pri_expected_value, base_sell, str_pri_expected_value, str_base_sell

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

    return duo_expected_value, base_sell, str_duo_expected_value, str_base_sell

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

    return tri_expected_value, base_sell, str_tri_expected_value, str_base_sell

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

    return tet_expected_value, base_sell, str_tet_expected_value, str_base_sell

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

    return pen_expected_value, base_sell, str_pen_expected_value, str_base_sell

inverce_accessories = {tuple(v):k for k, v in accessories.items()}
def acc_pri_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.75
        fail_chance = 0.25
        try1_stack_cost = 10 * concentrated_magical_black_gem
        if acc_alc:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost - acc[0])*success_chance) - ((acc[0] + try1_stack_cost)*fail_chance))
        else:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost)*success_chance) - ((acc[0] + try1_stack_cost)*fail_chance))
    else:
        success_chance = 0.7
        fail_chance = 0.3
        try1_stack_cost = 31 * bs_armour
        if acc_alc:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost - acc[0]*2)*success_chance) - ((acc[0]*2)*fail_chance))
        else:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost)*success_chance) - ((acc[0]*2)*fail_chance))

    str_pri_expected_value = '{:,}'.format(pri_expected_value)

    return pri_expected_value , str_pri_expected_value

def acc_duo_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.45
        fail_chance = 0.55
        try2_stack_cost = 11 * concentrated_magical_black_gem
        if acc_alc:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost - acc[1])*success_chance) - ((acc[1] + try2_stack_cost)*fail_chance))
        else:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost)*success_chance) - ((acc[1] + try2_stack_cost)*fail_chance))
    else:
        success_chance = 0.5
        fail_chance = 0.5
        try2_stack_cost = 150 * bs_armour
        if acc_alc:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost - acc[1] - acc[0])*success_chance) - ((acc[1] + acc[0])*fail_chance))
        else:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost)*success_chance) - ((acc[1] + acc[0])*fail_chance) )

    str_duo_expected_value = '{:,}'.format(duo_expected_value)

    return duo_expected_value, str_duo_expected_value

def acc_tri_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.3
        fail_chance = 0.7
        try3_stack_cost = 13 * concentrated_magical_black_gem
        if acc_alc:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost - acc[2])*success_chance) - ((acc[2] + try3_stack_cost)*fail_chance))
        else:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost)*success_chance) - ((acc[2] + try3_stack_cost)*fail_chance))
    else:
        success_chance = 0.41
        fail_chance = 0.59
        try3_stack_cost = 200 * bs_armour
        if acc_alc:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost - acc[2] - acc[0])*success_chance) - ((acc[2] + acc[0])*fail_chance))
        else:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost)*success_chance) - ((acc[2] + acc[0])*fail_chance) )

    str_tri_expected_value = '{:,}'.format(tri_expected_value)

    return tri_expected_value, str_tri_expected_value

def acc_tet_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.15
        fail_chance = 0.85
        try4_stack_cost = 16 * concentrated_magical_black_gem
        if acc_alc:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost - acc[3])*success_chance) - ((acc[3] + try4_stack_cost)*fail_chance))
        else:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost)*success_chance) - ((acc[3] + try4_stack_cost)*fail_chance))
    else:
        success_chance = 0.3
        fail_chance = 0.7
        try4_stack_cost = 2000 * bs_armour
        if acc_alc:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost - acc[3] - acc[0])*success_chance) - ((acc[3] + acc[0])*fail_chance))
        else:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost)*success_chance) - ((acc[3] + acc[0])*fail_chance) )

    str_tet_expected_value = '{:,}'.format(tet_expected_value)

    return tet_expected_value, str_tet_expected_value

def acc_pen_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.05
        fail_chance = 0.95
        try5_stack_cost = 20 * concentrated_magical_black_gem
        if acc_alc:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost - acc[4])*success_chance) - ((acc[4] + try5_stack_cost)*fail_chance))
        else:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost)*success_chance) - ((acc[4] + try5_stack_cost)*fail_chance))
    else:
        success_chance = 0.115
        fail_chance = 0.885
        try5_stack_cost = 20000 * bs_armour
        if acc_alc:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost - acc[4] - acc[0])*success_chance) - ((acc[4] + acc[0])*fail_chance))
        else:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost)*success_chance) - ((acc[4] + acc[0])*fail_chance) )

    str_pen_expected_value = '{:,}'.format(pen_expected_value)

    return pen_expected_value, str_pen_expected_value

@app.route('/acc-enhancing-v1')
def acc_enhancing_v1():
    return render_template('index.html')

@app.route('/acc-enhancing-v1-ajax', methods=['POST', 'GET'])
def index():
    tap = 0
    sell = 0
    str_tap = None
    str_sell = None
    name = None
    level = None
    item = None
    family_fame = False
    pp = False
    marchant_ring = False
    if request.method == 'POST':
        data = request.get_json()
        item = data['item']
        level = data['level']
        family_fame = data['family_fame']
        pp = data['pp']
        marchant_ring = data['marchant_ring']
        
        tax = 0.6533
        if family_fame:
            tax += 0.065
        if pp:
            tax += 0.1949
        if marchant_ring:
            tax += 0.0325

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
        tap, sell, str_tap, str_sell = selected_func(selected_accessory, tax)

    name = ja_name(item)
    level = ja_level_name(level)

    response = {
        'result':{
            'tap': tap,
            'sell': sell,
            'str_tap': str_tap,
            'str_sell': str_sell,
            'name': name,
            'level': level,
        }
    }

    return(jsonify(response))

@app.route('/acc-enhancing-v2')
def acc_calc_v2():
    return render_template('acc-enhancing-v2.html')

@app.route('/acc-enhancing-v2-ajax', methods=['GET', 'POST'])
def acc_calc_v2_ajax():
    int_profit = 0
    str_profit = None
    name = None
    level = None
    item = None
    family_fame = False
    pp = False
    marchant_ring = False
    acc_alc = False
    tax = 0.6533

    if request.method == 'POST':
        data = request.get_json()
        acc_alc = data['acc_alc']
        item = data['item']
        level = data['level']
        family_fame = data['family_fame']
        pp = data['pp']
        marchant_ring = data['marchant_ring']
        
        if family_fame:
            tax += 0.065
        if pp:
            tax += 0.1949
        if marchant_ring:
            tax += 0.0325

        enhancement_funcs = {
            'pri': acc_pri_v2,
            'duo': acc_duo_v2,
            'tri': acc_tri_v2,
            'tet': acc_tet_v2,
            'pen': acc_pen_v2
        }

        # 選択されたアクセサリーと強化関数を取得
        selected_accessory = accessories.get(item)
        selected_func = enhancement_funcs.get(level)

        # 強化期待値を計算
        if selected_accessory and selected_func:
            int_profit, str_profit = selected_func(selected_accessory, tax, acc_alc)

        name = ja_name(item)
        level = ja_level_name(level)
    
    else:
        int_profit = None
        str_profit = None

    response = {
        'result':{
            'int_profit': int_profit,
            'str_profit': str_profit,
            'name': name,
            'level': level,
        }
    }

    return(jsonify(response))


@app.route('/updates', methods=['GET', 'POST'])
def updates():

    updates = [
    {
        'date': '2023-04-11',
        'info': 'Ajaxを導入しました。(自己満足)'
    },
    {
        'date': '2023-04-08',
        'info': '計算機v2にマノスアクセ・アクセ錬金（金策）計算を追加しました。'
    },
    {
        'date': '2023-04-07',
        'info': '期待値計算機のバージョン2を公開しました。'
    },
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

@app.route('/', methods=['GET', 'POST'])
def index_root():
    return render_template('home.html')

@app.route('/privacy', methods=['GET', 'POST'])
def privacy():
    return render_template('privacy.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)