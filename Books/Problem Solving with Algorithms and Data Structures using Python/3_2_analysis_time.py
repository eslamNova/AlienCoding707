import time


def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    return theSum


def sumOfN2(n):
    start = time.time()
    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end-start


def sumOfN3(n):
    start = time.time()
    thesum = (n*(n+1))/2
    end = time.time()
    return thesum, end-start


nums = [1000, 10000, 100000, 1000000, 10000000, 100000000]
for i in nums:
    print("Sum<<<2>>> is %d required %10.7f seconds" % sumOfN2(i))
    print("Sum***3*** is %d required %10.9f seconds" % sumOfN3(i))
