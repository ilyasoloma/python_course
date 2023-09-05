def GetCountStep(prevLevel, CurrLevel):
    if CurrLevel == 0:
        return 1
    count = 0
    for level in range(1, prevLevel):
        count += GetCountStep(level, CurrLevel - level)
    return count

def CalcCountSteps(n):
    count = 0
    for i in range(1, n + 1):
        count += GetCountStep(i, n - i)
    return count

n = 12
count = CalcCountSteps(n)

print(count)