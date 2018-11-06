import sys
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

key = input('please input a key: ')

try:
    print('testing for error')
    print('the value for {0} is {1}'.format(key, dict[key]))

except KeyError:
    print('trapped error')
    print('the key ' + key + ' does not exist')
    sys.exit()

print('program continues..')
