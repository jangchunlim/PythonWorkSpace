import math
def getCountForChange(change):
    count = 0
    count += math.trunc(change / 50000)
    change = change % 50000
    count += math.trunc(change / 10000)
    change = change % 10000
    count += math.trunc(change / 5000)
    change = change % 5000
    count += math.trunc(change / 1000)
    change = change % 1000
    count += math.trunc(change / 500)
    change = change % 500
    count += math.trunc(change / 100)
    change = change % 100
    count += math.trunc(change / 50)
    change = change % 50
    count += math.trunc(change / 10)
    
    return count

change = int(input())
print(getCountForChange(change))
            