a = 34
b = 27
c = 83

a += c
c = a - c
a = a - c
b += c
c = b - c
b = b - c

print(a, b, c)

# 83 34 27