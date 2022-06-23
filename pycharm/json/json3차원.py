
import json

data = '''
{
 "name" : "홍길동",
 "dog"  : {
    "name" : "순둥이",
    "toys" : [
            { "name" : "뽀로로"},
            { "name" : "토마스"}
            ]
    }
}
'''

with open ('data/person.json', 'w') as fp:
    fp.write(data)

with open ('data/person.json') as data_file:
    person = json.load(data_file)

print('*'*50)

# print(person['dog']['toys'][0])

text = '{}의 개 {}의 장난감은 {},{}입니다.'.format(
    person['name'],
    person['dog']['name'],
    person['dog']['toys'][0]['name'], #리스트선택
    person['dog']['toys'][1]['name']  #dict형은 key입력
)

print(text)
