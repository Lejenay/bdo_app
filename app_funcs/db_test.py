# from pymongo import MongoClient

# from item_api import api_call


# client = MongoClient("mongodb://localhost:27017/")

# db = client["bdo_items"]

# enhancement_items = db["enhance_items"]

# """Get enhancement item price

# Returns:
#     int: price of enhancement item"""

# bs_armour = api_call.item_price_list(16002)
# bs_wepon = api_call.item_price_list(16001)
# concentrated_magical_black_gem = api_call.item_price_list(4987)

# enhance_items = [
#     {"name": "bs_armour", "ja_name": "ブラックストーン(防具)","price": bs_armour},
#     {"name": "bs_wepon", "ja_name": "ブラックストーン(武器)", "price": bs_wepon},
#     {"name": "concentrated_magical_black_gem", "ja_name": "凝縮された魔力の黒い結晶", "price": concentrated_magical_black_gem}
# ]

# enhancement_items.insert_many(enhance_items)


# acc_items = db["accessory_items"]

# """Get accessory item price

# Returns:
#     int: return LIST of accessory price
#         [base_price, pri_price, duo_price, tri_price, tet_price, pen_price]"""

# crescent = api_call.acc_price_list(12031)
# tun_ring = api_call.acc_price_list(12061)
# ruin_ring = api_call.acc_price_list(12060)
# disto = api_call.acc_price_list(11853)
# narc = api_call.acc_price_list(11834)
# tun_belt = api_call.acc_price_list(12237)
# tun_ear = api_call.acc_price_list(11828)
# tun_neck = api_call.acc_price_list(11629)
# turo_belt = api_call.acc_price_list(12257)
# basi_belt = api_call.acc_price_list(12230)
# centa_belt = api_call.acc_price_list(12229)
# ominous_ring = api_call.acc_price_list(12068)
# ogre_ring = api_call.acc_price_list(11607)
# laytenn = api_call.acc_price_list(11630)
# sicil = api_call.acc_price_list(11625)
# dawn = api_call.acc_price_list(11855)
# vaha = api_call.acc_price_list(11875)
# cadry = api_call.acc_price_list(12032)
# valt_belt = api_call.acc_price_list(12236)
# ethereal = api_call.acc_price_list(11856)
# lunar = api_call.acc_price_list(11663)
# river = api_call.acc_price_list(11662)
# orkin_belt = api_call.acc_price_list(12251)
# manos_ring = api_call.acc_price_list(705511)
# manos_earring = api_call.acc_price_list(705510)
# manos_necklace = api_call.acc_price_list(705509)
# manos_belt = api_call.acc_price_list(705512)

# accessory_items = [
#     {"name": "crescent", "ja_name": "三日月守護者のリング","price": crescent},
#     {"name": "tun_ring", "ja_name": "ツングラドのリング", "price": tun_ring},
#     {"name": "ruin_ring", "ja_name": "廃墟の瞳リング", "price": ruin_ring},
#     {"name": "disto", "ja_name": "黒い侵食のイヤリング", "price": disto},
#     {"name": "narc", "ja_name": "ナクの耳飾り", "price": narc},
#     {"name": "tun_belt", "ja_name": "ツングラドのベルト", "price": tun_belt},
#     {"name": "tun_ear", "ja_name": "ツングラドのイヤリング", "price": tun_ear},
#     {"name": "tun_neck", "ja_name": "ツングラドのネックレス", "price": tun_neck},
#     {"name": "turo_belt", "ja_name": "トゥーロのベルト", "price": turo_belt},
#     {"name": "basi_belt", "ja_name": "バジリスクのベルト", "price": basi_belt},
#     {"name": "centa_belt", "ja_name": "ケンタウロスのベルト", "price": centa_belt},
#     {"name": "ominous_ring", "ja_name": "不気味な背後のリング", "price": ominous_ring},
#     {"name": "ogre_ring", "ja_name": "オーガのリング", "price": ogre_ring},
#     {"name": "laytenn", "ja_name": "ライテンの動力石", "price": laytenn},
#     {"name": "sicil", "ja_name": "シチルのネックレス", "price": sicil},
#     {"name": "dawn", "ja_name": "黎明のイヤリング", "price": dawn},
#     {"name": "vaha", "ja_name": "バアの暁", "price": vaha},
#     {"name": "cadry", "ja_name": "カドリー守護者のリング", "price": cadry},
#     {"name": "valt_belt", "ja_name": "バルタラの隠れた光ベルト", "price": valt_belt},
#     {"name": "ethereal", "ja_name": "夢幻のイヤリング", "price": ethereal},
#     {"name": "lunar", "ja_name": "月明かりに酔った月のネックレス", "price": lunar},
#     {"name": "river", "ja_name": "目覚めた川のネックレス", "price": river},
#     {"name": "orkin_belt", "ja_name": "オルキンラドのベルト", "price": orkin_belt},
#     {"name": "manos_ring", "ja_name": "マノスリング", "price": manos_ring},
#     {"name": "manos_earring", "ja_name": "マノスイヤリング", "price": manos_earring},
#     {"name": "manos_necklace", "ja_name": "マノスネックレス", "price": manos_necklace},
#     {"name": "manos_belt", "ja_name": "マノスベルト", "price": manos_belt}
# ]

# acc_items.insert_many(accessory_items)

# def result():
#     for stack_e in enhancement_items.find():
#         return stack_e
#     for stack_a in acc_items.find():
#         return stack_a