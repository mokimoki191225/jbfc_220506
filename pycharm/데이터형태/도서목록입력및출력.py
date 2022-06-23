
books = list()      # 책 목록 선언

###### step1 -> 입력 : 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

'''
for book in books:  # 책 한 권씩 꺼내기 위한 루프 선언
    print(book)     # 책 한 권 데이터 출력
'''

# print(books[2])
# print(books[2]['추천유무'])
# print(books[4]['쪽수'])

###### stpe2 -> 유형작성하기, 선언하기
many_page = list()                              # 책 리스트 선언
recommends = list()                             # 책 리스트 선언
all_pages = int()                               # 전체 쪽수 변수 선언
all_pages = sum([book['쪽수'] for book in books]) # 전체 쪽수 변수 선언, 비슷하게 짧은 언어 "루비"
print(all_pages)
pub_companies = set()                           # 출판사 집합 선


###### stpe3 로직구현 -> 데이터 등록, 수정, 삭제
# many_page
for book in books:
    if book['쪽수']>250:
        many_page.append(book['제목'])
        print(many_page)

# 추천책
for book in books:
    if book['추천유무']==True:
        recommends.append(book['제목'])
        print(recommends)

# 전체쪽수
for book in books:
    all_pages+=book['쪽수']
    print(all_pages)

# 출판사
for book in books:
    pub_companies.update(sorted(book['출판사']))
    print(pub_companies)

###### step4. 결과값 출력 -> 책 한 권씩 꺼내기 위한 루프 선언
print('쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)