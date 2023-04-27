import re
import requests

def acc_price_list(item_id):
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



def item_price_list(item_id):
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