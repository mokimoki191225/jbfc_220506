
from day0620.database import common as dbcomn
from day0620.database import set_one as one
import pandas as pd

if __name__ == '__main__':

    db_name = 'bigpy'
    title = '사물인터넷 전망4'

    is_success, books_df1 = one.find_books_of_title(db_name,title)

    if one.update_recommendation(db_name, recommendation=7, title=title):
        print('데이터를 수정하였습니다.')
    else:
        print('데이터를 수정하지 못했습니다.')

    is_success, book_df2 = one.find_books_of_title(db_name,title)

    books_df = pd.concat([books_df1,book_df2],axis=0)
    books_df['update'] = ['수정전','수정후']
    books_df.set_index('update',inplace =True)
    print(books_df)





