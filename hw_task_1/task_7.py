def countDay(year, month):
    return year*12*29 + month*29 # было принято, что в году 12 месяцев

print(countDay(1,2))