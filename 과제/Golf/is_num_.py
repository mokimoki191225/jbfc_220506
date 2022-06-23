
def is_num(str_num):
    ret_num = True
    ret_msg = str()
    str_num = str(str_num)

    num_chk_list = list('0123456789')

    for char in str_num:
        is_num  = char in num_chk_list
        ret_num = ret_num * is_num
        ret_msg = '정수입니다.'
        if not is_num:
            ret_msg = '정수아닙니다.'
            break

    return ret_num, ret_msg

# print(is_num(-5))

# a = is_num()
# a.is_num()
# print()
