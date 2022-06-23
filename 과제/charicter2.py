
s='Lief is too short, You nee Python.'

new_s=str()
print(list(range(len(s)-1,-1,-1)))
r_new_s=str()

for c in s:
    r_new_s = c+r_new_s
print(r_new_s)

for c in range(len(s)-1,-1,-1):
    new_s+=s[c]
print(new_s)

print(s[::-1])
print(s)



