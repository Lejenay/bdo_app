from flask import Flask, render_template, request, jsonify
from  app_funcs import calculation_v1, calculation_v2, funcs

app = Flask(__name__)

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
        'pri': calculation_v1.acc_pri,
        'duo': calculation_v1.acc_duo,
        'tri': calculation_v1.acc_tri,
        'tet': calculation_v1.acc_tet,
        'pen': calculation_v1.acc_pen
    }

    # 選択されたアクセサリーと強化関数を取得
    selected_accessory = funcs.accessories.get(item)
    selected_func = enhancement_funcs.get(level)

    # 強化期待値と売り上げを計算
    if selected_accessory and selected_func:
        tap, sell, str_tap, str_sell = selected_func(selected_accessory, tax)

    name = funcs.ja_name(item)
    level = funcs.ja_level_name(level)

    # レスポンスを作成
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
            'pri': calculation_v2.acc_pri_v2,
            'duo': calculation_v2.acc_duo_v2,
            'tri': calculation_v2.acc_tri_v2,
            'tet': calculation_v2.acc_tet_v2,
            'pen': calculation_v2.acc_pen_v2
        }

        # 選択されたアクセサリーと強化関数を取得
        selected_accessory = funcs.accessories.get(item)
        selected_func = enhancement_funcs.get(level)

        # 強化期待値を計算
        if selected_accessory and selected_func:
            int_profit, str_profit = selected_func(selected_accessory, tax, acc_alc)

        name = funcs.ja_name(item)
        level = funcs.ja_level_name(level)
    
    else:
        int_profit = None
        str_profit = None

    # レスポンスを作成
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