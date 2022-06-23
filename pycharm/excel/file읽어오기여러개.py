
# 헤더 갯수세기

def

def read_csv(filename):
    fp      =   open(filename, "r", encoding="utf-8")
    data    =   fp.read()
    fp.close()

    elements=[]

    rows = data.split('\n')

    for row in rows:
        fields = row.split(",")
        for x_num in range():

        name    = fields[0].strip()
        date    = fields[1].strip()
        ceo     = fields[2].strip()
        merc    = fields[3].strip()
        ph      = fields[4].strip()
        add     = fields[5].strip()

        element = {
            "회사명"   : name
          , "설립일"   : date
          , "대표이사" : ceo
          , "업종"    : merc
          , "PH"     : ph
          , "add"    : add

        }
        elements.append(element)

    return elements

filename = "./data/jbbank2.csv"
corprations = read_csv(filename)

print(corprations)

for corpration in corprations:
    print(corpration)

print('*'*50)
print(corprations[0]['회사명'])