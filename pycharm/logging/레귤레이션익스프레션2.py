import re

#\w (1 문자)
#\d (1 숫자)
#\s (1 spcd)

# + (1,....,N)
# ? (0,1)
# * (0,1,...N)

# \d{N} (숫자가 N개 나온다.)
# \d{N,M} (숫자가 N~M개 나온다.)

text = """
옛날 옛적에 김진수라는 사람이 살았습니다.
그에게는 5형제가 있었는데, 김진수, 김진구, 김진용, 김진태, 김진욱 이렇게 다섯명 있었습니다.
그리고 그는 결혼을 해서 김찬영, 김준영, 김채영 3남매를 낳고 알콩달콩 행복하게 잘 살았습니다.
채영이가 좋아하는 사촌은 김예영이랑 김민영이랍니다. 김서영이는 본지가 너무 오래되었네요.
"""
# 형제 : 김진O
# 자녀 : 김O영

print('-'*70, '\n# 형제들 이름 찾기')
pattern = re.compile("김진\w")

brother = pattern.findall(text)
print(brother)

#sorted 알아서 리스트로 바꿔줌
brother = sorted(set(brother))
print(brother)

print('-'*70, '\n# 아이들 이름 찾기')
pattern = re.compile("김\w영")

children = pattern.findall(text)
print(children)

print('-'*70, '\n# 문장찾기')

# pattern = re.compile("김\w영")

sentence = re.findall('[.]',text)
print(sentence)