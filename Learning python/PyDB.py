
import pdb

# values = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
#
# for val in values:
#     sum = sum + val
#
# print(sum)

def doubleval(argsum, val):
    argsum = 0
    newval = argsum + val
    return newval

pdb.set_trace()

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for val in values:
    sum = doubleval(sum, val)

print(sum)
