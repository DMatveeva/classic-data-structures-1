def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(32)[::-1])

str1 = '0123456789'
filter_len = 32
res1 = 0
for c in str1:
    code = ord(c)
    res = (res1 * 17 + code) % filter_len
print(res1)

res2 = 0
for c in str1:
    code = ord(c)
    res2 = (res2 * 223 + code) % filter_len
print(res2)

a = 0
a = a ^ res1
a = a ^ res2
print(a)
print(toBinary(res1))
print(toBinary(res2))
print(toBinary(a))
print(a & res2 != 0)


