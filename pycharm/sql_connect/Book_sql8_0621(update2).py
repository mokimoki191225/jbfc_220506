
from day0620.database import common as dbcomn
from day0620.database import set_one as one
import pandas as pd

def getBooksDF(books):

    ret_df = pd.DataFrame()

    title = list()
    published_data = list()
    publisher = list()
    pages = list()
    recommendation = list()

    column_name = ['title', 'published_data', 'publisher', 'pages', 'recommendation']

    for book in books:
        title.append(book[0])
        published_data.append(book[1])
        publisher.append(book[2])
        pages.append(book[3])
        recommendation.append(book[4])

    data = {'title' : title,
            'published_data' : published_data,
            'publisher' : publisher,
            'pages': pages,
            'recommendation': recommendation}

    ret_df = pd.DataFrame(data, columns=column_name)

    return ret_df

def update_books(db_name):

    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomn.get_connection(db_name)
        # 커서 확보, 명령어 실행이 가능하다
        cur = conn.cursor()

        # 데이터 수정 SQL 실행 (제목이 ?인 책의 추천 유무를 ?로 변경하라)
        db_sql = 'UPDATE book_mgr set recommendation=%s where title=%s ' # <-- 스페이스를 줘야 조건에 맞는게 추출된다.

        #명령어를 실행하는 execute이다.
        cur.execute(db_sql, (5,'메가트랜드'))
        # 조회한 데이터 불러오기
        print('[7] 데이터 수정하기')
        # books = cur.fetchall()
        # ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        if is_success:
            #데이터베이스 반영
            conn.commit()
        else:
            #데이터베이스 철회
            conn.rollback()
        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success

if __name__ == '__main__':

    db_name = 'bigpy'

    is_success, ret_df1 = one.select_one_books(db_name)

    if update_books(db_name):
        print('데이터를 수정하였습니다.')
    else:
        print('데이터를 수정하지 못했습니다.')

    is_success, ret_df2 = one.select_one_books(db_name)

    books_df = pd.concat([ret_df1,ret_df2],axis=0)
    books_df['update'] = ['수정전','수정후']
    books_df.set_index('update',inplace =True)
    print(books_df)





