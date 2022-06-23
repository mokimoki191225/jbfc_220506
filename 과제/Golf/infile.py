

def read_csv(filename):
    fp = open(filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()

    elements = []
    key_rows = []

    rows = data.split('\n')
    # print(rows[0])
    key_rows = rows[0].split(',')

    for idx in range(len(key_rows)):
        key_rows[idx] = key_rows[idx].strip()
        # print(key_rows[idx])

    print('-'*50)

    for row in rows[1:]: # 8번 돈다
        fields = row.split(",")
        # print(row)
        # print(fields)
        for idx in range(len(key_rows)):
            fields[idx] = fields[idx].strip()
            print('{} : {} '.format(key_rows[idx],fields[idx]))
        print('-'*50)

    return elements

# filename = "./data/jbbank2.csv"
# corprations = read_csv(filename)

# print('*' * 50)