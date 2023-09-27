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

    def get_popular_review(self):
        tools = dict()
        for item in self.data:
            if item['Free/Paid/Other'] == 'Free':
                if item['Free/Paid/Other'] not in tools.keys():
                    tools[item['Free/Paid/Other']] = item['Review']
                else:
                    tools[item['Free/Paid/Other']] += item['Review']
        return max(tools, key=tools.get)

    def get_popular_free_category(self):
        category = dict()
        for item in self.data:
            if item['Free/Paid/Other'] == 'Free':
                if item['Useable For'] not in category.keys():
                    category[item['Useable For']] = 1
                else:
                    category[item['Useable For']] += 1
        return max(category, key=category.get).replace('/', '')


analys = Analys('./all_ai_tool.csv')
analys.read_data()
print(analys.get_popular_review())
print(analys.get_popular_free_category())

