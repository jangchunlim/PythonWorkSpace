

def getDifference(current, target):
    count = 0
    while current != target:
        if target - current >= 5:
            count += 1
            current += 5
            continue
        elif current - target >= 5:
            count += 1
            target += 5
            continue
        if target > current:
            count += 1
            current += 1
            continue
        elif current > target:
            count += 1
            target += 1
            continue
    return count

currentTemperature, targetTemperature = map(int, input().split())

print(getDifference(int(currentTemperature/10),int(targetTemperature/10))
+getDifference(int(currentTemperature%10),int(targetTemperature%10)))


# requirementCount += int(targetTemperucter / 10)
# targetTemperucter = targetTemperucter % 10
# requirementCount += int(targetTemperucter / 5)
# targetTemperucter = targetTemperucter % 5
# requirementCount += int(targetTemperucter)

# 5이상이면 +5해주면서 카운트 업, 1이상이면 +1해주면서 카운트 업
            
