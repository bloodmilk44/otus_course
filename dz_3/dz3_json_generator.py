import json
from csv import DictReader


with open('../files/books2.csv', newline='') as b:
    reader = DictReader(b)

    title_list = []

    for row in reader:
        book_list = {}
        book_list['Title'] = str(row['Title'])
        book_list['Author'] = str(row['Author'])
        book_list['Height'] = str(row['Height'])
        title_list.append(book_list)

with open("../files/users.json", "r") as f:
    data_list = json.loads(f.read())


result_2 = []
for name in data_list:
    book = {}
    book['name'] = name['name']
    book['gender'] = name['gender']
    book['address'] = name['address']
    book['books'] = [title_list.pop(0)] if len(title_list) > 0 else []
    result_2.append(book)

with open("../files/example.json", "w") as g:
    g.write(json.dumps(result_2, indent=4))