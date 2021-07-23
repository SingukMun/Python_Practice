i, k = 0, 0

for i in range(2, 10, 1) :
    print("<%d단 입니당~~>" % i)
    for k in range(1, 10, 1) :
        print(" %d x %d = %d " % (i, k, i*k))
    print("")
