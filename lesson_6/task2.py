from pympler import asizeof
import sys
import collections

# 1
z = 8
print(asizeof.asizeof(z))
print(sys.getsizeof(z))

print()
print()
print()

# 2
z1 = []
z2 = ()
z3 = {}

z4 = collections.defaultdict(lambda : '', {})
de = collections.deque()

print('dict ', asizeof.asizeof(z1))
print(asizeof.asizeof(z2))
print('set ', asizeof.asizeof(z3))
print(asizeof.asizeof(z4))
print(asizeof.asizeof(de))

print ("*"*30)
z1 = 999999999999999999999999999999999999999999999
z2 = 9999999999999999999999999999999999999999999999.0
z3 = '80'
z4 = 'wwwwwwwwww'
z5 = 'ыыыыыыыыыы'


print("Int = " + str(asizeof.asizeof(z1)))
print("Float = " + str(asizeof.asizeof(z2)))
# print(asizeof.asizeof(z3))
print("Lat = " + str(asizeof.asizeof(z4)))
print("Rus = " + str(asizeof.asizeof(z5)))