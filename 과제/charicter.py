
s= 'The BigpyCraft find the information to design valuable society with Technology & Craft.'

print('대문자\n' + s.upper())
print('소문자\n' + s.lower())

new_s = str()

for c in s:
    if c.islower():
        new_s+=c.upper()
    else:
        new_s+=c.lower()

print('바꿔서\n'+ new_s)
print('바꿔서\n'+ s.swapcase())
