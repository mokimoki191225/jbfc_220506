
# STEP0. 과제
# 1. 쪽수가 250넘는 리스트
# 2. 내가 추천하는 책 리스트
# 3. 내가 읽은 책 전체 쪽수
# 4. 내가 읽은 책의 출판사 목록

# STEP 00. 변수선언

class BookMaster:
    books      = list()
    many_page  = []
    recommend  = []
    sum_page   = []
    get_chool  = []

    # STEP1. 데이터 입력

    def reg_book(self):
        self.books.append({'제목': '파이썬 프로그램', '출판연도': '2016', '출판사': 'A', '쪽수': 200, '추천유무': False})
        self.books.append({'제목': '플랫폼 비즈니스', '출판연도': '2013', '출판사': 'B', '쪽수': 584, '추천유무': True})
        self.books.append({'제목': '빅데이터 마케팅', '출판연도': '2014', '출판사': 'A', '쪽수': 296, '추천유무': True})
        self.books.append({'제목': '외식경영 전문가', '출판연도': '2010', '출판사': 'B', '쪽수': 526, '추천유무': False})
        self.books.append({'제목': '십억만 벌어보자', '출판연도': '2013', '출판사': 'A', '쪽수': 248, '추천유무': True})

    # STEP2. 함수선언 및 변수 선언

    def many_pages(self):
        self.many_page = [book['제목'] for book in self.books if book['쪽수'] > 250]

    def get_recommends(self):
        self.recommend = [book['제목'] for book in self.books if book['추천유무']]

    def sum_pages(self):
        self.sum_page = sum([book['쪽수'] for book in self.books])

    def get_chools(self):
        self.get_chool = list(set([book['출판사'] for book in self.books]))

    # STEP3. Class 출력

    def final_display(self):
        print('##도서목록 출력 내용## \n', '-'*90)
        print('1.쪽수가 250쪽 넘는 책 리스트', self.many_page[0])
        print('2.내가 추천하는 책리스트', self.recommend)
        print('3.내가 읽은책 전체 쪽수 {:0,.1f}'.format(self.sum_page))
        print('4.내가 읽은 책의 출판사 목록', sorted(self.get_chool))

bookmaster = BookMaster()

bookmaster.reg_book()
bookmaster.many_pages()
bookmaster.get_recommends()
bookmaster.sum_pages()
bookmaster.get_chools()

bookmaster.final_display()














