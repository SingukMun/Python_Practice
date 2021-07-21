a, result, i = 100, 0, 0

for i in range(1, 5):
    result = a<<i
    print("%d<<%d = %d" % (a, i, result))

for i in range(1, 5):
    result = a>>i
    print("%d>>%d = %d" % (a, i, result))
