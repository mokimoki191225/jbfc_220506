from sql연결.database import common as dbcomn
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

def select_some_books(db_name, number):

    ret_df = pd.DataFrame()
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomn.get_connection(db_name)
        # 커서 확보, 명령어 실행이 가능하다
        cur = conn.cursor()

        # 조회용 SQL 실행
        db_sql = 'SELECT * FROM book_mgr'
        #명령어를 실행하는 execute이다.
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[2] 데이터 일부 출력하기')
        books = cur.fetchmany(number)
        # 일부만 가져오기

        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success, ret_df

if __name__ == '__main__':

    db_name = 'bigpy'

    is_success, books_df = select_some_books(db_name, number=1)

    if is_success:
        print('조회된 데이터는 총 %d건 입니다.' %len(books_df))
    else:
        print('데이터를 조회하지 못했습니다.')

    print(type(books_df))
    print(books_df)





