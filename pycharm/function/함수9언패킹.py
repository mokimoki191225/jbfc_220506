
#튜플

def get_a(a,b):
    return a*b

data = 10, 20

# print(get_a(data))
print(get_a(*data)) # * 언패킹 풀어서 나눠가지고 호출한다.

#이어서 글자쓰기

# def get_b(name,greeting):
#     return '{name}님, {greeting}' .format(name=name, greeting=greeting)
# get_b_dict = {'name':'영목', 'greeting':'방가'}
# print(get_b(**get_b_dict))

def get_b(**greeting):
    for key,value in greeting.items():
        print('%s : %s' %(key,value))
get_b (name = '영목', greeting = '방가')




