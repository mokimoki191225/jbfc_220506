
def cs_num(num):
    ret_num = str()
    str_num = str(num)
    rev_num = str_num[::-1]
    tmp_num = str()

    for i in range(len(rev_num)): #3자리
        if (i>0) and (i%3==0):
            tmp_num = tmp_num + ','
        tmp_num = tmp_num + rev_num[i]

    ret_num = tmp_num[::-1]
    return ret_num
