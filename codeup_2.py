
def getMinCount(lowTemp, highTemp):
    count = 0
    while lowTemp != highTemp:
        count += 1
        if highTemp - lowTemp >= 10:
            lowTemp += 10
            continue
        elif highTemp - lowTemp >=8:
            lowTemp += 10
            continue
        elif highTemp - lowTemp >=3:
            lowTemp += 5
            continue
        elif highTemp - lowTemp >=1:
            lowTemp += 1
        else:
            lowTemp -= 1

    return count

currentTemperature, targetTemperature = map(int, input().split())

if int(currentTemperature) > int(targetTemperature):
    print(getMinCount(int(targetTemperature), int(currentTemperature)))
else:
    print(getMinCount(int(currentTemperature), int(targetTemperature)))
