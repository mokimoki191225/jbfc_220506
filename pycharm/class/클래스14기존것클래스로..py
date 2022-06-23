
class BookManager:
    books         = list()
    many_page     = []
    recommends    = []
    pub_companies = []
    all_pages     = int()

    def reg_book(self,book):
        self.books.append(book)

    def get_book(self):
        return self.books

    def get_many_page(self):
        self.many_page = [ book['제목'] for book in self.books if book['쪽수']>250]

    def get_recommends(self):
        self.recommends = [book['제목'] for book in self.books if book['추천유무']]

    def get_pub_companies(self):
        pub_companies = { book['출판사'] for book in self.books}

    def get_all_pages(self):
        self.all_pages = sum([book['쪽수'] for book in self.books])

    def final_display(self):
        print('##도서목록출력내용##\n', '-'*50)
        print('1.쪽수가 250쪽 넘는 책 리스트=', self.many_page)
        print('2.내가 추천하는 책 리스트=', self.get_recommends)
        print('3.내가 읽은 책 전체 쪽수=', self.all_pages)
        print('4.내가 읽은 책의 출판사 목록=', sorted(self.get_pub_companies))

bookManager = BookManager()
print('책관리자 클래스를 통해 책정보 등록')
bookManager.reg_book({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
bookManager.reg_book({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
bookManager.reg_book({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
bookManager.reg_book({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
bookManager.reg_book({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

print('-'*50)

print('등록된 책정보 확인')
books = bookManager.get_book()
for book in books:
    print(book)

print('-'*50)

bookManager.get_book()
bookManager.get_many_page()
bookManager.get_recommends()
bookManager.get_all_pages()
bookManager.get_pub_companies()

bookManager.final_display()




