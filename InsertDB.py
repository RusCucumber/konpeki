import dataset
import csv

f = open("konpeki_no_sora.csv", "r")
reader = csv.reader(f)
header = next(reader)

DBMS = "postgresql"
USER = "hzgkkbhhfsktbx"
PASS = "59daad22673fac8ce670d17cefb4db6d8f2e4210f93772d40a1ca4765771e68d"
HOST = "ec2-3-231-16-122.compute-1.amazonaws.com"
DB = "d74j7rocds33bn"

db = dataset.connect("{0}://{1}:{2}@{3}/{4}".format(DBMS, USER, PASS, HOST, DB))
table = db["konpeki"]

data = []

for row in reader:
    data.append({"id": row[0], "url": row[1]})

table.insert_many(data)

