import json
from csv import DictReader


with open('../files/books.csv', newline='') as b:
    reader = DictReader(b)

    for row in reader:
        title = str(row['Title'])
        author = str(row['Author'])
        height = str(row['Height'])
        print(json.dump(title, author, height))  #  С помощью 'print' получается составить последовательности из csv,
        # но при генерации JSON берется только одно значение, не разобрался как сделать.

with open("../files/users.json", "r") as f:
    data_list = json.loads(f.read())

for name in data_list:
    name_user = name['name']
    gender_user = name['gender']
    address_user = name['address']
    print(name_user, gender_user, address_user)

    result = [{'name': name_user, 'gender': gender_user, 'address': address_user, 'books': [{'title': title, 'author': author, 'height': height}]}]
    # result_2 = [{'title': title, 'author': author, 'height': height}]
    print(result)

    with open("../files/example.json", "w") as g:
        json.dump(result, g, indent=4)  # JSON генерируется только по одной записи
