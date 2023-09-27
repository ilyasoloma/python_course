import csv
class Analys:
    def __init__(self, path):
        self.path = path
        self.data = []

    def read_data(self):
        with open(self.path, newline='') as dataset:
            tmp = csv.DictReader(dataset)
            for row in tmp:
                self.data.append(row)

    def UFO_favorites_country(self):
        country = dict()
        for item in self.data:
            if item['country'] not in country.keys():
                country[item['country']] = 1
            else:
                country[item['country']] += 1
        return max(country, key=country.get)

    def UFO_favorites_month(self):
        datetime = dict()
        for item in self.data:
            if item['datetime'][:2].replace('/','') not in datetime.keys():
                datetime[item['datetime'][:2].replace('/','')] = 1
            else:
                datetime[item['datetime'][:2].replace('/','')] += 1
        return max(datetime, key=datetime.get)

analys = Analys('nlo.csv')
analys.read_data()
print(analys.UFO_favorites_country())
print(analys.UFO_favorites_month())


