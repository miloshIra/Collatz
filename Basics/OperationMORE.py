c = [1, 2, 3]
a = [1, 2, 3]
b = a

res_equality = (a==c)
res_is1 = (a is c)
res_isnot1 = (a is not c)
res_is2 = (a is b)
res_isnot2 = (a is not b)


print("a == c = ", res_equality)
print("a is c = ", res_is1)
print("a is not c = ", res_isnot1)
print("____________________________")
print("a is b = ", res_is2)
print("a is not b = ", res_isnot2)

