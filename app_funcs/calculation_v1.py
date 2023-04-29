# 真nを叩いた時の期待売上(string) / str_{n}_expected_value
# ベース2つを売った時の売上(string) / str_base_sell

# *スタックと必要ブラックストーン数、成功確率の関係
# format.{enhancement level / amount of bs / fail stacks / success chance }
# pri(真1) / 31bs(ブラックストーン) / 18fs(スタック18) / 0.700(強化成功確率)
# duo / 150bs / 40fs / 0.500
# tri / 200bs / 44fs / 0.405
# tet / 2000bs / 110fs / 0.300
# pen / 20000bs / 490fs(不可能なので220fsで計算) / 0.115(220fs)

import app_funcs.item_db as item_db

def acc_pri(acc, tax):
    stack_cost = item_db.bs_armour * 31
    chance = 0.70
    pri_expected_value = round((acc[1]*tax - stack_cost)*chance)
    str_pri_expected_value = '{:,}'.format(pri_expected_value)
    base_sell = round((acc[0]*2) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return pri_expected_value, base_sell, str_pri_expected_value, str_base_sell

def acc_duo(acc, tax):
    try2_stack_cost = (150 + 31) * item_db.bs_armour
    try1_stack_cost = 31 * item_db.bs_armour
    s2_chance = 0.7*0.5
    s1f1_chance = 0.7*0.5
    f1_chance = 0.3
    duo_expected_value = round( ((acc[2]*tax - try2_stack_cost)* s2_chance) + ((0 - try1_stack_cost)*s1f1_chance) + acc[0]*tax*f1_chance ) 
    str_duo_expected_value = '{:,}'.format(duo_expected_value)
    base_sell = round((acc[0]*3) *tax)
    str_base_sell = '{:,}'.format(base_sell)

    return duo_expected_value, base_sell, str_duo_expected_value, str_base_sell

def acc_tri(acc, tax):
    try3_stack_cost = (200 + 150 + 31) * item_db.bs_armour
    try2_stack_cost = (150 + 31) * item_db.bs_armour
    try1_stack_cost = 31 * item_db.bs_armour
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
    try4_stack_cost = (2000 + 200 + 150 + 31)* item_db.bs_armour
    try2_stack_cost = (150 + 31) * item_db.bs_armour
    try1_stack_cost = 31 * item_db.bs_armour

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
    try4_stack_cost = (2000 + 200 + 150 + 31)* item_db.bs_armour
    try3_stack_cost = (200 + 150 + 31) * item_db.bs_armour
    try2_stack_cost = (150 + 31) * item_db.bs_armour
    try1_stack_cost = 31 * item_db.bs_armour

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