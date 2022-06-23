
#중복제거

beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast =', unique_beast)
sorted_beast = sorted(unique_beast)
print("sorted_beast =", sorted_beast)

