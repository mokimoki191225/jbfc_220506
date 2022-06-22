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

def find_big_books(db_name):

    ret_df = pd.DataFrame()
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomn.get_connection(db_name)
        # 커서 확보, 명령어 실행이 가능하다
        cur = conn.cursor()

        # 조회용 SQL 실행
        db_sql = 'SELECT * FROM book_mgr ' # <-- 스페이스를 줘야 조건에 맞는게 추출된다.
        db_sql += 'WHERE pages > 300'

        #명령어를 실행하는 execute이다.
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[4] 페이지 많은 책 출력하기')
        books = cur.fetchall()
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

    is_success, books_df = find_big_books(db_name)

    if is_success:
        print('조건에 맞는 데이터는 총 %d건 입니다. \n (조건:pages>300)' %len(books_df))
    else:
        print('데이터를 조회하지 못했습니다.')

    print(type(books_df))
    print(books_df)





