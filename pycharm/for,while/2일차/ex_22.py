
# BMI만들기

weight=float(input("체중(kg)?"))
height=float(input("키(cm)?"))

height=height/100
bmi=weight/(height*height)

result=''

if bmi<18.5:
   result='마름'
elif (18.5<=bmi) and (bmi<25):
   result='보통'
elif (25<=bmi) and (bmi<30):
   result='가벼운비만'
elif  bmi>=30:
   result = '심한비만'

print('bmi',bmi)
print('판정',result)

