# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return i

    return -1
#Поиск количества различных подстрок в строке
def find_str(s):
    all_s = []
    for i in range(len(s)):
        for j in range(len(s)):
            all_s.append(hashlib.sha1(s[i:i+j].encode('utf-8')).hexdigest())
    print(len(all_s))

print(rabin_karp("sqerwrtestqwf","test"))
find_str("sqerwrtestqwf")
