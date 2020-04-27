import time
from random import randrange


def findMin(list):
    """O(n2)"""
    overallmin = list[0]
    for i in list:
        issmallest = True
        for j in list:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


def findMin2(list):
    """O(n)"""
    minsofar = list[0]
    for i in list:
        if i < minsofar:
            minsofar = i
    return minsofar


# print(findMin([5, 4, 3, 2, 1, 0]))
# print(findMin([52, 47, 36, 25, 12, 6]))

for listSize in range(1000, 10001, 1000):
    list = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(list))
    end = time.time()
    print("Size %d time %f" % (listSize, end-start))
