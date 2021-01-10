times = int(input())
keyValue = dict()
for i in range(times):
    key, value = map(int, input().split())
    keyValue[key] = value
orderedKeyValue = sorted(keyValue.items())
for key, value in orderedKeyValue:
    print(key, value)