from app_funcs import item_db, funcs

inverce_accessories = {tuple(v):k for k, v in funcs.accessories.items()}
def acc_pri_v2(acc, tax, acc_alc):
    if "manos" in inverce_accessories[tuple(acc)]:
        success_chance = 0.75
        fail_chance = 0.25
        try1_stack_cost = 10 * item_db.concentrated_magical_black_gem
        if acc_alc:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost - acc[0])*success_chance) - ((acc[0] + try1_stack_cost)*fail_chance))
        else:
            pri_expected_value = round( ((acc[1]*tax - try1_stack_cost)*success_chance) - ((acc[0] + try1_stack_cost)*fail_chance))
    else:
        success_chance = 0.7
        fail_chance = 0.3
        try1_stack_cost = 31 * item_db.bs_armour
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
        try2_stack_cost = 11 * item_db.concentrated_magical_black_gem
        if acc_alc:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost - acc[1])*success_chance) - ((acc[1] + try2_stack_cost)*fail_chance))
        else:
            duo_expected_value = round( ((acc[2]*tax - try2_stack_cost)*success_chance) - ((acc[1] + try2_stack_cost)*fail_chance))
    else:
        success_chance = 0.5
        fail_chance = 0.5
        try2_stack_cost = 150 * item_db.bs_armour
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
        try3_stack_cost = 13 * item_db.concentrated_magical_black_gem
        if acc_alc:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost - acc[2])*success_chance) - ((acc[2] + try3_stack_cost)*fail_chance))
        else:
            tri_expected_value = round( ((acc[3]*tax - try3_stack_cost)*success_chance) - ((acc[2] + try3_stack_cost)*fail_chance))
    else:
        success_chance = 0.41
        fail_chance = 0.59
        try3_stack_cost = 200 * item_db.bs_armour
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
        try4_stack_cost = 16 * item_db.concentrated_magical_black_gem
        if acc_alc:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost - acc[3])*success_chance) - ((acc[3] + try4_stack_cost)*fail_chance))
        else:
            tet_expected_value = round( ((acc[4]*tax - try4_stack_cost)*success_chance) - ((acc[3] + try4_stack_cost)*fail_chance))
    else:
        success_chance = 0.3
        fail_chance = 0.7
        try4_stack_cost = 2000 * item_db.bs_armour
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
        try5_stack_cost = 20 * item_db.concentrated_magical_black_gem
        if acc_alc:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost - acc[4])*success_chance) - ((acc[4] + try5_stack_cost)*fail_chance))
        else:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost)*success_chance) - ((acc[4] + try5_stack_cost)*fail_chance))
    else:
        success_chance = 0.115
        fail_chance = 0.885
        try5_stack_cost = 20000 * item_db.bs_armour
        if acc_alc:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost - acc[4] - acc[0])*success_chance) - ((acc[4] + acc[0])*fail_chance))
        else:
            pen_expected_value = round( ((acc[5]*tax - try5_stack_cost)*success_chance) - ((acc[4] + acc[0])*fail_chance) )

    str_pen_expected_value = '{:,}'.format(pen_expected_value)

    return pen_expected_value, str_pen_expected_value