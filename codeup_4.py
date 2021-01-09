import math

def getAverage(topingCalorie):
    sum = 0
    for i in topingCalorie:
        sum += i
    return sum/len(topingCalorie)

topingCount = int(input())
doughPrice, topingPrice = map(int, input().split())
doughCalorie = int(input())
topingCalorie = set()
for i in range(0, topingCount):
    eachCalorie = int(input())
    set.add(eachCalorie)



totalPrice = doughPrice + topingCount * topingPrice
totlaCalorie = doughCalorie + topingCalorie
print(math.trunc(totlaCalorie/totalPrice))





print(
572
+1110
+2530
+472
+1060
+1861
+1649
+463
+430)

print(10147/91)

# 8
# 11 10
# 572
# 1110
# 2530
# 472
# 1060
# 1861
# 1649
# 463
# 430

# 112 -> 161 