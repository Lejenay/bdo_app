from app_funcs import item_db

accessories = {
    'crescent': item_db.crescent,
    'tun_ring': item_db.tun_ring,
    'tun_belt': item_db.tun_belt,
    'disto': item_db.disto,
    'narc': item_db.narc,
    'ruin_ring': item_db.ruin_ring,
    'tun_ear': item_db.tun_ear,
    'tun_neck': item_db.tun_neck,
    'turo_belt': item_db.turo_belt,
    'basi_belt': item_db.basi_belt,
    'centa_belt': item_db.centa_belt,
    'ominous_ring': item_db.ominous_ring,
    'ogre_ring': item_db.ogre_ring,
    'laytenn': item_db.laytenn,
    'sicil': item_db.sicil,
    'dawn': item_db.dawn,
    'vaha': item_db.vaha,
    'cadry': item_db.cadry,
    'valt_belt': item_db.valt_belt,
    'lunar': item_db.lunar,
    'river': item_db.river,
    'ethereal': item_db.ethereal,
    'orkin_belt': item_db.orkin_belt,
    'manos_ring': item_db.manos_ring,
    'manos_earring': item_db.manos_earring,
    'manos_necklace': item_db.manos_necklace,
    'manos_belt': item_db.manos_belt
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